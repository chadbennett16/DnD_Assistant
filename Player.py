from xlrd import * # Need to install xlrd
from tkinter import *

class Player(object):
    """Represents a player's character sheet"""
    #file_name = 'path to file'
    classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk",
               "Paladin", "Ranger", "Rouge", "Sorcerer", "Warlock", "Wizard"]
    
    races = ["Dwarf", "Elf", "Halfling", "Human", "Dragonborn", "Gnome",
             "Half-Elf", "Half-Orc", "Tiefling"]
    def __init__(self, name):
        self.name = "name"
        self.level = 1
        self.cls = ''
        self.race = ''
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        self.armor_cl = 0
        self.initiative = 0
        self.speed = 0
        self.max_hp = 0
        self.skills = []
        self.inventory = []
        self.xp = 0
        
     def add_inv(self, item):
        self.inventory.append(item)
        
     def add_skill(self, skill):
        self.skills.append(skill)
        
     def select_cls(self, name):
        cls_win = Tk()
        cls_win.title("Select a class below")
        cls_win.label("Hello %s. Please choose your class" % name).grid(row=0, column=0, sticky=W)
        self.cls = StrVar()
        for item in classes:
            Radiobutton(cls_win, text=item, variable=self.cls, value=item).pack(side=LEFT)
        # Might need a submit button
        cls_win.mainloop() # runs select a class menu
        
        
     def select_race(self, name):
        race_win = Tk()
        race_win.title("Select a race below")
        race_win.label("Hello %s. Please choose your race" % name).grid(row=0, column=0, sticky=W)
        self.race = StrVar()
        for item in races:
            Radiobutton(race_win, text=item, variable=self.race, value=item).pack(side=LEFT)
        race_win.mainloop() # runs select a class menu
        
     def create_char(self, name):
        self.name = name
        select_cls(name)
        select_race(name)
        # Do rolls for character attributes and add race/class bonuses
        
