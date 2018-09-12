from tkinter import *
from tkinter import messagebox
from random import randint
from References import *

# This file contains all variations of windows for selecting proficiencies including:
# Race proficiencies
# Class proficiencies
# Background proficiencies

def add_prof(value, index, player):              # Make sure before func is called a '' is appended to profs
    if (value.get() not in player.profs):
        player.profs.pop(index)
        player.profs.insert(index, value.get())
        print("Added " + value.get() + " at index " + str(index))

    else:
        messagebox.showinfo("Error", "You are already proficient in " + value.get())


class Prof_Windows(object):

    # Things I need to add based on race, class, background that are based on player choice
    # Tool profs
    # Languages
    # Spells/Cantrips
    # Ancestry
    # Ability Score increments
    # Skills

    def __init__(self, master, player):
        self.root = master
        master.title("Character Creator")
        Label(master, text="Select your proficiencies below:").pack()
        player.profs.append("Common")   # all races speak Common
        player.prof_bonus = 2               # all characters start with +2 prof bonus
        self.race_f = Frame(master)
        self.cls_f = Frame(master)
        self.back_f = Frame(master)
        self.race_f.pack()
        self.cls_f.pack()
        self.back_f.pack()
        
        self.race_f = Race_Frame(self.race_f, player)
        self.cls_f = Cls_Frame(self.cls_f, player)
        self.back_f = Back_Frame(self.back_f, player)

        self.submitButton = Button(master, text="Submit", command=lambda: self.submit_profs(player))
        self.submitButton.pack()

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


