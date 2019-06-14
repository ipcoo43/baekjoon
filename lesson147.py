# Recursive Complexity FN by 3

def func(n):
    if n <= 0:
        return
    for i in range(1, 3):
        func(n//3)
    print(n, end=' ')
func(6)
print()

def func2(n):
    if n <= 0:
        return
    for i in range(1,3):
        func2(n-1)
    print(n,end=' ')
func2(6)
print()

def func3(n):
    if n <= 0:
        return
    for i in range(1,3):
        func3(0.8*n)
    print(n,end=' ')
func3(10)