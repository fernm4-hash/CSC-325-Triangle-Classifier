def is_valid_triangle(a, b, c) -> bool:
    if a <=0 or b <=0 or c <= 0:
        return false
    
    if a + b <= c or a + c <= b or b + c <= a:
        return false
    
    return true