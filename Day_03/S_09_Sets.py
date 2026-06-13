# Sets

set = {1,2,2,2,2}

print(set)  # {1, 2} it removes duplicate values


# add()

set.add(3)

print(set)  # {1, 2, 3}


# remove()

set.remove(1)

print(set)  # {2, 3}


# clear()

# set.clear()

# print(set)  # set()


# pop()

# set is {2,3}

set.pop()

print(set)  # {3}


# union

s1 = {1,2,3,4,5}
s2 = {5,6,7,8,9}

print(s1.union(s2))  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

print(s1.intersection(s2))  # {5}