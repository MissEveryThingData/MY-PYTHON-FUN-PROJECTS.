import random

def roll_dice():

    dice_drawing = {1: (

        "┌─────────┐",

        "│         │",

        "│    ●    │",

        "│         │",

        "└─────────┘",

    ),

    2: (

        "┌─────────┐",

        "│  ●      │",

        "│         │",

        "│      ●  │",

        "└─────────┘",

    ),

    3: (

        "┌─────────┐",

        "│  ●      │",

        "│    ●    │",

        "│      ●  │",

        "└─────────┘",

    ),

    4: (

        "┌─────────┐",

        "│  ●   ●  │",

        "│         │",

        "│  ●   ●  │",

        "└─────────┘",

    ),

    5: (

        "┌─────────┐",

        "│  ●   ●  │",

        "│    ●    │",

        "│  ●   ●  │",

        "└─────────┘",

    ),

    6: (

        "┌─────────┐",

        "│  ●   ●  │",

        "│  ●   ●  │",

        "│  ●   ●  │",

        "└─────────┘",

    ),
    }

    roll = input("roll dice? (yes r no):")

    while roll.lower == "yes".lower():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        print ("dice rolled:{} and {}".format(dice1,dice2))
        print ("\n".join(dice_drawing[dice1]))
        print ("\n".join(dice_drawing[dice2]))

        roll = input("Roll again? (yes/no)")

roll_dice()
