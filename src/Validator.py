class Validator(object):

    def word_check(self, word, word_len):
        if not word.isalpha():
            return False
        if len(word) > word_len:
            return False
        if len(word) < word_len:
            return False
        else:
            list = []
            temp = word.lower()
            for i in temp:
                if i in list:
                    return False
                list.append(i)
        return True

    def bulls_or_cows(self, word_random, word_input):
        bulls = 0
        cows = 0
        i = 0
        if self.word_check(word_input, len(word_random)):
            word_input = word_input.lower()
            for letter in word_input:
                if letter == word_random[i]:
                    bulls += 1
                elif letter in word_random:
                    cows += 1
                i += 1
            return bulls, cows
        return 0, 0

    def word_add_dictionary(self, word_add):
        if not word_add.isalpha():
            return False
        if len(word_add) < 3:
            return False
        else:
            list = []
            temp = word_add.lower()
            for i in temp:
                if i in list:
                    return False
                list.append(i)
        return True
