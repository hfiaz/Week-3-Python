# import array and random libraries
import array
import random

dice_array = array.array("i", [1, 2, 3, 4, 5, 6])

ko = False
while not ko:
    player1_ko = int(input("Player 1 choose a KO number (2 - 12): "))
    input("Press enter to roll dice 1")
    first_dice_roll = random.choice(dice_array)
    print("You rolled a: ", first_dice_roll)
    input("Press enter to roll dice 2")
    second_dice_roll = random.choice(dice_array)
    print("You rolled a: ", second_dice_roll)

    if (first_dice_roll + second_dice_roll) == player1_ko:
        print("You got knocked out")
        ko = True
    else:
        print("You survived this round")