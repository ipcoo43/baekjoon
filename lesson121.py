# 함수의 정의 : p(n)은 p(n-1)을 호출하고 n을 출력한다
# 초항 : n == 0이면 끝

def p(n):
    if n == 0:
        return
    p(n-1)
    print(n, end=' ')
p(10)

print()   

def p2(n):
    if n > 1:
        p2(n-1)
    print(n, end=' ')
p2(10)