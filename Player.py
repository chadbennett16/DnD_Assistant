#from xlrd import * # Need to install xlrd

class Player:
    """Represents a player's character sheet"""
    #file_name = 'path to file'
    classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk",
               "Paladin", "Ranger", "Rouge", "Sorcerer", "Warlock", "Wizard"]
    
    races = ["Hill Dwarf", "Mountain Dwarf", "High Elf", "Wood Elf", "Dark Elf", 
             "Lightfoot Halfling", "Stout Halfling", "Human", "Dragonborn", "Forest Gnome", 
             "Rock Gnome", "Half-Elf", "Half-Orc", "Tiefling"]

    backgrounds = ["Acolyte", "Charlatan", "Criminal", "Entertainer", "Folk Hero",
                   "Guild Artisan", "Hermit", "Noble", "Outlander", "Sage", "Sailor",
                   "Soldier", "Urchin"]

    def __init__(self):
        self.name = ''
        self.cls = ''
        self.race = ''
        self.background = ''
        self.ability_score = {"Str": 0, "Dex": 0, "Con": 0,
                              "Int": 0, "Wis": 0, "Cha": 0}
        self.modifiers = {"Str": 0, "Dex": 0, "Con": 0,
                          "Int": 0, "Wis": 0, "Cha": 0}
        self.saving_throws = {"Str": 0, "Dex": 0, "Con": 0,
                              "Int": 0, "Wis": 0, "Cha": 0}
        self.ac = 0
        self.initiative = 0
        self.speed = 0
        self.hit_dice = [0, 0] # num D sides
        self.max_hp = 0
        self.skills = {"Acrobatics": 0, "Animal Herding": 0, "Arcana": 0, "Athletics": 0,
                       "Deception": 0, "History": 0, "Insight": 0, "Intimidation": 0,
                       "Investigation": 0, "Medicine": 0, "Nature": 0, "Perception": 0,
                       "Performance": 0, "Persuasion": 0, "Religion": 0, "Sleight of Hand": 0,
                       "Stealth": 0, "Survival": 0}
        self.inventory = []
        self.weapons = []
        self.armor = []
        self.xp = 0
        self.carry = 0
        self.pass_perc = 0
        self.death_saves = [0, 0]  #(Success, Failures) -> counts up to 3 for both
        self.profs = []
        self.traits = []
        self.height = [0, 0]    #(Feet, Inches)
        self.weight = 0         # in lbs
        self.prof_bonus = 0
        self.cantrips = []
        self.spell_slots = 0
        self.avail_spells = []
        self.equipped_spells = []