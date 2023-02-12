import tkinter as tk
import tkinter.messagebox
from data.colors import Colors
from Slogan import Slogan


class BottomPart:

    alphabet = list("AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUWXYZŹŻ")

    def __init__(self, window, word, picture):
        self.frame = tk.Frame(master=window, bg=Colors.WHITE)
        self.w = word
        self.create_btn_alphabet()
        self.picture = picture
        self.create_restart()
        self.add_frame()

    def add_frame(self):
        self.frame.pack(side=tk.BOTTOM, expand=True)

    def create_button(self, char, index, row, column):

        btn = tk.Button(master=self.frame, name=index, text=char, width=10, height=4, bg=Colors.GRAY, activebackground=Colors.GRAY)
        btn.grid(row=row, column=column, sticky='e', padx=2, pady=2)
        btn.bind('<Button-1>', lambda eve: self.add_event(i=index))

    def create_btn_alphabet(self):

        for index, char in enumerate(BottomPart.alphabet):
            if index < 10:
                self.create_button(char, str(index), 0, index)
            elif index < 20:
                self.create_button(char, str(index), 1, (index-10))
            elif index < 30:
                self.create_button(char, str(index), 2, (index - 20))
            else:
                self.create_button(char, str(index), 3, (index-30))

    def create_restart(self):
        new_game = tk.Button(master=self.frame, name='new', text='Nowa gra', width=22, height=4, bg=Colors.BLACK, fg=Colors.WHITE)
        new_game.grid(row=3, column=8, columnspan=2)
        new_game.bind('<Button-1>', self.restart)

    def restart(self, event):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.reload_frames()

    def reload_frames(self):
        self.w.reload_word()
        self.frame.master.children.get('slogan').destroy()
        Slogan(self.frame.master, self.w.placeholder)
        self.create_btn_alphabet()
        self.create_restart()
        self.picture.reload()

    def add_event(self, i):
        if not self.w.check_letter(BottomPart.alphabet[int(i)]):
            self.frame.children.get(i).destroy()
            self.frame.master.children.get('slogan').destroy()
            Slogan(self.frame.master, self.w.placeholder)
        else:
            self.frame.children.get(i).destroy()
            self.picture.reload(self.w.get_guesses())

        if self.w.end_game():
            if tkinter.messagebox.askyesno(master=self.frame.master,
                                           message='Wygrałeś, czy chcesz zagrać ponownie?',
                                           icon='info'):
                for widget in self.frame.winfo_children():
                    widget.destroy()
                self.reload_frames()
            else:
                self.frame.master.destroy()
        if self.w.get_guesses() == 8:
            if tkinter.messagebox.askyesno(master=self.frame.master,
                                           message=f'Przegrałeś, słowem było {self.w.get_word().upper()} czy chcesz zagrać ponownie?',
                                           icon='error'):
                for widget in self.frame.winfo_children():
                    widget.destroy()
                self.reload_frames()
            else:
                self.frame.master.destroy()






