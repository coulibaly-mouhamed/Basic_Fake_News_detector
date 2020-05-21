
import unittest

import manage_class
from fact_checking_nlp import *


class ScoreGoodOutput(unittest.TestCase):
    def test_percentage(self):
        """we should always return a score between 0 to 100"""
        title ="Hillary Clinton lost US elections"
        self.assertTrue(0<=fact_checking(title)<=100)


class ScoreBadInput(unittest.TestCase):
    def test_wronglink(self):
        """score should fail with a link that doesn't work"""
        article = "wwh.google.com"
        self.assertRaises(manage_class.not_a_link, fact_checking_score_url,article)
    def test_wrongTitle(self):
        """score should fail with a title that doesn't correspond to any article"""
        title =""
        self.assertRaises(manage_class.invalid_input, fact_checking,title)

if __name__ == "__main__":
    unittest.main()