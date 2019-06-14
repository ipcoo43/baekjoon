# Complexity With Break Statement : Break문과 복잡성

def func(n):
    cnt = 0
    for i in range(n//2, n):
        j = 1
        cnt += 1
        while j+n/2 <=n:
            j = j*2
            cnt += 1
            break
    print(cnt)
func(20)