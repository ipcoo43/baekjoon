# Sqrt Complextity

def func(n):
    i = s = 1
    while s < n:
        i += 1
        s += i
        print('*', end=' ')
func(20)
print()

def func2(n):
    i = 1
    cnt = 0
    while i * i < n:
        cnt += 1
        i += 1
    print(cnt)
func2(20)