# N Cube(입방체) Log N Complexity

def func(n):
    if n < 2:
        return
    else:
        cnt = 0
    for i in range(1,8):
        func(n//2)
    for i in range(1,n**3):
        cnt += 1
    return cnt

print(func(10))