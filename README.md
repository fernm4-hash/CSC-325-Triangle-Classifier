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