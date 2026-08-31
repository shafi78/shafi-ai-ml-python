# Text Analyzer

# Given:

text = """
   Python is amazing.
   Python is powerful.
   I am learning AI and Machine Learning.
"""


# Your program should:

# 1. Clean the text

# Remove unnecessary spaces and convert it to lowercase.

# 2. Split it into words

# Create a list of words.

# 3. Count total words
# 4. Count how many times python appears
# 5. Check whether ai exists
# 6. Remove the . characters
# 7. Print the cleaned text

# Expected output should contain something like:

# Text Analyzer

# Cleaned Text:
# python is amazing python is powerful i am learning ai and machine learning

# Total Words: 12

# Python Count: 2

# Contains AI: True



print("Text Analyzer")

print()

cleaned_text = text.strip().lower()

cleaned_text = cleaned_text.replace(".", "")

cleaned_text = " ".join(cleaned_text.split())

words = cleaned_text.split()

tot_words = len(words)

python_count = words.count("python")

contains_ai = 'ai' in words 

print("Cleaned Text:")

print()

print(cleaned_text)

print()

print("Total Words:",tot_words)

print()

print("Python Count:",python_count)

print()

print("Contains AI:",contains_ai)