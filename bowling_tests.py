import unittest
from bowling import Game, Player


class TestPlayer(unittest.TestCase):
    def testPlayerInit(self):
        self.assertEqual(
            Player('John').__dict__,
            {'name': 'John', 'rolls': [], 'scores': [], 'frames': []}
        )

    def testRoll(self):
        """Player.roll() uses randint, thus we testing it many times"""
        p = Player()
        for i in range(200):
            self.assertTrue(
                0 <= p.roll(10) <= 10
            )
            self.assertEqual(len(p.rolls), i+1)


class TestGame(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
