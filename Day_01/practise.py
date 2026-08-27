# Exercise 1 — Variables - # Print all four.

name = "Shafi"
age = 24 
city = "Saundatti"
favorite_number = 78


print(name,age,city,favorite_number)



# Exercise 2 — List

# Create:

numbers = [10, 25, 30, 45, 50, 65]

# Find:

# total
# number of elements
# highest number
# lowest number
# average

print(sum(numbers))
print(len(numbers))
print(max(numbers))
print(min(numbers))
print((sum(numbers)/len(numbers)))



# Exercise 3 — Loop

# Using the same list, print every number.

# Then print only numbers greater than 30.


for num in numbers:
    if num>30:
        print(num)



# Exercise 4 — Function

# Create:

# def calculate_average(numbers):
#     # your code

# Test it with:

numbers = [10, 20, 30, 40, 50]

# Expected: 30.0


def calculate_average(numbers):
    return sum(numbers)/len(numbers)

my_ans = calculate_average(numbers)
print(my_ans) # 30.0