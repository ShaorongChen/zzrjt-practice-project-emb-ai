"""
Test module for sentiment analysis functionality.
This module contains test cases to verify the correctness of 
the sentiment_analyzer function for different sentiment types.
"""

import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):
    """
    Test class for the sentiment analysis functionality.
    This class contains test cases to verify the correctness of 
    the sentiment_analyzer function for different sentiment types.
    """

    def test_sentiment_analyzer(self):
        """
        Test the sentiment analyzer with various input strings
        to ensure it correctly identifies positive, negative, and neutral sentiments.
        """
        # Test case for positive sentiment
        result_1 = sentiment_analyzer('I love working with Python')
        self.assertEqual(result_1['label'], 'SENT_POSITIVE')
        # Test case for negative sentiment
        result_2 = sentiment_analyzer('I hate working with Python')
        self.assertEqual(result_2['label'], 'SENT_NEGATIVE')
        # Test case for neutral sentiment
        result_3 = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(result_3['label'], 'SENT_NEUTRAL')

unittest.main()