# functions


# function defination

def hello():
    print("hello shafi!")


# function call

hello() # hello shafi!


# sum of 2 numbers

def sumFunc(a,b):
    print(a+b)

sumFunc(5,10)  # 15


# return function

def minusFunc(a,b):
    final = a-b 
    return final

print(minusFunc(10,5))  # 5


# bydefault parameters

def sumCal(a,b=1):
    print(a+b)

sumCal(5)  # 6  Note: im passing value for only a variable


# function types

# 1) built in
# print()
# input()
# type()
# range()

# 2) user defined
# ex: calculateSum() , all functions created by user/developer



# lambda function

avg = lambda a,b: (a+b)/2
print(avg(4,5))