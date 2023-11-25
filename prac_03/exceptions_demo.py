"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
# A ValueError occurs when you try to convert a non-integer string to an integer using int(). For example, entering a non-numeric value (like a letter or a symbol) when prompted for the numerator or denominator will trigger a ValueError.
2. When will a ZeroDivisionError occur?
# A ZeroDivisionError occurs when attempting to divide by zero. If the user enters 0 as the denominator, it will lead to division by zero and raise a ZeroDivisionError.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")