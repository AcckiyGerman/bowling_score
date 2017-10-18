from random import randint


class Player:
    def __init__(self, name=""):
        self.name = name
        self.rolls = []
        self.frames = []
        self.scores = []

    def roll(self, bottles):
        """
        The Player tosses a ball, and knocks down random number
        of bottles.  0 <= result <= bottles
        Result is saved in self.rolls for future score calculations.
        return: integer
        """
        result = randint(0, bottles)
        self.rolls.append(result)
        return result

    def play_frame(self):
        """
        The player rolls a ball one (if strike) or two times.
        Results are saved in self.frames;
        The tenth frame could be three rolls long to satisfy
        spare or strike bonus (see bowling rules)
        """
        frame = []
        roll1 = self.roll(10)
        frame.append(roll1)
        if roll1 == 10:  # strike
            # check for tenth frame
            if len(self.frames) == 9:
                roll2 = self.roll(10)
                frame.append(roll2)
                roll3 = self.roll(10-roll2 or 10)
                frame.append(roll3)
        else:
            roll2 = self.roll(10-roll1)
            frame.append(roll2)
            # check for spare in tenth frame
            if len(self.frames) == 9 and sum(frame) == 10:
                frame.append(self.roll(10))  # roll3
        # save the frame
        self.frames.append(frame)
        # debug
        # print(frame, end="")

    def calculate_frames_score(self):
        """
        Define each frame score. Save results in self.scores
        """
        self.scores = []
        ri = 0  # roll index
        for frame in self.frames:
            if sum(frame) < 10:  # usual frame
                self.scores.append(sum(frame))
                ri += 2  # there are two rolls in a usual frame
            try:
                if frame == [10]:  # strike
                    self.scores.append(
                        # frame result + strike bonus
                        self.rolls[ri] + self.rolls[ri+1] + self.rolls[ri+2]
                    )
                    ri += 1  # one roll in frame, when there was a strike
                # spares and final frame
                elif sum(frame) >= 10:
                    if len(frame) == 2:  # spare frame
                        self.scores.append(sum(frame) + self.rolls[ri+2])
                    else:  # final frame
                        self.scores.append(sum(frame))
                    ri += 2
            except IndexError:  # seems that rolls are over
                break  # so we couldn't calculate the bonus

    def __str__(self):
        """
        Prints player name, fancy looking frames and scores table,
        and the Total score.
        """
        print('Player: ', self.name)
        for frame in self.frames:
            print(self.format_frame(frame), end="")
        for score in self.scores:
            print(self.format_score(score), end="")
        print('Total score:', sum(self.scores))

    @staticmethod
    def format_frame(frame):
        """:return: fancy string representing frame"""
        # last frame
        if len(frame) == 3:
            roll1 = 'X' if frame[0] == 10 else frame[0] or '-'
            if frame[0] + frame[1] == 10 and frame[1]:
                roll2 = '/'
            elif frame[1] == 10:
                roll2 = 'X'
            else:
                roll2 = frame[1] or '-'
            roll3 = 'X' if frame[2] == 10 else frame[2] or '-'
            return '|%s %s %s|' % (roll1, roll2, roll3)
        # usual or spare frame
        elif len(frame) == 2:
            roll1 = frame[0] or '-'
            roll2 = '/' if sum(frame) == 10 else frame[1] or '-'
            return '| %s %s |' % (roll1, roll2)
        # strike
        elif len(frame) == 1:
            return "|   X |"

    @staticmethod
    def format_score(score):
        """:return: fancy string representing score for one frame"""
        return '|  %2d |' % score


class Game:
    def __init__(self, *names):
        self.players = [Player(name) for name in names]
