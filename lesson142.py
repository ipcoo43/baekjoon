# N Log Square Complexity

def func(n):
    cnt = 0
    for i in range(n//2, n):
        j = 1
        while j+n/2 <= n:
            k = 1
            while k <= n:
                cnt +=1
                k *= 2
            j *= 2
    print(cnt)
func(20)