import unittest

from databasetest import Article, NoletterError, NotaLinkError, NotaTitleError


class ScoreGoodOutput(unittest.TestCase):
def test_percentage(self):
    """we should always return a score between 0 to 100"""
    article =https://www.bbc.com/news/world-latin-america-52644339
    self.assertTrue(0=<Score(article)=<100)


class ScoreBadInput(unittest.TestCase):

    def test_number(self):
        """score should fail with numeral input"""
        article = 7589
        self.assertRaises(NoletterError, Score(article))

    def test_wronglink(self):
        """score should fail with a link that doesn't work"""
         article = wwh.google.com
        self.assertRaises(NotaLinkError, Score(article))
    def test_wrongTitle(self):
        """score should fail with a title that doesn't correspond to any article"""
         article = Why qh WHY
        self.assertRaises(NotaTitleError, Score(article))

if __name__ == "__main__":
    unittest.main()
