import random as rand

def sum_die(n):
    """
    Sum the values of random dice throws until the sum
    is greater than the given number n.
    How many times was the dice thrown?
    How many times did the die land on a specific number?
    """
    tosses = 0
    dice_sum = 0
    dice_land = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    while dice_sum <= n:
        die = rand.randint(1,6)
        dice_land[die] += 1
        dice_sum += die
        tosses += 1
    
    return tosses, dice_sum, dice_land

final = sum_die(n=rand.randint(0,100))

tosses = final[0]
dice_sum = final[1]
dice_land = final[2]

print("Amount of throws:",tosses)
print("Final sum:", dice_sum)
print(dice_land)

#Could split this exercise by splitting into sorting what number
#is thrown into a list then converting to a dictionary?