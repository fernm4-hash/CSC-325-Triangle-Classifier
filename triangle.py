import math

def is_valid_triangle(a, b, c) -> bool:
    if a <=0 or b <=0 or c <= 0:
        return false
    
    if a + b <= c or a + c <= b or b + c <= a:
        return false
    
    return true

def classify_triangle(a, b, c) -> str:
    if not is_valid_triangle(a,b,c):
        return "Invalid"
    
    if a == b == c:
        triangle = "Equilateral"
    
    elif a == b or a == c or b == c:
        triangle =  "Isosceles"

    else:
        triangle = "Scalene"

    sides = [a,b,c]
    sides.sort()


    if math.isclose(a**2 + b**2, c**2):
        return "Right " + triangle 
        