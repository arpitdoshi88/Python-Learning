"""Exponentiation calculator.

Reads a base and an exponent from standard input (as floats) and prints
the result of raising the base to the exponent, formatted to two
decimal places.

Example:
    Enter the base number: 2
    Enter the exponent number: 3
    2.0 to the power of 3.0 is 8.00
"""

base = float(input("Enter the base number: "))
exponent = float(input("Enter the exponent number: "))

result = base ** exponent
print(f"{base} to the power of {exponent} is {result:.2f}")