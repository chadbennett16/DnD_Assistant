from random import randint
from tkinter import *
from Prof_Windows import *
from tkinter import messagebox

class Ability_Win(object):
    def __init__(self, master, player):
        self.root = master
        master.title("Character Creator")
        self.f2 = Frame(master)
        self.f2.pack()
        self.f2_top = Frame(self.f2)
        self.f2_top.pack()
        self.f2_bottom = Frame(self.f2)
        self.f2_bottom.pack()
        self.f3 = Frame(master)
        self.f3.pack()
        Label(self.f2_top, text="Here are your ability score rolls:").pack()
        self.ability_rolls = self.roll_abilities()
        Label(self.f2_top, text=str(self.ability_rolls)).pack()

        # From that generated array, enter where you want those scores to assign to

        Label(self.f2_top, text="Assign these values to your abilities below:").pack()
        Label(self.f2_bottom, text="Strength: ").pack()
        self.strength = Spinbox(self.f2_bottom, width=5, from_=1, to=max(self.ability_rolls))
        self.strength.pack()
        Label(self.f2_bottom, text="Dexterity: ").pack()
        self.dex = Spinbox(self.f2_bottom, width=5, from_=1, to=max(self.ability_rolls))
        self.dex.pack()
        Label(self.f2_bottom, text="Constitution: ").pack()
        self.con = Spinbox(self.f2_bottom, width=5, from_=1, to=max(self.ability_rolls))
        self.con.pack()
        Label(self.f2_bottom, text="Intelligence: ").pack()
        self.intel = Spinbox(self.f2_bottom, width=5, from_=1, to=max(self.ability_rolls))
        self.intel.pack()
        Label(self.f2_bottom, text="Wisdom: ").pack()
        self.wis = Spinbox(self.f2_bottom, width=5, from_=1, to=max(self.ability_rolls))
        self.wis.pack()
        Label(self.f2_bottom, text="Charisma: ").pack()
        self.cha = Spinbox(self.f2_bottom, width=5, from_=1, to=max(self.ability_rolls))
        self.cha.pack()

        self.submitButton = Button(self.f2_bottom, text="Submit", command=lambda: self.submit_scores(player))
        self.submitButton.pack()

    def submit_scores(self, player):
        player.ability_score["Str"] = int(self.strength.get())
        player.ability_score["Dex"] = int(self.dex.get())
        player.ability_score["Con"] = int(self.con.get())
        player.ability_score["Int"] = int(self.intel.get())
        player.ability_score["Wis"] = int(self.wis.get())
        player.ability_score["Cha"] = int(self.cha.get())

        #if sorted(self.ability_rolls) == sorted(list(player.ability_score.values())):
        self.f2.destroy()
        self.f3 = Prof_Windows(self.root, player)
        #else:
        #    messagebox.showinfo("Error", "Sorry, those values do not match your rolls")

    def roll_abilities(self):
        abilities = []
        for _ in range(6):
            rolls = []
            for _ in range(4):
                rolls.append(randint(1, 6))
            abilities.append(sum(sorted(rolls, reverse=True)[:3]))
        return abilities
