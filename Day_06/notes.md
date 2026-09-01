# Day 6 — File Handling & Real Data

## Goal

Learn how Python reads and writes data stored in files.

Today's concepts:

1. open()
2. Reading files
3. Writing files
4. Appending files
5. with open()
6. Reading lines
7. JSON

---

# 1. open()

Python uses open() to work with files.

```python
file = open("data.txt", "r")

Common modes:

"r" → read
"w" → write / overwrite
"a" → append

```

# 2. Reading a File

```python

with open("data.txt", "r") as file:
    content = file.read()

print(content)

read() reads the entire file as a string.

```

# 3. with open()

```python

Using:

with open("data.txt", "r") as file:

is preferred because Python automatically closes the file.

```

# 4. Reading Line by Line

```python

with open("scores.txt", "r") as file:
    for line in file:
        print(line.strip())

strip() removes whitespace and the newline character.

```

# 5. readlines()

```python

with open("scores.txt", "r") as file:
    lines = file.readlines()

This returns a list containing each line.

Example:

["85\n", "72\n", "91\n"]

We can clean the lines:

scores = [int(line.strip()) for line in lines]

```

# 6. Writing to a File

```python

with open("output.txt", "w") as file:
    file.write("Hello")

"w" writes to the file and overwrites existing content.

```

# 7. Writing Multiple Lines

```python

with open("students.txt", "w") as file:
    file.write("Shafi\n")
    file.write("Guru\n")
    file.write("Cindrella\n")
    file.write("Sam\n")

The \n creates a new line.

```

# 8. Appending

Use "a" to add data without replacing existing content.

```python

with open("students.txt", "a") as file:
    file.write("Sam\n")

Remember:

"w" → overwrite
"a" → append

```

# 9. JSON

JSON is a common format for storing structured data.

```python

Example:

{
    "name": "Shafi",
    "score": 85
}

Python can work with JSON using the json module.

import json

```

# 10. Python Dictionary → JSON

```python

student = {
    "name": "Shafi",
    "score": 85
}

with open("student.json", "w") as file:
    json.dump(student, file)

```

# 11. JSON → Python Dictionary

```python

import json

with open("student.json", "r") as file:
    student = json.load(file)

print(student)

```