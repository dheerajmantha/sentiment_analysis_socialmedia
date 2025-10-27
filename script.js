document.addEventListener('DOMContentLoaded', () => {
    const textInput = document.getElementById('textInput');
    const analyzeButton = document.getElementById('analyzeButton');
    const resultsOutput = document.getElementById('resultsOutput');

    analyzeButton.addEventListener('click', async () => {
        const text = textInput.value;
        if (!text.trim()) {
            resultsOutput.textContent = 'Please enter some text to analyze.';
            return;
        }

        resultsOutput.textContent = 'Analyzing...';
        analyzeButton.disabled = true;

        try {
            const response = await fetch('/api/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text: text }),
            });

            if (!response.ok) {
                throw new Error(`Error: ${response.statusText}`);
            }

            const data = await response.json();
            
            // Format the JSON data for beautiful output
            const formattedResults = JSON.stringify(data, null, 2);
            resultsOutput.textContent = formattedResults;

        } catch (error) {
            console.error('Analysis error:', error);
            resultsOutput.textContent = `An error occurred: ${error.message}`;
        } finally {
            analyzeButton.disabled = false;
        }
    });
});
