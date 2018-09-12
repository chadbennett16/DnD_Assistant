from random import randint
from tkinter import *
from Ability_Win import Ability_Win

class Char_Win(object):
    
    def __init__(self, master, player):
        self.root = master
        master.title("Character Creator")
        #self.root.geometry("400x400")

        self.f1 = Frame(master)
        self.f1.pack()
        self.f2 = Frame(master)
        self.f2.pack()

        Label(self.f1, text="Please fill out the form below:").pack()

        Label(self.f1, text="Name:").pack()
        self.e1 = Entry(self.f1)
        self.e1.pack()

        Label(self.f1, text="Select Race:").pack()
        self.race_var = StringVar()
        self.race_var.set(player.races[0])
        raceMenu = OptionMenu(self.f1, self.race_var, *player.races)
        raceMenu.pack()

        Label(self.f1, text="Select Class:").pack()
        self.cls_var = StringVar()
        self.cls_var.set(player.classes[0])
        clsMenu = OptionMenu(self.f1, self.cls_var, *player.classes)
        clsMenu.pack()

        Label(self.f1, text="Select Background:").pack()
        self.back_var = StringVar()
        self.back_var.set(player.backgrounds[0])
        backMenu = OptionMenu(self.f1, self.back_var, *player.backgrounds)
        backMenu.pack()

        self.submitButton = Button(self.f1, text="Submit", command=lambda: self.submit_char(player))
        self.submitButton.pack()

    def submit_char(self, player):
        player.name = self.e1.get()
        player.race = self.race_var.get()
        player.cls = self.cls_var.get()
        player.background = self.back_var.get()
        self.f1.destroy()
        self.f2 = Ability_Win(self.root, player)
        #self.f2 = Prof_Win(self.root, player)
        #self.newWindow = Toplevel(self.root)
        #prof_win = Prof_Win(self.newWindow, player)
