# Create a file called:

# names.txt

# Using Python, write:

# Shafi
# Guru
# Cindrella
# Sam


with open("./Day_06/names.txt","w") as file:
    file.write("Shafi \n")
    file.write("Guru \n")
    file.write("Cindrella \n")
    file.write("Sam \n")



# Exercise 2 — Read a File

# Read names.txt and print each name separately.

# Expected:

# Shafi
# Guru
# Cindrella
# Sam


with open("./Day_06/names.txt","r") as file:
    content = file.read()

print(content)




# Exercise 3 — Append

# Append:

# Alex

# to names.txt.

# Then read the file again.

# Expected:

# Shafi
# Guru
# Cindrella
# Sam
# Alex


with open("./Day_06/names.txt","a") as file:
    file.write("Dora \n")



# Exercise 4 — Scores

# Create:

# scores.txt

# containing:

# 85
# 72
# 91
# 45
# 67

# Read the file and convert the values into integers.

# You should end up with:

# [85, 72, 91, 45, 67]


with open("./Day_06/scores.txt","r") as file:
    scores = [int(line.strip()) for line in file]

print(scores)


# Exercise 5 — Calculate Average

# Using the list from Exercise 4, calculate:

# Average: 72.0

# Use what you learned on Day 1.


print(sum(scores)/len(scores))



# Exercise 6 — JSON

# Create a Python dictionary:

# student = {
#     "name": "Shafi",
#     "score": 85
# }

# Save it as:

# student.json

# Then read it back into Python and print:

# Name: Shafi
# Score: 85


import json

student = {
    "name": "Shafi",
    "score": 85
}

# save
with open("./Day_06/student.json", "w") as file:
    json.dump(student, file)

# read
with open("./Day_06/student.json", "r") as file:
    student = json.load(file)

print("Name:", student["name"])
print("Score:", student["score"])