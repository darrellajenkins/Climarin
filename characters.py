import random
import time


class Monster:
    def __init__(self, name):
        """ Monster class. """
        self.name = name
        self.mouth = "ROAR! ***"
        self.strike_sound = "BOOM! ooo"
        self.speak = ""
        self.power = 3
        self.tool = "Claw"

    def move(self):
        p = random.choice(['A', 'B', 'C', 'M', 'X', 'Y', 'Z'])
        return f"{self.name} lands on '^' \033[1m{p}\033[0m '^'", p

    def strike(self):
        return f"{self.name} strikes with Power {self.power}!"

class Warrior:
    def __init__(self, name):
        """ Warrior class. """
        self.name = name
        self.mouth = "YELL! !!!"
        self.strike_sound = "BAM! oooO"
        self.magic = "~~~~~~~~"
        self.speak = ""
        self.power = 2.5
        self.tool = "Sword"

    def move(self):
        p = random.choice(['A', 'B', 'C', 'M', 'X', 'Y', 'Z'])
        return f"{self.name} lands on '^' \033[1m{p}\033[0m '^'", p

    def strike(self):
        return f"{self.name} strikes with Power {self.power}!"

class Sorcerer:
    def __init__(self, name):
        """ Sorcerer class. """
        self.name = name
        self.mouth = "Hmmm ---"
        self.strike_sound = "Swoooo! ~~~"
        self.cast = "Marai!"
        self.speak = ""
        self.power = 3
        self.tool = ["Staff", "Wand"]
        self.traits = {'Name':self.name, 'Mouth':self.mouth, 'strike_sound':self.strike_sound, 'Class': self.__class__.__name__,
                       'Cast':self.cast, 'Speak':self.speak, 'Power':self.power, 'Tool':self.tool}

    def move(self):
        p = random.choice(['A', 'B', 'C', 'M', 'X', 'Y', 'Z'])
        return f"{self.name} lands on '^' \033[1m{p}\033[0m '^'", p

    def magic(self):
        for i in range(3):
            print(f"\033[31m{chr(8608)}\033[39m", end=" ")
            time.sleep(0.3)
        print()
        for _ in range(5):
            for s in [chr(164), chr(167), chr(931), chr(1046), chr(8982)]:
                print(f"\033[34mMagic: {s}\033[39m", end='\r')
                time.sleep(0.1)

    def strike(self):
        return f"{self.name} casts {self.cast} at Power {self.power}!"

class Sage:
    def __init__(self, name):
        """ Sage class."""
        self.name = name
        self.mouth = ["Speak....", "Not one more step"]
        self.strike_sound = "Ahhh...."
        self.speak = ""
        self.power = 2.5
        self.tool = "Book"

    def move(self):
        p = random.choice(['A', 'B', 'C', 'M', 'X', 'Y', 'Z'])
        return f"{self.name} lands on '^' \033[1m{p}\033[0m '^'", p

    def strike(self):
        return f"{self.name} strikes with Power {self.power}!"
