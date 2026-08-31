# Day 5 — Strings & Text Processing

## Goal

Learn how to work with text using Python.

Today's concepts:

1. String basics
2. String indexing
3. String slicing
4. lower()
5. upper()
6. strip()
7. replace()
8. split()
9. join()
10. in
11. len()

---

# 1. Strings

A string represents text.

```python
name = "Shafi"
message = "I am learning AI"

```

# 2. String Indexing

Strings use zero-based indexing.

```python

name = "Shafi"
S h a f i
0 1 2 3 4

Example:

print(name[0])
print(name[-1])

Output:

S
i

```

# 3. String Slicing

String slicing works similarly to list slicing.

```python

text = "Artificial"

print(text[0:4])

Output:

Arti

```

The start index is included and the stop index is excluded.

# 4. lower() and upper()

```python

text = "Hello World"

print(text.lower())
print(text.upper())

Output:

hello world
HELLO WORLD

```

Lowercase conversion is useful when normalizing text.

# 5. strip()

strip() removes whitespace from the beginning and end of a string.

```python

text = "   hello world   "

print(text.strip())

Output:

hello world

```

# 6. replace()

replace() replaces part of a string.

```python

text = "I love Python"

new_text = text.replace("Python", "AI")

print(new_text)

Output:

I love AI

```

Strings are immutable, so replace() returns a new string.

# 7. split()

split() converts a string into a list.

```python

sentence = "I am learning AI"

words = sentence.split()

print(words)

Output:

["I", "am", "learning", "AI"]

We can also split using a specific separator.

data = "Shafi,Guru,Cindrella,Sam"

names = data.split(",")

print(names)

```

# 8. join()

join() combines a list of strings into one string.

```python

words = ["I", "am", "learning", "AI"]

sentence = " ".join(words)

print(sentence)

Output:

I am learning AI

Remember:

split()
String → List

join()
List → String

```

# 9. in

The in operator checks whether a value exists inside a string.

```python

text = "I am learning AI"

print("AI" in text)

Output:

True

```

# 10. len()

len() returns the number of characters in a string.

```python

text = "Shafi"

print(len(text))

Output:

5

```