class Race_Frame(Prof_Windows):

    def __init__(self, master, player):

        #Label(master, text="As a " + player.race + ", you are proficient in the following:").pack()

        if "Dwarf" in player.race:

            player.ability_score["Con"] += 2
            player.profs.append("Dwarvish")
            player.profs.extend(["Battleaxe", "Handaxe", "Light Hammer", "Warhammer"])
            player.traits.extend(["Darkvision", "Dwarven Resilience", "Stonecunning"])
            player.speed = 25

            Tool_List(master, player, ["Smith's Tools", "Brewer's Tools", "Mason's Tools"])

            if player.race == "Hill Dwarf":
                player.ability_score["Wis"] += 1
                player.max_hp += 1
                player.height = self.find_height([3, 8], [2, 4])
                player.weight = self.find_weight(115, [2, 4], [2, 6])

            elif player.race == "Mountain Dwarf":
                player.ability_score["Str"] += 2
                player.height = self.find_height([4, 0], [2, 4])
                player.weight = self.find_weight(130, [2, 4], [2, 6])
                player.profs.extend(["Light Armor", "Medium Armor"])

        elif player.race == "Half-Elf":
            player.ability_score["Cha"] += 2

            player.speed = 30
            player.height = self.find_height([4, 9], [2, 8])
            player.weight = self.find_weight(110, [2, 8], [2, 4])
            player.traits.extend(["Darkvision", "Fey Ancestry"])
            # Choose two skills to be proficient in
            Skill_List(master, player)
            Skill_List(master, player)
            player.profs.append("Elvish")
            # Choose one other language
            Language_List(master, player, std_languages)

            # Choose two ability scores to increase by 1
            Ability_Increase(master, player)    # Need to fix, just adds the last clicked option
            Ability_Increase(master, player)

        elif "Elf" in player.race:
            player.ability_score["Dex"] += 2
            player.speed = 30
            player.traits.extend(["Fey Ancestry", "Trance"])
            player.profs.append("Elvish")
            player.profs.append("Perception")
            player.skills["Perception"] += player.prof_bonus

            if player.race == "Dark Elf":
                player.ability_score["Cha"] += 1
                player.traits.extend(["Superior Darkvision", "Sunlight Sensitivity"])
                player.profs.extend(["Rapier", "Shortsword", "Hand Crossbow"])
                player.cantrips.append("Dancing Lights")
                player.height = self.find_height([4, 5], [2, 6])
                player.weight = self.find_weight(75, [2, 6], [1, 6])

            elif player.race == "High Elf":
                player.ability_score["Int"] += 1
                player.profs.extend(["Longsword", "Shortsword", "Shortbow", "Longbow"])
                player.traits.append("Darkvision")

                #Pick one extra language
                Language_List(master, player, std_languages)
                Language_List(master, player, std_languages)
                #Pick one cantrip from wizard spell list
                Cantrip_List(master, player, wizard_cantrips)

                player.height = self.find_height([4, 6], [2, 10])
                player.weight = self.find_weight(90, [2, 10], [1, 4])


            elif player.race == "Wood Elf":
                player.ability_score["Wis"] += 1
                player.profs.extend(["Longsword", "Shortsword", "Shortbow", "Longbow"])
                player.speed = 35
                player.traits.extend(["Darkvision", "Mask of the Wild"])
                player.height = self.find_height([4, 6], [2, 10])
                player.weight = self.find_weight(100, [2, 10], [1, 4])

        elif "Halfling" in player.race:
            player.ability_score["Dex"] += 2
            player.speed = 25
            player.traits.extend(["Lucky", "Brave", "Halfling Nimbleness"])
            player.profs.append("Halfling")
            player.height = self.find_height([2, 7], [2, 4])
            player.weight = self.find_weight(35, [2, 4], [1, 1])

            if player.race == "Lightfoot Halfling":
                player.ability_score["Wis"] += 1
                player.traits.append("Naturally Stealthy")

            elif player.race == "Stout Halfling":
                player.abililty_score["Con"] += 1
                player.traits.append("Stout Resilience")

        elif player.race == "Human":
            for score in player.ability_score:
                player.ability_score[score] += 1
            player.speed = 30
            player.height = self.find_height([4, 8], [2, 10])
            player.weight = self.find_weight(110, [2, 10], [2, 4])
            # choose_language(player.languages)
            Language_List(master, player, std_languages)

        elif player.race == "Dragonborn":
            player.ability_score["Str"] += 2
            player.ability_score["Cha"] += 1
            player.speed = 30
            player.profs.append("Draconic")
            player.height = self.find_height([6, 0], [2, 8])
            player.weight = self.find_weight(220, [2, 8], [2, 4])
            
            # Have player choose their draconic ancestry
            Draconic_Ancestry(master, player)

        elif "Gnome" in player.race:
            player.ability_score["Int"] += 2
            player.speed = 25
            player.height = self.find_height([2, 11], [2, 4])
            player.weight = self.find_weight(35, [2, 4], [1, 1])
            player.traits.extend(["Darkvision", "Gnome Cunning"])
            player.profs.append("Tinker's Tools")
            player.profs.append("Gnomish")
            if player.race == "Forest Gnome":
                player.ability_score["Dex"] += 1
                player.cantrips.append("Minor Illusion")
                player.traits.append("Speak with Small Beasts")
            elif player.race == "Rock Gnome":
                player.ability_score["Con"] += 1
                player.traits.append("Artificer's Lore")

        elif player.race == "Half-Orc":
            player.ability_score["Str"] += 2
            player.ability_score["Con"] += 1
            player.speed = 30
            player.height = self.find_height([4, 10], [2, 10])
            player.weight = self.find_weight(140, [2, 10], [2, 6])
            player.traits.extend(["Darkvision", "Relentless Endurance", "Savage Attacks"])
            player.profs.append("Orc")
            player.profs.append("Intimidation") # used for error checking
            #player.skills["Intimidation"] += player.prof_bonus

        elif player.race == "Tiefling":
            player.ability_score["Int"] += 1
            player.ability_score["Cha"] += 2
            player.speed = 30
            player.traits.extend(["Darkvision", "Hellish Resistance"])
            player.profs.append("Infernal")
            player.height = self.find_height([4, 8], [2, 10])
            player.weight = self.find_weight(110, [2, 10], [2, 4])
            player.cantrips.append("Thaumaturgy")

