import random as rand
def dice_toss(n):
    """
    Simulate rolling a dice until it lands on a number n.
    """
    counter = 0
    flag = True
    while flag:
        die = rand.randint(1,6)
        flag = (die != n)
        counter += 1
    
    return counter

tosses = dice_toss(n=rand.randint(1,6))
print(tosses)