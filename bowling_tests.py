import unittest
from bowling import Game, Player


class TestPlayer(unittest.TestCase):
    def testPlayerInit(self):
        self.assertEqual(
            Player('John').__dict__,
            {'name': 'John', 'rolls': [], 'scores': [], 'frames': []}
        )


class TestGame(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
