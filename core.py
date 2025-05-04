from characters import Monster, Warrior, Sorcerer, Sage
import special_abilities as spc_abs
import time


def player_1():
    p_1 = input("\033[1mPlayer 1\033[0m, please select your character: \n[W]arrior\n[M]onster\n[S]orcerer\nSa[g]e\n")

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
    p_2 = input("\033[1mPlayer 2\033[0m, please select your character: \n[W]arrior\n[M]onster\n[S]orcerer\nSa[g]e\n")

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

def next_to(first, second):
    """Determine if the first and second players landed next to each other"""
    field = ['A', 'B', 'C', 'M', 'X', 'Y', 'Z']
    return field.index(first) == field.index(second) - 1 or field.index(first) == field.index(second) + 1

player_1 = player_1()
p1_name = player_1[0]
p1_charac = player_1[1]
p1_score = 0

player_2 = player_2()
p2_name = player_2[0]
p2_charac = player_2[1]
p2_score = 0

p = True
while p:
    play = input("[P]lay, [S]top, or [Q]uit ")
    if play.lower() == 'q':
        p = False
        print("Thanks for playing!")
        break
    elif play.lower() == 'p':
        input(f"{p1_name} begins...press enter")
        p1_move = p1_charac.move()
        print(p1_show_move := p1_move[0])
        p1_lands = p1_move[1]
        if isinstance(p1_charac, Sorcerer):
            print(p1_charac.strike())
            p1_charac.magic()
        else:
            print(p1_charac.strike())

        input(f"\n{p2_name} begins...press enter")
        p2_move = p2_charac.move()
        print(p2_show_move := p2_move[0])
        p2_lands = p2_move[1]
        if isinstance(p2_charac, Sorcerer):
            print(p2_charac.strike())
            p2_charac.magic()
        else:
            print(p2_charac.strike())
        if next_to(p1_lands, p2_lands):
            print("Both players landed next to each other.")
            if p1_charac.power > p2_charac.power:  # Make this a separate function later. One will always be larger than the other unless you write in option
                # to use the enhancers.
                p1_score += p1_charac.power - p2_charac.power
            elif p1_charac.power < p2_charac.power:
                p2_score += p2_charac.power - p1_charac.power
        elif p1_lands == p2_lands:
            print("Players landed in the same region. A special battle begins...")
            pass
        else:
            print("Players did not land next to each other.")

    elif play.lower() == 's':
        print(f"Score:  Player 1 = {p1_score} vs Player 2 = {p2_score}")
        break

# TODO: create function to save score.
# TODO: modify code to read saved game and continue from there.
