from Stats import Stats


class Subtitles(object):
    engine = None
    current_position = 0

    def __init__(self, engine):
        self.engine = engine

    def clear(self):
        print("\n" * 20)

    def update(self):
        self.show_subtitles("")

    def set_position(self, position):
        self.current_position = position
        if self.current_position == 0:
            self.engine.stop_game()
        self.update()

    def show_subtitles(self, position):
        self.clear()
        if self.current_position == 0:
            self.show_menu(position)
        elif self.current_position == 1:
            self.show_rules(position)
        elif self.current_position == 2:
            self.show_settings(position)
        elif self.current_position == 3:
            self.show_game_start(position)
        elif self.current_position == 4:
            self.show_game_end()

    def show_settings(self, num_settings):
        print("Ustawienia\n"
              "1)Wybierz poziom trudnosci\n"
              "2)Wybierz ilosc prob\n"
              "3)Dodaj nowe slowo do dictionary.txt\n"
              "4)Powroc do menu")

        if num_settings == "1":
            self.clear()
            self.engine.change_difficulty()
            self.update()
        elif num_settings == "2":
            self.clear()
            self.engine.num_of_tries()
            self.update()
        elif num_settings == "3":
            self.clear()
            self.engine.add_dictionary_word()
            self.update()
        elif num_settings == "4":
            self.set_position(0)

    def show_menu(self, num_menu):
        print("Witaj w Bulls and Cows!\n"
              "Wybierz co chcesz zrobic:\n"
              "1)Nowa gra\n"
              "2)Zasady gry\n"
              "3)Ustawienia gry\n"
              "4)Zakoncz gre\n")

        if num_menu == "1":
            self.engine.start_game()
            self.set_position(3)
        elif num_menu == "2":
            self.set_position(1)
        elif num_menu == "3":
            self.set_position(2)
        elif num_menu == "4":
            exit(1)

    def show_rules(self, num_rules):
        print("Komputer losuje slowo z listy a nastepnie twoim zadaniem jest je odgadnac\n"
              "Po wpisaniu hasla dostajemy inforamcje zwrotna o ilosci Bulls i Cows\n"
              "Bulls czyli ilosc liter ktora podales i wystepuje ona tez w szukanym slowie\n"
              "oraz Cows o ilosci zgadnietych liter na dobrym miejscu\n\n"
              "1) - Powrot do menu")
        if num_rules == "1":
            self.set_position(0)

    def show_game_start(self, game_start_num):
        if game_start_num == "1":
            self.set_position(0)
            return
        elif game_start_num != "":
            self.engine.stats_add(game_start_num)
        if len(self.engine.highscores) == 0:
            self.engine.highscores.append(Stats(0, 0, ""))
        if self.current_position == 4:
            return
        print("Wylosowane slowo ma:", len(self.engine.word), "liter")
        print("Pozostalo:", self.engine.trials - len(self.engine.highscores) + 1, "prob\n")
        i = 0
        for x in range(len(self.engine.highscores)):
            if i != 0:
                print(self.engine.highscores[i])
            i += 1
        print("\n1) - Przerwij gre")

    def show_game_end(self):

        if self.engine.win:
            print("Brawo! Udalo ci sie zgadnac haslo!")
        else:
            print("Niestety skonczyly sie proby. Haslo to:", self.engine.word)
        print("1) - Zapisz wyniki\n"
              "2) - Wyjdz z gry")
        game_start_num = input()
        if game_start_num == "1":
            self.engine.highscore_to_file()
            return exit(1)
        if game_start_num == "2":
            return exit(1)
