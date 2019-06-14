# 재귀 함수 이해

def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f
print(factorial(5))

# 1) 함수의 정의 : f(n)은 n 팩토리얼을 구하는 함수
# 2) 점화식과 초항
# 2-1) 점화식 : f(n) = n * f(n-1)
# 2-2) 초항 : f(1) = 1

def f(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(f(5))

# 1) 함수의 정의 : s(n)은 1부터 n까지의 합을 구하는 함수
# 2) 점화식과 초항
# 2-1) 점화식 : s(n) = n + s(n-1)
# 2-2) 초항 : s(1) = 1

def s(n):
    if n == 1:
        return 1
    return n + s(n-1)
print(s(10))