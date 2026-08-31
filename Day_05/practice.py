# ### Exercise 1 — String Basics

# Given:

text = "Artificial Intelligence"

# Print:

# first character
# last character
# length
# first 10 characters


print(text[0])
print(text[-1])
print(len(text))
print(text[0:10])



# Exercise 2 — Normalize Text

# Given:

text = "   HELLO AI WORLD   "

# Convert it to:

# hello ai world

# Use:

# strip()
# lower()


print(text.strip().lower())




# Exercise 3 — Replace

# Given:

text = "I am learning Java"

# Replace Java with Python.

# Expected:

# I am learning Python

print(text.replace("Java","Python"))




# Exercise 4 — Split

# Given:

sentence = "Python is easy to learn"

# Convert it into:

# ["Python", "is", "easy", "to", "learn"]

# Then print each word using a loop.


arr = sentence.split(" ")

print(arr)

for word in arr:
    print(word)




# Exercise 5 — Join

# Given:

words = ["Machine", "Learning", "is", "interesting"]

# Convert it into:

# Machine Learning is interesting

# Use join().


sentence = " ".join(words)
print(sentence)




# Exercise 6 — Text Filtering

# Given:

sentences = [
    "I love Python",
    "Machine Learning is amazing",
    "I am learning AI",
    "Python is powerful",
    "I like databases"
]

# Print only sentences containing:

# Python


for sentence in sentences:
    if "Python" in sentence:
        print(sentence)




# Exercise 7 — Word Count

# Given:

sentence = "Python is very easy to learn"

# Find the number of words.

# Expected:

# 6


print(len(sentence.split()))