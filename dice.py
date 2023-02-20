import random

dice_1 = random.randint(1,6)
dice_2 = random.randint(1,6)
n=0
if dice_1 + dice_2 == 7 or dice_1 + dice_2 == 11:
    print(f"{dice_1} + {dice_2} = {dice_1 + dice_2}")
    print("You won")
elif dice_1 + dice_2 == 2 or dice_1 + dice_2 == 3 or dice_1 + dice_2 == 12:
    print(f"{dice_1} + {dice_2} = {dice_1 + dice_2}")
    print("You lose")
elif (dice_1 + dice_2 >= 4 and dice_1 + dice_2 <= 6) or (dice_1 + dice_2 >= 8 and dice_1 + dice_2 <= 10):
    n = dice_1 + dice_2
    print(f"The sum of dice is {n}")
    print(f"Now your goal number is {n}")
    while (dice_1 + dice_2 != 7):
        dice_1 = random.randint(1,6)
        dice_2 = random.randint(1,6)
        if (dice_1 + dice_2 == n):
            print(f"{dice_1} + {dice_2} = {dice_1 + dice_2}")
            print("You won")
            break
        elif (dice_1 + dice_2 == 7):
            print(f"{dice_1} + {dice_2} = {dice_1 + dice_2}")
            print("You lose")
            break
