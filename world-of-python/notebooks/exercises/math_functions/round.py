
"""round.py

Simple example program demonstrating Python's built-in `round()` function.

This script reads a floating-point number from standard input, rounds it to
two decimal places, and prints the result. It is intended as a small
exercise for learners to see how `round()` works in practice.

Notes:
- `round(x, 2)` returns `x` rounded to 2 decimal places. For values exactly
	halfway between two possible rounded values (for example, `2.5`), Python
	uses bankers' rounding (round-to-even) behavior.

Usage example:
> python round.py
Enter a floating-point number: 3.14159
The number 3.14159 rounded to 2 decimal places is 3.14.

You can modify the code to round to a different number of decimal places or
to accept input from another source.
"""

num = float(input("Enter a floating-point number: "))
rounded_num = round(num,2)
print(f"The number {num} rounded to 2 decimal places is {rounded_num}.")