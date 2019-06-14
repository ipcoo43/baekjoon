# 1. 함수의 정의 - fibo(n)은 n번째 피보나치 수를 출력하는 함수
# 2. 점화식과 초항
# 2-1. 점화식 : fibo(n) = fibo(n-1) + fibo(n-2)
# 2-2. 초항 : s(0,1) = 1, 1

def fibo(n):
    if n <= 1:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(5))