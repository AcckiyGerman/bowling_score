from random import randint


class Player:
    def __init__(self, name=""):
        self.name = name
        self.rolls = []
        self.frames = []
        self.scores = []


class Game:
    def __init__(self, *names):
        self.players = [Player(name) for name in names]
