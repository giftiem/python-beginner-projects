"""
Approximating pi by throwing darts at a target and using the area 
of a square and a circle.
   +r|
     |
------------
-r   |    +r
     |-r

Areas:
    Area_of_circle = pi*r^2
    Area_of_square = 2r*2r = 4r^2

    Area_of_circle/Area_of_square = pi*r^2/4r^2
                                  = pi/4
    
Approximation:
    darts_landing_circle/darts_landing_square approx= pi/4

"""
import random
import math

def dart(r):
    """
    Write a function that will return random coordinates for
    each dart thrown
    """
    x = random.randint(-r,r)  
    y = random.randint(-r,r)
    return x,y

def dart_landing_position(x,y,r):
    """
    Write a function that evaluates if the dart landed in the 
    circle or the square
    """
    area_of_circle = ma
