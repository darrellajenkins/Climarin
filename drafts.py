from characters import Monster, Warrior, Sorcerer, Sage
import special_abilities as spc_abs


if __name__ == '__main__':
    malda = Sorcerer("Malda")
    for title, trait in malda.traits.items():
        if trait:
            print(f"{title}:  {trait}")

    move_1 = input("\n\tWould you like to move? (Y or N) ")
    if move_1.lower() == "y":
        print(f"\n\t{malda.move()}")

    field = ['A', 'B', 'C', 'M', 'X', 'Y', 'Z']

