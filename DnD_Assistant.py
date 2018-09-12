"""
Chad Bell
08/04/2018
DnD Assistant

Goals:
Be able to roll any specified die
Keep track of PC information including:
    > Stats
    > Skills
    > Inventory
Save/Pull NPC data
Setup Encounters
Save progress
"""

from Player import Player
from Char_Win import Char_Win
from tkinter import *

players = []

c = Player()
root = Tk()
Char_Win(root, c)
root.mainloop()

print(c.name)
print(c.race)
print(c.cls)
print(c.background)
print(c.height)
print(c.weight)
print(c.ability_score)
print(c.profs)
print(c.traits)