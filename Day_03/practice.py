# Exercise 1 — Basic Function

# Create:

# def square(number):
#     # your code

# Example:

# print(square(5))

# Expected:

# 25

def square(number):
    return number*number 

print(square(5))



# Exercise 2 — Multiple Parameters

# Create:

# def calculate_discount(price, discount):
#     # your code

# Example:

# print(calculate_discount(1000, 20))

# Expected:

# 800


def calculate_discount(price,discount):
    return price * (1-discount / 100)

print(calculate_discount(1000,20))



# Exercise 3 — List Function

# Create:

# def get_even_numbers(numbers):
#     # your code

# Given:

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Expected:

# [2, 4, 6, 8]

# Try using a list comprehension.

def get_even_numbers(numbers):
    return [number for number in numbers if number %2 == 0]

print(get_even_numbers(numbers))



# Exercise 4 — Statistics Function

# Create:

# def analyze_numbers(numbers):
#     # your code

# It should return:

# average
# highest
# lowest

# Example:

numbers = [10, 20, 30, 40, 50]

# average, highest, lowest = analyze_numbers(numbers)

# print(average)
# print(highest)
# print(lowest)

# Expected:

# 30.0
# 50
# 10


def analyze_numbers(numbers):
    average = sum(numbers)/len(numbers)
    highest = max(numbers)
    lowest = min(numbers)

    return average,highest,lowest

print(analyze_numbers(numbers))

# or

average,highest,lowest = analyze_numbers(numbers)

print(average)
print(highest)
print(lowest)

# or

# The '*' unpacks the returned tuple into 3 separate arguments
print(*analyze_numbers(numbers), sep="\n")



