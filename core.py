from characters import Monster, Warrior, Sorcerer, Sage, Enhancers


malda = Sorcerer("Malda")

for title, trait in malda.traits.items():
    if trait:
        print(f"{title}:  {trait}")

move_1 = input("\n\tWould you like to move? (Y or N) ")
if move_1.lower() == "y":
    print(f"\n\tYou have landed on {malda.move()}")

# TODO: Test remaining classes
