from characters import Monster, Warrior, Sorcerer, Sage
import special_abilities as spc_abs


field = ['A', 'B', 'C', 'M', 'X', 'Y', 'Z']

def player_1():
    p_1 = input("\033[1mPlayer 1\033[0m, please select your character: \n[W]arrior\n[M]onster\n[S]orcerer\nSa[g]e\n\t")

    if p_1.lower() == 'w':
        name = input("Warrior, please enter your name: ")
        charac = Warrior(name)
    elif p_1.lower() == 'm':
        name = input("Monster, please enter your name: ")
        charac = Monster(name)
    elif p_1.lower() == 's':
        name = input("Sorcerer, please enter your name: ")
        charac = Sorcerer(name)
    elif p_1.lower() == 'g':
        name = input("Sage, please enter your name: ")
        charac = Sage(name)
    else:
        print("Invalid input")
        player_1()
    return name, charac

def player_2():
    p_2 = input("\033[1mPlayer 2\033[0m, please select your character: \n[W]arrior\n[M]onster\n[S]orcerer\nSa[g]e")

    if p_2.lower() == 'w':
        name = input("Warrior, please enter your name: ")
        charac = Warrior(name)
    elif p_2.lower() == 'm':
        name = input("Monster, please enter your name: ")
        charac = Monster(name)
    elif p_2.lower() == 's':
        name = input("Sorcerer, please enter your name: ")
        charac = Sorcerer(name)
    elif p_2.lower() == 'g':
        name = input("Sage, please enter your name: ")
        charac = Sage(name)
    else:
        print("Invalid input")
        player_2()
    return name, charac

player_1 = player_1()
p1_name = player_1[0]
p1_charac = player_1[1]

player_2 = player_2()
p2_name = player_2[0]
p2_charac = player_2[1]


opponents = [(p1_name, p1_charac), (p2_name, p2_charac)]

p = True
while p:
    play = input("[P]lay, [S]top, or [Q]uit ")
    if play.lower() == 'q':
        p = False
        print("Thanks for playing!")
        break
    elif play.lower() == 'p':
        for name, charac in opponents:
            input(f"{name} begins...press enter")
            print(charac.move())
    elif play.lower() == 's':
        print("Score is tied 1 to 1")  # TODO: create function to calculate score.
        break


# TODO: create function to save score.
# TODO: modify code to read saved game and continue from there.