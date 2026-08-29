# Day 3 — Functions & Data Processing

## Goal

Learn how to create reusable functions that process data.

Today's concepts:

1. Function parameters
2. return
3. Multiple parameters
4. Default parameters
5. Functions that process lists
6. Functions + loops/conditions
7. Functions + list comprehensions

---

# 1. Function Parameters

A parameter allows a function to receive data.

```python
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

Here numbers is the parameter.

The function can work with different lists:

print(calculate_average([10, 20, 30]))
print(calculate_average([50, 60, 70]))

```


# 2. return

return sends a result back from a function.

```python
def add(a, b):
    return a + b

We can store the returned value:

result = add(10, 20)

print(result)

Output:

30

```

# 3. return vs print

```python
Using print():

def add(a, b):
    print(a + b)

The function displays the result.

Using return():

def add(a, b):
    return a + b

```

The function gives the result back so that we can use it elsewhere.

For data processing, return is usually more useful.

# 4. Multiple Parameters

A function can accept multiple parameters.

```python

def calculate_total(price, quantity):
    return price * quantity

Example:

total = calculate_total(100, 5)

print(total)

Output:

500

```

# 5. Default Parameters

A parameter can have a default value.

```python

def greet(name, message="Hello"):
    return message + " " + name

If we don't provide message:

print(greet("Shafi"))

Output:

Hello Shafi

We can also provide a different message:

print(greet("Shafi", "Welcome"))

Output:

Welcome Shafi

```

# 6. Functions That Process Lists

Functions can receive lists and process their data.

```python

def get_passing_scores(scores):
    result = []

    for score in scores:
        if score >= 50:
            result.append(score)

    return result

Example:

scores = [45, 78, 92, 56, 33, 88]

passing = get_passing_scores(scores)

print(passing)

Output:

[78, 92, 56, 88]

```

# 7. Function + List Comprehension

The previous function can also be written using list comprehension:

```python

def get_passing_scores(scores):
    return [score for score in scores if score >= 50]

This produces the same result.

```

# 8. Returning Multiple Values

A function can return multiple values.

```python

def analyze_scores(scores):
    average = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)

    return average, highest, lowest

We can receive the values:

average, highest, lowest = analyze_scores(scores)

print(average)
print(highest)
print(lowest)

```

# 9. Why Functions Matter in AI/ML

Machine learning projects usually have multiple steps.

```python

For example:

Raw Dataset
     ↓
clean_data()
     ↓
prepare_features()
     ↓
train_model()
     ↓
evaluate_model()

```

Functions allow us to separate these tasks into reusable pieces.

This makes ML programs easier to:

Understand

Test

Debug

Reuse

Maintain