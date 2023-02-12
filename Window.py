import tkinter as tk
from data.colors import Colors


MAIN_WINDOW_WIDTH = 960
MAIN_WINDOW_HEIGHT = 880


class Window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Hangman")
        self.set_size()
        self.window.configure(background=Colors.WHITE)

    def start_method(self):
        self.window.mainloop()

    def set_size(self):
        w, h = MAIN_WINDOW_WIDTH, MAIN_WINDOW_HEIGHT
        self.window.geometry(f'{w}x{h}')

