from http.server import BaseHTTPRequestHandler
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        # Get the size of the incoming data
        content_length = int(self.headers.get('Content-Length', 0))
        
        # Read the data
        post_data = self.rfile.read(content_length)
        
        try:
            # Parse the JSON data
            data = json.loads(post_data)
            text_to_analyze = data.get('text')

            if not text_to_analyze:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'No text provided'}).encode('utf-8'))
                return

            # Initialize the VADER analyzer
            analyzer = SentimentIntensityAnalyzer()
            sentiment = analyzer.polarity_scores(text_to_analyze)

            # Determine overall sentiment
            if sentiment['compound'] >= 0.05:
                overall = 'Positive'
            elif sentiment['compound'] <= -0.05:
                overall = 'Negative'
            else:
                overall = 'Neutral'
            
            # Prepare the response
            response_data = {
                'overall_sentiment': overall,
                'scores': {
                    'positive': sentiment['pos'],
                    'neutral': sentiment['neu'],
                    'negative': sentiment['neg'],
                    'compound': sentiment['compound']
                },
                'original_text': text_to_analyze
            }

            # Send the successful response
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*') # Add CORS header for safety
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode('utf-8'))

        except json.JSONDecodeError:
            self.send_response(400)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Invalid JSON'}).encode('utf-8'))
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))
            
        return
