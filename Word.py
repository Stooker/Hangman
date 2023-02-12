import random


class Word:
    def __init__(self, f_path):
        self.f_path = f_path
        self.word = self.rand_word()
        self.placeholder = self.set_placeholder()
        self.bad_guesses = 0

    def rand_word(self):
        try:
            with open(self.f_path, encoding="utf-8") as file:
                word_list = [s.strip() for s in file.read().split(sep=',')]
            word = random.choice(word_list)
            return word
        except FileNotFoundError:
            print(f'Brak pliku o ścieżce {self.f_path}')

    def set_placeholder(self):
        placeholder = []
        for i in range(len(self.word)):
            placeholder.append('_')
        return placeholder

    def check_letter(self, letter):
        bad_guess = True
        for i in range(len(self.word)):
            if letter == self.word[i] or letter.lower() == self.word[i]:
                self.placeholder[i] = letter
                bad_guess = False
        if bad_guess:
            self.bad_guesses += 1
        return bad_guess

    def end_game(self):
        if '_' not in self.placeholder:
            return True

    def reload_word(self):
        self.word = self.rand_word()
        self.placeholder = self.set_placeholder()
        self.bad_guesses = 0

    def get_guesses(self):
        return self.bad_guesses

    def get_word(self):
        return self.word

    def get_placeholder(self):
        return self.placeholder



