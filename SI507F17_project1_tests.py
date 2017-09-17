import unittest
from SI507F17_project1_cards import *

class Test_Card(unittest.TestCase):
    def setUp(self):
        self.x_Card = Card(1, 3)
        self.y_Card = Card(1, 12)

    def test_string_method1(self):
        self.assertEqual(self.x_Card.__str__(), "3 of Clubs",
                         "testing string method Card with number value")

    def test_suit(self):
        self.assertEqual(self.x_Card.suit, "Clubs", "testing suit variable")

    def test_rank_num(self):
        self.assertEqual(self.x_Card.rank_num, 3, "testing rank_num variable")

    def test_rank(self):
        self.assertEqual(self.y_Card.rank, "Queen", "testing rank variable")

    def test_rank(self):
        self.assertEqual(self.y_Card.rank_num, 12, "testing rank_num variable")

    # Error #1: Doesn't give face value of cards
    def test_string_method2(self):
        x_Card = Card(2, 1)
        self.assertEqual(x_Card.__str__(), "Ace of Hearts", "testing string "
                         "method of Card with face value")





if __name__ == '__main__':
    unittest.main(verbosity=2)
