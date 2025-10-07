"""
Sentiment Analysis Module

This module provides functionality to analyze the sentiment of text using the Watson NLP API.
It includes a function to send text to the sentiment analysis service and return the sentiment label and score.

Functions:
    sentiment_analyzer(text_to_analyse): Analyze the sentiment of the given text using Watson NLP API.
"""

import json
import requests

def sentiment_analyzer(text_to_analyse):
    """
    Analyze the sentiment of the given text using Watson NLP API.
    
    This function sends a POST request to the Watson Sentiment Analysis API
    to determine the sentiment label and score of the provided text.
    
    Args:
        text_to_analyse (str): The text to analyze for sentiment
        
    Returns:
        dict: A dictionary containing the sentiment label and score with keys 'label' and 'score'.
              Returns {'label': None, 'score': None} if the API request fails or returns an error status code.
              
    Example:
        >>> sentiment_analyzer("I love this product!")
        {'label': 'POSITIVE', 'score': '0.95'}
        
    Note:
        The function handles both successful responses (status code 200) and 
        server errors (status code 500) appropriately.
    """
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header, timeout=10)

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    # Initialize variables to avoid possibly used before assignment error
    label = None
    score = None

    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    # If the response status code is 500, set label and score to None
    elif response.status_code == 500:
        label = None
        score = None

    # Return the label and score in a dictionary
    return {'label': label, 'score': score}