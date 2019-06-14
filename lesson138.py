# Log Square(정사각형) N Complexity(복잡성)
# logarithms(대수:로그)

def logarithms(n):
    i = 1
    cnt = 0
    while i <= n:
        j = n
        while j > 0:
            j = j // 2
            cnt += 1
        i *= 2
    return cnt
print(logarithms(10))