# 함수의 정의 : p(n)은 n을 출력하고 p(n-1)을 호출한다.
# 초항 : n == 0이면 끝

def p(n):
    if n == 0:
        return
    print(n, end=' ')
    p(n-1)
p(10)
    