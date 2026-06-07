# operators in python

# 1. Arithmetic operators

a = 10
b = 5 

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

# a pow b
print(a ** b)


# 2. relational operators

print(a < b)  # false
print(a > b)  # true
print(a == b) # false
print(a != b) # true
print(a >= b) # true


# 3. assignment operators

a += 1
print(a)  # 11


# 4. logic operators

# not
var = False
print(not var)  # true

# and
print(3<5 and 5>10)  # false
print(3<5 and 10>5)  # true

# or
print(3<5 or 5>10)  # true
print(3<5 or 10>5)  # true
print(3>5 or 5>10)  # false