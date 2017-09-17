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
        self.assertEqual(self.x_Card.rank_num, 3, "testing the rank_num variable")

    def test_rank(self):
        self.assertEqual(self.y_Card.rank, "Queen", "testing the rank_num variable")

    def test_rank(self):
        self.assertEqual(self.y_Card.rank_num, 12, "testing the rank_num variable")

    # Error #1: Doesn't give face value of cards
    def test_string_method2(self):
        x_Card = Card(2, 1)
        self.assertEqual(x_Card.__str__(), "Ace of Hearts",
                         "testing the string method of Card with face value")

class Test_Deck(unittest.TestCase):
    def setUp(self):
        self.x_Deck = Deck()

    def test_Deck1(self):
        self.assertEqual(type(self.x_Deck.cards), type([1, 2, 3]),
                         "testing that cards variable creates a list")

    def test_Deck2(self):
        Deck_string = self.x_Deck.__str__()
        self.assertIn("3 of Hearts", Deck_string,
                      "testing string method of Deck with the number value")

    def test_Deck3(self):
        Deck_string = self.x_Deck.__str__()
        self.assertEqual(len(Deck_string.split('\n')), 52,
                         "testing the number of cards in the deck")

    def test_Deck4(self):
        self.x_Deck.deal_hand(2)
        self.assertEqual(len(self.x_Deck.cards), 50,
                         "testing that deal_hand removes cards from deck")

    def test_Deck4(self):
        self.x_Deck.pop_card(2)
        self.assertEqual(len(self.x_Deck.cards), 51,
                         "testing that pop_card removes cards from deck")

    # Error #2: sort_cards does not sort remaining cards in deck: gives full
    #  deck length
    def test_Deck5(self):
        self.x_Deck.deal_hand(3)
        self.x_Deck.sort_cards()
        self.assertEqual(len(self.x_Deck.cards), 49,
                         "testing that sort_cards sorts only remaining cards in deck")

    # Error #1: must reference Cards method, doesn't give face value of card
    def test_Deck6(self):
        Deck_string = self.x_Deck.__str__()
        self.assertIn("Ace of Hearts", Deck_string,
                      "testing string method of Deck with face value")

    def test_Deck7(self):
        self.assertEqual(len(self.x_Deck.deal_hand(5)), 5,
                         "testing the length of deal_hand")

    def test_Deck8(self):
        self.assertEqual(len(self.x_Deck.deal_hand(52)), 52,
                         "testing the maximum length that deal_hand can take from deck")

    # Error #3: deal_hand cannot handle taking out large values from deck
    def test_Deck9(self):
        self.assertEqual(len(self.x_Deck.deal_hand(27)), 27,
                         "testing larger inputs for deal_hand to take from deck")

    def test_Deck10(self):
        self.assertEqual(len(self.x_Deck.deal_hand(20)), 20,
                         "testing medium inputs for deal_hand to take from deck")

class Testing_playWarGames(unittest.TestCase):
    def test_tuple(self):
       result = play_war_game(True)
        self.assertTrue(type(result), tuple)
        self.assertTrue(type(result[0]), str)
        self.assertTrue(type(result[1]), int)
        self.assertTrue(type(result[2]), int, " Testing to make sure a tuple is returned")


if __name__ == '__main__':
    unittest.main(verbosity=2)
