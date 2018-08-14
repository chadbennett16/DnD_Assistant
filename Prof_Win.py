from tkinter import *
from random import randint

class Prof_Win(object):
    """description of class"""
    def __init__(self, master, player):
        
        # Do ability_score rolls here?
        # For each class, figure out the most beneficial stat dist
        # Ex. For Monk:
        # Highest go to Dex, next to Wisdom, Strength, Cons, Cha, and Int

        # Or make some kind of interface that displays the rolls and lets the user choose

        self.root = master
        master.title("Character Creator")

        Label(master, text="Select your Proficiencies below:").grid(row=0, sticky=W)

        if player.race == "Hill Dwarf":         #Need to add tool proficiency, maybe stonecunning and langauges
            player.ability_score["Con"] += 2
            player.ability_score["Wis"] += 1
            player.proficiencies.extend(("Battle Axe", "Hand Axe", "Light Hammer", "War Hammer"))
            player.hp_max += (1 * player.level)
            player.height = self.find_height([3, 8], [2, 4])
            player.weight = self.find_weight(115, [2, 4], [2, 6])
            player.speed = 25
            

        elif player.race == "Mountain Dwarf":
            player.ability_score["Con"] += 2
            player.ability_score["Str"] += 2
            player.proficiencies.extend(("Battle Axe", "Hand Axe", "Light Hammer", "War Hammer", "Light Armor", "Medium Armor"))
            player.height = self.find_height([4, 0], [2, 4])
            player.weight = self.find_weight(130, [2, 4], [2, 6])
            player.speed = 25

        self.submitButton = Button(master, text="Submit", command=lambda: self.submit_profs(player))
        self.submitButton.grid(row=1)

    def submit_profs(self, player):
        self.root.destroy()

    def dice_roll(self, roll):      #roll = [num dice, num sides]   num D sides
        sum = 0
        for _ in range(1, roll[0] + 1):
            sum += randint(1, roll[1])
        return sum

    def find_height(self, base, roll):      #base = [feet, inches]
        height = base
        height[1] += self.dice_roll(roll)

        while height[1] >= 12:
            height[0] += 1
            height[1] -= 12

        return height

    def find_weight(self, base, height_roll, roll):
        return base + (self.dice_roll(height_roll) * self.dice_roll(roll))
        