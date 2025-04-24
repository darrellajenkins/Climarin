import random


class Monster:
    def __init__(self, name):
        """ """
        self.name = name
        self.mouth = "ROAR! ***"
        self.strike = "BOOM! ooo"
        self.speak = ""
        self.power = 3

    def move(self):
        p = random.choice(['A', 'B', 'C', 'M', 'X', 'Y', 'Z'])
        return f"{self.name} lands on '^' \033[1m{p}\033[0m '^'"

class Warrior:
    def __init__(self, name):
        """ """
        self.name = name
        self.mouth = "YELL! !!!"
        self.strike = "BAM! oooO"
        self.magic = "~~~~~~~~"
        self.speak = ""
        self.power = 2.5
        self.tool = "Sword"

    def move(self):
        p = random.choice(['A', 'B', 'C', 'M', 'X', 'Y', 'Z'])
        return f"{self.name} lands on '^' \033[1m{p}\033[0m '^'"

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
        self.traits = {'Name':self.name, 'Mouth':self.mouth, 'Strike':self.strike, 'Class': self.__class__.__name__,
                       'Cast':self.cast, 'Speak':self.speak, 'Power':self.power, 'Tool':self.tool}

    def move(self):
        p = random.choice(['A', 'B', 'C', 'M', 'X', 'Y', 'Z'])
        return f"{self.name} lands on '^' \033[1m{p}\033[0m '^'"

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
        p = random.choice(['A', 'B', 'C', 'M', 'X', 'Y', 'Z'])
        return f"{self.name} lands on '^' \033[1m{p}\033[0m '^'"



