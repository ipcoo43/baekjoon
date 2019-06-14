# 함수의 기초

# 1) 1+2 print
a=1
b=2
print(a+b) 

# 2) 1+2 print function
def add():
    a=1
    b=2
    print(a+b)
add()

# 3) a+b print function
def add(a,b):
    print(a+b)
add(1,2)

# 4) a+b return function
def add(a,b):
    return a+b
print(add(1,2))
print(add(add(1,2),add(1,2)))