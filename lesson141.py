# N Log N with Loops
def func(n):
    cnt = 0
    if n <= 0:
        return
    for i in range(1,n):
        j = 1
        while j < n:
            j += i
            cnt += 1
    print(cnt)

func(20)

def func2(n):
    for i in range(1,n):
        j = 1
        while j <= n:
            j *= 2
            print('*',end=' ')
func2(20)
print()
print()

def func3(n):
    for i in range(1, n//3):
        j = 1
        while j <= n:
            j += 4
            print('*',end=" ")
func3(20)