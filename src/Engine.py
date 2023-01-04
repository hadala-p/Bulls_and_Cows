import Dictionary
import Validator
from Stats import Stats
import Subtitles
import datetime
import time


class Engine(object):
    highscores = []
    game_run = False

    def __init__(self):
        self.dictionary = Dictionary.Dictionary()
        self.subtitles = Subtitles.Subtitles(self)
        self.validator = Validator.Validator()
        self.stats = Stats(0, 0, None)
        self.difficulty = 2
        self.trials = 10
        self.word = None
        self.win = None
        self.start()

    def num_of_tries(self):
        print("Obecna ustawiono ilosc prob:", self.trials, "(Domyslnie: 10)")
        input_not = int(input('Podaj ile chcesz miec prob na odgadniecie hasla (max 30): '))
        while input_not not in range(1, 31):
            input_not = int(input("Podaj liczbe z zakresu (1-30):"))
        self.trials = input_not

    def change_difficulty(self):
        if self.difficulty == 1:
            print("Obecny ustwiony poziom trudnosci to latwy  (Domyslnie: Sredni)")
        elif self.difficulty == 2:
            print("Obecny ustwiony poziom trudnosci to: Sredni  (Domyslnie: Sredni)")
        elif self.difficulty == 3:
            print("Obecny ustwiony poziom trudnosci to: Trudny  (Domyslnie: Sredni)")
        input_difficulty = int(input('Podaj poziom trudnosci:\n1) Latwy\n2)Sredni\n3)Trudny'))
        while input_difficulty not in range(1, 4):
            input_difficulty = int(input('\nPodano zla liczbe!\nPodaj poziom trudnosci:\n1) Latwy\n2)Sredni\n3)Trudny'))
        self.difficulty = input_difficulty

    def add_dictionary_word(self):
        print("a)Slowo musi byc izogramem\n"
              "b)Zawierac min 3 litery\n"
              "c)Nie zawierac liczb oraz nie dozwolonych znakow")
        word_input = input("Podaj slowo:")
        word_input = word_input.lower()
        for wyraz in self.dictionary.dane:
            if wyraz == word_input:
                print("Ten wyraz znajduje sie juz w pliku")
                time.sleep(4)
                return
        if self.validator.word_add_dictionary(word_input):
            try:
                f = open('dictionary.txt', 'a')
                f.write("\n")
                f.write(str(word_input))
            except FileNotFoundError:
                print("Nie znaleziono pliku")
            print(f"Slowo {word_input} zostalo dodane do dictionary.txt")
            time.sleep(4)
        else:
            print(f"Slowo {word_input} nie moze byc dodane do pliku")
            time.sleep(4)

    def start_game(self):
        self.game_run = True
        self.word = self.dictionary.return_word(self.difficulty)
        del self.highscores[1:]
        self.stats = (0, 0, "-")
        self.win = False

    def stop_game(self):
        self.game_run = False

    def highscore_to_file(self):

        try:
            f = open('../data/highscore.txt', 'a')
            f.write(f"---------------------------------------------\n")
            f.write(f"Data i godzina gry: {datetime.datetime.now()}\n")
            f.write(f"Wylosowane slowo: {self.word}\n")
            f.write(f"\nWybrana poczatkowa ilosc prob: {self.trials}")
            i = 0
            for x in range(len(self.highscores)):
                if i != 0:
                    f.write("\nPróba: ")
                    f.write(str(i))
                    f.write(")   ")
                    f.write(str(self.highscores[i]))
                i += 1
            f.write(f"\n---------------------------------------------\n")
        except FileNotFoundError:
            print("Blad!")

    def start(self):
        self.running()

    def running(self):
        self.subtitles.show_subtitles("")
        arg = input()
        while True:
            if self.subtitles.current_position != 4:
                self.subtitles.show_subtitles(arg)
            arg = input()

    def stats_add(self, word_user):
        current_highscore = self.validator.bulls_or_cows(self.word, word_user)
        self.highscores.append(Stats(current_highscore[0], current_highscore[1], word_user))
        if current_highscore[0] == len(self.word):
            self.win = True
            self.subtitles.current_position = 4
            self.subtitles.show_game_end()
            return
        if len(self.highscores) > self.trials:
            self.win = False
            self.subtitles.current_position = 4
            self.subtitles.show_game_end()
            return
