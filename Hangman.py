from Word import Word
from Window import Window
from TopPart import TopPart
from Slogan import Slogan
from BottomPart import BottomPart


class Hangman:
    def __init__(self, file):
        self.file = file
        self.w = Word(file)
        self.root = Window()
        self.topFrame = TopPart(self.root.window)
        self.slogan = Slogan(self.root.window, self.w.placeholder)
        self.bottomFrame = BottomPart(self.root.window, self.w, self.topFrame)
        self.root.start_method()
