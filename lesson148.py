# Recursive N Complexity


def func(n):
    cnt = 1
    if n <= 0:
        return
    for i in range(1, n):
        cnt += 1
    n = n//2
    func(n)
    print(cnt, end=' ')
func(20)
print()

def func2(n):
    if n <= 0:
        return
    print('*')
    func2(n//2)
    func2(n//2)
    print('*',end=' ')
func2(20)
    