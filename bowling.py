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


class Game:
    def __init__(self, *names):
        self.players = [Player(name) for name in names]
