import random
# This code keeps dice shapes as a list and prints according to the incoming number
dice = [
    " ------- ",
    "|       |",
    "|   o   |",
    "|       |",
    " ------- ",
]
# Incoming number
number = random.randint(1,6)
# Dice shapes for each number
while True:
    if number == 1:
        dice = dice
    elif number == 2:
        dice = [
        " ------- ",
        "|o      |",
        "|       |",
        "|      o|",
        " ------- ",
    ]
    elif number == 3:
        dice = [
        " ------- ",
        "|      o|",
        "|   o   |",
        "|o      |",
        " ------- ",
    ]
    elif number == 4:
        dice = [
        " ------- ",
        "|o     o|",
        "|       |",
        "|o     o|",
        " ------- ",
    ]
    elif number == 5:
        dice = [
        " ------- ",
        "|o     o|",
        "|   o   |",
        "|o     o|",
        " ------- ",
    ]
    elif number == 6:
        dice = [
        " ------- ",
        "|o     o|",
        "|o     o|",
        "|o     o|",
        " ------- ",
    ]
    # printing dice with for loop
    for line in dice:
        print(line)
    # rolling again or not with if else
    again = input("Do you want to roll again ? (Y/N) : ")
    if again == "n":
        break
    else:
        number = random.randint(1,6)
