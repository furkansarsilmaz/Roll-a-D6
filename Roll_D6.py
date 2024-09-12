import random

# Initial dice representation for number 1
dice = [
    " ------- ",
    "|       |",
    "|   o   |",
    "|       |",
    " ------- ",
]

# Generate a random number between 1 and 6 to simulate the dice roll
number = random.randint(1, 6)

# Loop flag to control whether the dice will be rolled again
loop = True

# Start the dice rolling loop
while loop == True:
    # Based on the rolled number, update the dice representation
    if number == 1:
        # No need to update the dice, as it's already set to represent 1
        dice = dice
    elif number == 2:
        # Update the dice representation for number 2
        dice = [
            " ------- ",
            "|o      |",
            "|       |",
            "|      o|",
            " ------- ",
        ]
    elif number == 3:
        # Update the dice representation for number 3
        dice = [
            " ------- ",
            "|      o|",
            "|   o   |",
            "|o      |",
            " ------- ",
        ]
    elif number == 4:
        # Update the dice representation for number 4
        dice = [
            " ------- ",
            "|o     o|",
            "|       |",
            "|o     o|",
            " ------- ",
        ]
    elif number == 5:
        # Update the dice representation for number 5
        dice = [
            " ------- ",
            "|o     o|",
            "|   o   |",
            "|o     o|",
            " ------- ",
        ]
    elif number == 6:
        # Update the dice representation for number 6
        dice = [
            " ------- ",
            "|o     o|",
            "|o     o|",
            "|o     o|",
            " ------- ",
        ]

    # Print the current dice representation line by line
    for line in dice:
        print(line)

    # Prompt the user to ask if they want to roll the dice again
    again = input("Do you want to roll again? (Y/N): ")

    # If the user chooses 'n', stop the loop; otherwise, roll again
    if again.lower() == "n":
        loop = False
    else:
        # Generate a new random number for the next dice roll
        number = random.randint(1, 6)
