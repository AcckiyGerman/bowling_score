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

    def testCalculateFramesScore(self):
        # test table structure: [(rolls, frames, frame_scores), ...]
        # It looks huge and ugly :(  but since the player.roll() and
        # player.play_frames() methods give random results each time,
        # I did not find a better way to emulate the game process in the test.
        # so I will assign Player.rolls and Player.frames, call the testing
        # function and check the Player.scores

        # if there is not enough rolls to define all the bonuses,
        # then the frame score is yet undefined
        games_list = [
            ([0, 0], [[0, 0]], [0]),
            ([5, 4], [[5, 4]], [9]),

            ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),

            ([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
             [[4, 4], [4, 4], [4, 4], [4, 4], [4, 4], [4, 4], [4, 4], [4, 4], [4, 4], [4, 4]],
             [8, 8, 8, 8, 8, 8, 8, 8, 8, 8]),

            # Strikes.
            ([10, 2, 2], [[10], [2, 2]], [14, 4]),
            ([1, 1, 10, 3, 3], [[1, 1], [10], [3, 3]], [2, 16, 6]),
            ([10, 10, 10], [[10], [10], [10]], [30]),

            # Strike in the last frame
            ([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
             [[10], [10], [10], [10], [10], [10], [10], [10], [10], [10, 10, 10]],
             [30, 30, 30, 30, 30, 30, 30, 30, 30, 30]),

            ([1, 1, 2, 2, 4, 4, 3, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 2, 2],
             [[1, 1], [2, 2], [4, 4], [3, 5], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [10, 2, 2]],
             [2, 4, 8, 8, 0, 0, 0, 0, 0, 14]),

            # Spares
            ([2, 8], [[2, 8]], []),
            ([0, 10], [[0, 10]], []),
            ([0, 10, 1, 0], [[0, 10], [1, 0]], [11, 1]),
            ([5, 5, 5, 4], [[5, 5], [5, 4]], [15, 9]),
            ([0, 5, 5, 0], [[0, 5], [5, 0]], [5, 5]),  # not a spare
            ([5, 5, 5, 5], [[5, 5], [5, 5]], [15]),  # second spare is not defined yet
            ([9, 1, 1, 1], [[9, 1], [1, 1]], [11, 2]),
            # spare in the last frame
            ([0, 0, 5, 5, 0, 0, 4, 6, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 5],
             [[0, 0], [5, 5], [0, 0], [4, 6], [8, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 10, 5]],
             [0, 10, 0, 18, 8, 0, 0, 0, 0, 15]),
            # mixed
            ([10, 5, 5, 3, 0], [[10], [5, 5], [3, 0]], [20, 13, 3]),
            ([0, 10, 10, 0, 0], [[0, 10], [10], [0, 0]], [20, 10, 0]),

            ([0, 0, 2, 8, 10, 3, 3],
             [[0, 0], [2, 8], [10], [3, 3]],
             [0, 20, 16, 6]),

            ([0, 0, 5, 5, 0, 0, 4, 6, 8, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 10, 5],
             [[0, 0], [5, 5], [0, 0], [4, 6], [8, 0], [0, 0], [0, 0], [0, 0], [0, 10], [0, 10, 5]],
             [0, 10, 0, 18, 8, 0, 0, 0, 10, 15]),

            ([0, 0, 5, 5, 0, 0, 4, 6, 8, 0, 0, 0, 0, 0, 0, 0, 10, 0, 10, 5, 0],
             [[0, 0], [5, 5], [0, 0], [4, 6], [8, 0], [0, 0], [0, 0], [0, 0], [10, 0], [10, 5, 0]],
             [0, 10, 0, 18, 8, 0, 0, 0, 20, 15])
        ]

        p = Player()
        for rolls, frames, scores in games_list:
            p.rolls = rolls
            p.frames = frames
            p.calculate_frames_score()
            self.assertEqual(scores, p.scores)


class TestGame(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
