import random


class Dictionary(object):
    def __init__(self, f="../data/dictionary.txt"):
        self.word_choice = None
        try:
            with open(f) as file:
                list = []
                counter = 0
                for line in file:
                    for word in line.split():
                        list.append(word)
                        counter += 1
                if counter < 10:
                    print("Brakuje jeszcze slow w pliku! Jest", counter, "a powinno byc min 10")
                    exit(1)
        except FileNotFoundError:
            print("Nie znaleziono pliku")
            exit(1)
        self.dane = list

    def return_word(self, dificulty):
        if dificulty < 1 or dificulty > 3:
            print("Podano zla liczbe, ustawiono domysly poziom trudnosci")
        elif dificulty == 1:
            word_easy = [word for word in self.dane if len(word) <= 4]
            self.word_choice = random.choice(word_easy)
        elif dificulty == 2:
            word_medium = [word for word in self.dane if 7 >= len(word) > 4]
            self.word_choice = random.choice(word_medium)
        elif dificulty == 3:
            word_hard = [word for word in self.dane if len(word) > 7]
            self.word_choice = random.choice(word_hard)
        return self.word_choice
