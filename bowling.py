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


class Game:
    def __init__(self, *names):
        self.players = [Player(name) for name in names]
