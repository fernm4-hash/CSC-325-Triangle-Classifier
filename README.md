# CSC-325-Triangle-Classifier


## Copilot Review Log

| Test | Copilot-suggested? | Kept / Edited / Rejected | Why |
|---|---|---|---|
| `test_is_valid_triangle` | Yes | Edited | Copilot combined five scenarios into one test, causing Assertion Roulette. I separated them into individual tests. |
| `test_classify_equilateral_triangle` | Yes | Kept | Correctly tested an equilateral triangle. |
| `test_classify_isosceles_triangle` | Yes | Kept | Correctly tested an isosceles triangle. |
| `test_classify_scalene_triangle` | Yes | Edited | Copilot expected Scalene for (3, 4, 5), which is a right triangle. I changed the input to (3, 4, 6). |
| `test_classify_right_triangle` | Yes | Kept | Correctly tested a right scalene triangle. |
| `test_classify_isosceles_right_triangle` | Yes | Kept | Correctly tested a right isosceles triangle with a non-integer side. |
| `test_classify_invalid_triangle` | Yes | Kept | Correctly tests a invalid triangle. |

## Acceptance Criteria  

When a customer enters 3 valid sides lengths, the system must return the correct triangle classification  
  
When a customer enters 3 sides that cannot form a triangle, the system must return "Invalid" without crashing  
  
When a customer enters 3 sides that form a right triangle, the system must add the prefix "right" to the triangle classification

## How to run tests

1. Clone GitHub repo or open project in Vs code  
2. Install the required dependencies: python -m pip install -r requirements.txt  
3. Run the tests in terminal: pytest test_triangle.py, text_acceptance.py  

## Equivalence Classes and Boundaries

| Class | Representative test | Expected result |
|---|---|---|
| Valid equilateral | (5,5,5) | Equilateral |
| Valid isosceles | (5,5,8) | Isosceles |
| Valid scalene | (3,4,6) | Scalene |
| Right scalene | (3,4,5) | Right Scalene |
| Right Isosceles | (1,1,sqrt(2)) | Right Isosceles |
| Negative side | (-1,2,3) | Invalid |
| Zero Side | (0,2,3) | Invalid |
| Invalid triangle | (1,1,2) | Invalid |

## Why an equilateral cannot be right 
Since all of the sides of a equilateral triangle are equal, this means all the angles must be equal. To be a right triangle one of its angles must be 90 degrees, a equilateral triangle can only have angles of 60 degrees.  

## Ai disclouser 

I used GitHub Copilot's autocomplete feature to generate suggestions for the unit tests in test_triangle.py. I reviewed the suggestions and corrected mistakes, including an incorrect scalene triangle classification and an Assertion Roulette.  

I also used ChatGPT to help me format the README file. 