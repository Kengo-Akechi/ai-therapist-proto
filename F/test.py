def roll_dice():
    import random
    number = random.randint(1, 6)
    msg = "You rolled a " + number
    return msg

print(roll_dice())
