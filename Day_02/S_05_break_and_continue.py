# break and continue


# break

i=1

while (i<=10):
    if (i%6 == 0):
        break
    print(i)
    i += 1


# continue

num=1

while (num<=10):
    if (num == 3):
        num+=1
        continue
    print(num)
    num += 1