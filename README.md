# Social Media Sentiment Analysis

This is a simple web application that analyzes the sentiment of a given piece of text (like a tweet or comment). It classifies the text as Positive, Negative, or Neutral and provides detailed scores.

This project is built to be deployed seamlessly on Vercel.

## Tech Stack

* **Frontend:** Plain HTML, CSS, and Vanilla JavaScript
* **Backend:** Python Serverless Function (hosted on Vercel)
* **Sentiment Library:** [VADER (Valence Aware Dictionary and sEntiment Reasoner)](https://github.com/cjhutto/vaderSentiment)

## How It Works

1.  The user enters text into the `textarea` on the `index.html` page.
2.  The JavaScript (`script.js`) sends this text to the backend API endpoint (`/api/analyze`).
3.  The Vercel-hosted Python function (`api/analyze.py`) receives the request.
4.  It uses the `vaderSentiment` library to analyze the text.
5.  It returns a JSON object with the overall sentiment and detailed scores (positive, negative, neutral, compound).
6.  The JavaScript receives the JSON and displays it in the results box.

## How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/dheerajmantha/sentiment_analysis_socialmedia.git](https://github.com/dheerajmantha/sentiment_analysis_socialmedia.git)
    cd sentiment_analysis_socialmedia
    ```

2.  **Install Vercel CLI** (for running the serverless function locally):
    ```bash
    npm install -g vercel
    ```

3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the development server:**
    ```bash
    vercel dev
    ```
    This will start a local server (usually on `http://localhost:3000`) that mimics the Vercel production environment, running both the static frontend and the Python API.

## Deployment to Vercel

This project is configured for instant deployment on Vercel.

1.  Push this repository to your GitHub account.
2.  Go to your [Vercel Dashboard](https://vercel.com/dashboard).
3.  Click "Add New... Project".
4.  Select your GitHub account and import the `sentiment_analysis_socialmedia` repository.
5.  Vercel will automatically detect it as a Python project.
6.  Click "Deploy". Your site will be live in moments.
