string = "shafi"

# in -> membership operator

for var in string:
    print(var)


# in

if 's' in string:
    print("exisits!")

else:
    print("not exists!")



for i in range(10):
    print(i)    # 0 to 9
    print(i+1)  # 1 to 10


# count no of a's in this word

word = "bharath sarkar"
count = 0 

for ch in word:
    if (ch == 'a'):
        count += 1 

print(count)