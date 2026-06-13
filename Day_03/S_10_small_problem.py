# problem

# given a list of typles with info(name,subject)

# 1. list all unique course
# 2. list students enrolled in javascript
# 3. create dictionary(student,set of courses)

info = [
    ("shafi","python"),
    ("bharath","javascript"),
    ("geerthi","javascript"),
    ("sameer","python"),
    ("shafi","java"),
    ("yusuf","javascript")
]

# 1.

course_set = set()

for i in info:
    course_set.add(i[1])

print(course_set)  # {'java', 'python', 'javascript'}

# 2. 

for i in info:
    if (i[1] == "javascript"):
        print(i[0])

# bharath geerthi yusuf


# 3. 

dict = {}

for name,course in info:
    if (dict.get(name) == None):
        dict.update({name:set()})
        dict[name].add(course)

    else:
        dict[name].add(course)

print(dict)

# {'shafi': {'java', 'python'}, 'bharath': {'javascript'}, 'geerthi': {'javascript'}, 'sameer': {'python'}, 'yusuf': {'javascript'}}