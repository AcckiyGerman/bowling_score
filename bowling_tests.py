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

    def testPlayFrame(self):
        """
        Method should append a valid frame to the player.frames:
        [10]  # strike
        [6, 0]  # usual frame
        [x, x] or [x,x,x]  # tenth frame
        """
        for _ in range(200):
            p = Player()
            for i in range(9):
                p.play_frame()
                frame = p.frames[i]
                self.assertTrue(type(frame) == list)
                self.assertTrue(1 <= len(frame) <= 2)
                self.assertTrue(0 <= sum(frame) <= 10)
                if len(frame) == 1:
                    self.assertEqual(frame, [10])
                # check frames are stored
                self.assertEqual(len(p.frames), i+1)
                self.assertTrue(p.frames[i] is frame)
            # last frame
            p.play_frame()
            frame = p.frames[9]
            self.assertTrue(2 <= len(frame) <= 3)
            self.assertTrue(0 <= sum(frame) <= 30)
            self.assertEqual(len(p.frames), 10)


class TestGame(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
