import tkinter as tk
from data.colors import Colors
from PIL import Image, ImageTk


class TopPart:
    def __init__(self, window):
        self.frame = tk.Frame(master=window, bg=Colors.WHITE)
        self.reload(0)
        self.add_frame()

    def add_frame(self):
        self.frame.pack(fill=tk.X)

    def render_picture(self, picture):
        load = Image.open(picture)
        render = ImageTk.PhotoImage(load.resize((300, 300)))
        lbl_img = tk.Label(self.frame, name='picture', image=render, borderwidth=0)
        lbl_img.image = render
        lbl_img.pack()

    def reload(self, number=0):
        try:
            self.frame.children.get('picture').destroy()
        except:
            pass
        finally:
            pic = f'pictures/{number}.png'
            self.render_picture(pic)

