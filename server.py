'''This module provides a Flask web application for sentiment analysis.

The application exposes two endpoints:
- /: Renders the main index page
- /sentimentAnalyzer: Performs sentiment analysis on text provided as a query parameter

The sentiment analysis is performed using the sentiment_analyzer function from the 
SentimentAnalysis.sentiment_analysis module.
'''

from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")


@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """Analyze the sentiment of the provided text.

    This function receives text through the 'textToAnalyze' query parameter,
    performs sentiment analysis, and returns the label and confidence score.

    Args:
        None

    Returns:
        str: A formatted string containing the sentiment label and confidence score,
             or an error message if the input is invalid.

    Example:
        Input: textToAnalyze=I love this product!
        Output: The given text has been identified as positive with a score of 0.98.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Check if no text was provided at all
    if text_to_analyze is None:
        return "Invalid input! Try again."

    # Check if the text is blank (empty string)
    if text_to_analyze.strip() == "":
        return "Please enter text to analyze."

    # Pass the text to the sentiment_analyzer function and store the response
    response = sentiment_analyzer(text_to_analyze)

    # Extract the label and score from the response
    label = response['label']
    score = response['score']

    # Check if the label is None, indicating an error or invalid input
    if label is None:
        return "Invalid input! Try again."
    else:
        # Return a formatted string with the sentiment label and score
        return f"The given text has been identified as {label.split('_')[1]} with a score of {score}."


@app.route("/")
def render_index_page():
    """Render the main application index page.

    This function handles the root URL and returns the rendered HTML template
    for the main application page.

    Args:
        None

    Returns:
        The rendered index.html template.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
