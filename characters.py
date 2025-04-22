import random
from json import tool


class Monster:
    def __init__(self, name):
        """ """
        self.name = name
        self.mouth = "ROAR! ***"
        self.strike = "BOOM! ooo"
        self.speak = ""
        self.power = 3

    def move(self):
        return random.choice(['A', 'B', 'C', 'D', 'X', 'Y', 'Z'])

class Warrior:
    def __init__(self, name):
        """ """
        self.name = name
        self.mouth = "SHOUT! !!!"
        self.strike = "BAM! oooO"
        self.speak = ""
        self.power = 2.5
        self.tool = "Sword"

    def move(self):
        return random.choice(['A', 'B', 'C', 'D', 'X', 'Y', 'Z'])

class Sorcerer:
    def __init__(self, name):
        """ """
        self.name = name
        self.mouth = "Hmmm ---"
        self.strike = "Swoooo! ~~~"
        self.cast = "Marai!"
        self.speak = ""
        self.power = 3
        self.tool = ["Staff", "Wand"]
        self.traits = {'Name':self.name, 'Mouth':self.mouth, 'Strike':self.strike, 'Cast':self.cast, 'Speak':self.speak, 'Power':self.power, 'Tool':self.tool}

    def move(self):
        return random.choice(['A', 'B', 'C', 'D', 'X', 'Y', 'Z'])

class Sage:
    def __init__(self, name):
        """ """
        self.name = name
        self.mouth = ["Speak....", "Not one more step"]
        self.strike = "Ahhh...."
        self.speak = ""
        self.power = 2.5
        self.tool = "Book"

    def move(self):
        return random.choice(['A', 'B', 'C', 'D', 'X', 'Y', 'Z'])

class Enhancers:
    def __init__(self):
        """ """
        self.demi_god = 2
        self.god = 4
