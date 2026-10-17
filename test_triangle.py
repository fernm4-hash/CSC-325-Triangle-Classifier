import math
import pytest
from triangle import is_valid_triangle, classify_triangle

def test_valid_triangle():
    assert is_valid_triangle(3, 4, 5) == True

def test_degenerate_triangle():
    assert is_valid_triangle(1, 1, 2) == False
def test_negative_side():
    assert is_valid_triangle(-1, 2, 3) == False

def test_zero_side():
    assert is_valid_triangle(0, 2, 3) == False

def test_valid_equilateral_triangle():
    assert is_valid_triangle(5, 5, 5) == True

def test_classify_equilateral_triangle(): 
    assert classify_triangle(5, 5, 5) == "Equilateral"

def test_classify_isosceles_triangle():
    assert classify_triangle(5, 5, 8) == "Isosceles"

def test_classify_scalene_triangle():
    assert classify_triangle(3, 4, 6) == "Scalene"

def test_classify_right_triangle():
    assert classify_triangle(3, 4, 5) == "Right Scalene"

def test_classify_isosceles_right_triangle():
    assert classify_triangle(1, 1, math.sqrt(2)) == "Right Isosceles"

def test_classify_invalid_triangle():
    assert classify_triangle(1, 2, 3) == "Invalid"