from triangle import classify_triangle

def test_acceptance_criteria():
    #Acceptance Criteria 1:
    assert classify_triangle(5, 5, 5) == "Equilateral"

    #Acceptance Criteria 2:
    assert classify_triangle(-3, 3, 6) == "Invalid"

    #Acceptance Criteria 3: 
    assert classify_triangle(3, 4, 5) == "Right Scalene"