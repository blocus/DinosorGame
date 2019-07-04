from tkinter import *

class Cactus:
    def __init__(self):
        self.x = 800
        self.y = 225
        self.img = PhotoImage(file = "./cactus.gif")

    def move(self):
        self.x -= 10
