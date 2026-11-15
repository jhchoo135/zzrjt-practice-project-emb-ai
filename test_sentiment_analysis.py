''' Tests the sentiment_analysis module
'''
import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):
    ''' The class to test the sentiment_analyzer function
    '''
    def test_sentiment_analyzer(self):
        ''' The function to test the sentiment_analyzer function
        '''
        result1 = sentiment_analyzer("I love working with Python.")
        self.assertEqual(result1["label"], "SENT_POSITIVE")

        result2 = sentiment_analyzer("I hate working with Python.")
        self.assertEqual(result2["label"], "SENT_NEGATIVE")

        result3 = sentiment_analyzer("I am neutral on Python")
        self.assertEqual(result3["label"], "SENT_NEUTRAL")

unittest.main()
