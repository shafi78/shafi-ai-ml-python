# type convertion

name = "shafi"
print(type(name))  # str

ans1 = int(5+10.0)  # casting
ans2 = 5+10.0  # convertion

print(ans1,type(ans1))  # 15 int
print(ans2,type(ans2))  # 15.0 float

val = int("123")
print(type(val))  # int

val1 = bool(0) # zero value
val2 = bool(10) # non-zero value

print(val1,type(val1))  # false bool
print(val2,type(val2))  # true bool