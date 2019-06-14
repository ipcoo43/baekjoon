# Recursive Complexity 재귀 복잡성

def func(n):
    cnt = 0
    if n <= 0:
        return
    for i in range(1, n):
        for j in range(1, n):
            cnt += 1
    func(n-3)
    print(cnt)
func(20)