class Cls_Frame(Prof_Windows):

    def __init__(self, master, player):
        Label(master, text="As a " + player.cls + ", you are proficient in the following:").pack()

class Back_Frame(Prof_Windows):

    def __init__(self, master, player):
        if player.background[0] in "AEIOU":
            Label(master, text="As an " + player.background + ", you are proficient in the following:").pack()

        else:
            Label(master, text="As a " + player.background + ", you are proficient in the following:").pack()

class Language_List():
    def __init__(self, master, player, languages):
        f = Frame(master)
        f.pack()
        Label(f, text="Select a language:").pack()
        self.lang = StringVar()
        player.profs.append('')
        self.blank = len(player.profs) - 1
        langMenu = OptionMenu(f, self.lang, *languages, command=lambda x: add_prof(self.lang, self.blank, player))
        langMenu.pack()

class Tool_List():
    def __init__(self, master, player, tools):
        f = Frame(master)
        f.pack()
        Label(f, text="Select your tool proficiency").pack()
        self.tool = StringVar()
        player.profs.append('')
        blank = len(player.profs) - 1
        toolMenu = OptionMenu(f, self.tool, *tools, command=lambda x: add_prof(self.tool, blank, player))
        toolMenu.pack()

class Skill_List():
    def __init__(self, master, player):
        f = Frame(master)
        f.pack()
        Label(f, text="Select a skill:").pack()
        self.skill = StringVar()
        player.profs.append('')
        blank = len(player.profs) - 1
        skillMenu = OptionMenu(f, self.skill, *skills_ref, command=lambda x: add_prof(self.skill, blank, player))
        skillMenu.pack()

class Cantrip_List():
    def __init__(self, master, player, cantrips):
        f = Frame(master)
        f.pack()
        Label(f, text="Select a cantrip:").pack()
        self.can = StringVar()
        player.profs.append('')
        blank = len(player.profs) - 1
        canMenu = OptionMenu(f, self.can, *cantrips, command=lambda x: add_prof(self.can, blank, player))
        canMenu.pack()

class Spell_List():
    def __init__(self, master, player, spells):
        f = Frame(master)
        f.pack()
        Label(f, text="Select a spell").pack()
        self.spell = StringVar()
        player.profs.append('')
        blank = len(player.profs) - 1
        spellMenu = OptionMenu(f, self.spell, *spells, command=lambda x: add_prof(self.spell, blank, player))
        spellMenu.pack()

class Ability_Increase():               # Cannot do 2 in a row. Original_values are the same for both
    def __init__(self, master, player):
        f = Frame(master)
        f.pack()
        self.ability_list = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
        self.original_values = list(player.ability_score.values())
        print(self.original_values)
        Label(f, text="Select an ability score to increase").pack()
        self.var = IntVar()
        for item in range(6):
            Radiobutton(f, text=self.ability_list[item], variable=self.var, value=item, command=lambda: self.sel(player)).pack(side=LEFT)

    def sel(self, player):
        for i, key in enumerate(player.ability_score):
            if i == self.var.get():
                player.ability_score[key] += 1
            else:
                player.ability_score[key] = self.original_values[i]

class Draconic_Ancestry():
    def __init__(self, master, player):
        f = Frame(master)
        f.pack()
        Label(f, text="Select your Draconic Ancestry").pack()
        self.anc = StringVar()
        player.traits.append('')
        blank = len(player.traits) - 1
        ancMenu = OptionMenu(f, self.anc, *[item[0] for item in draconic_ancestry], command=lambda x: self.add_anc(self.anc, blank, player))
        ancMenu.pack()

    def add_anc(self, value, index, player):
        player.traits.pop(index)
        resist_loc = [item[0] for item in draconic_ancestry].index(value.get())
        player.traits.insert(index, draconic_ancestry[resist_loc][1] + " Resistance")

#class Choose_Equipment():
