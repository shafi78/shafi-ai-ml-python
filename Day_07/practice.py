# Exercise 1 — Handle Invalid Number

# Write a program that:

# number = int(input("Enter a number: "))

# If the user enters:

# abc

# print:

# Invalid number

# Use try and except ValueError.

try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid number")




# Exercise 2 — Division

# Ask the user for a number and divide 100 by it.

# Handle:

# ValueError
# ZeroDivisionError

# Example:

# Enter number: 0
# Cannot divide by zero


try:
    number = int(input("Enter number: "))
    result = 100 / number
    print(result)

except ValueError:
    print("Please enter a valid number")

except ZeroDivisionError:
    print("Cannot divide by zero")




# Exercise 3 — Dictionary

# Given:

student = {
    "name": "Shafi",
    "score": 85
}

# Try accessing:

# student["age"]

# Handle the KeyError.

# Expected:

# Age information not available


try:
    print(student["age"])

except KeyError:
    print("Age information not available")




# Exercise 4 — List

# Given:

numbers = [10, 20, 30]

# Try:

# numbers[10]

# Handle the IndexError.


try:
    print(numbers[10])

except IndexError:
    print("Invalid list index")




# Exercise 5 — File

# Try opening:

# unknown.txt

# Handle:

# FileNotFoundError

# Expected:

# File not found


try:
    file = open("unknown.txt")

except FileNotFoundError:
    print("File not found")





# Exercise 6 — Validation with raise

# Create:

# def validate_score(score):
#     # your code

# If score is less than 0 or greater than 100, raise:

# ValueError("Score must be between 0 and 100")

# Example:

# validate_score(150)

# should produce the error.


def validate_score(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")

    return score


print(validate_score(150))