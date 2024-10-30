def quadratic(a,b,c):
    """
    define a function that can solve the quadratic equation
    shown below using the quadratic formula also shown below.
    
    equation:
    ax^2 + bx + c = 0

    formula:
    x = -b +- sqrt(b^2 - 4ac)/2a
    """
    import math
    quadratic_pos = ((-1*b) + math.sqrt((b^2) - (4*a*c)))/(2*a)
    quadratic_neg = ((-1*b) - math.sqrt((b^2) - (4*a*c)))/(2*a)

    return quadratic_pos, quadratic_neg

