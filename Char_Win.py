from random import randint
from tkinter import *
from Prof_Win import Prof_Win

class Char_Win(object):
    
    def __init__(self, master, player):
        self.root = master
        master.title("Character Creator")
        #self.root.geometry("400x400")

        self.f1 = Frame(master)
        self.f1.grid(row=0)
        self.f2 = Frame(master)
        self.f2.grid(row=0)

        Label(self.f1, text="Please fill out the form below:").grid(row=0, sticky=W)

        Label(self.f1, text="Name:").grid(row=1, sticky=W)
        self.e1 = Entry(self.f1)
        self.e1.grid(row=1, column=1)

        Label(self.f1, text="Starting Level:").grid(row=2, sticky=W)
        self.e2 = Entry(self.f1)
        self.e2.grid(row=2, column=1)

        Label(self.f1, text="Select Race:").grid(row=3, sticky=W)
        self.race_var = StringVar()
        self.race_var.set(player.races[0])
        raceMenu = OptionMenu(self.f1, self.race_var, *player.races)
        raceMenu.grid(row=3, column=1)

        Label(self.f1, text="Select Class:").grid(row=4, sticky=W)
        self.cls_var = StringVar()
        self.cls_var.set(player.classes[0])
        clsMenu = OptionMenu(self.f1, self.cls_var, *player.classes)
        clsMenu.grid(row=4, column=1)

        Label(self.f1, text="Select Background:").grid(row=5, sticky=W)
        self.back_var = StringVar()
        self.back_var.set(player.backgrounds[0])
        backMenu = OptionMenu(self.f1, self.back_var, *player.backgrounds)
        backMenu.grid(row=5, column=1)

        self.submitButton = Button(self.f1, text="Submit", command=lambda: self.submit_char(player))
        self.submitButton.grid(row=10, column=0)

    def submit_char(self, player):
        player.name = self.e1.get()
        player.level = self.e2.get()
        player.race = self.race_var.get()
        player.cls = self.cls_var.get()
        player.background = self.back_var.get()
        self.f1.destroy()
        self.f2 = Prof_Win(self.root, player)
        #self.newWindow = Toplevel(self.root)
        #prof_win = Prof_Win(self.newWindow, player)
