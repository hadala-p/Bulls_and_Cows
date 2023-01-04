class Stats(object):
    bulls = 0
    cows = 0
    word = None

    def __init__(self, bulls, cows, word):
        self.bulls = bulls
        self. cows = cows
        self.word = word

    def __repr__(self):
        return "Bulls:" + str(self.bulls) + " / Cows: " + str(self.cows) + " / Wyraz: " + str(self.word)
