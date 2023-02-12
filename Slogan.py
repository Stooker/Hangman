import tkinter as tk
from data.colors import Colors


class Slogan():

    def __init__(self, window, word):
        self.frame = tk.Frame(master=window, name='slogan')
        self.window = window
        self.render_word(word)
        self.add_frame()

    def add_frame(self):
        self.frame.pack(fill=tk.X, expand=False, side=tk.TOP)

    def render_word(self, word):
        word_label = tk.Label(master=self.frame, text=' '.join(word).upper(), font=('Arial', 30))
        word_label.pack()

    def reload_slogan(self, word):
        self.frame.destroy()
        self.frame = tk.Frame(master=self.window, name='slogan')
        self.render_word(word)
        self.add_frame()