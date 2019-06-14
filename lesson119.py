# 1. 함수의 정의 - bin(n)은 10진수를 2진수로 바꿔주는 함수
# 2. 점화식과 초항
# 2-1. 점화식 : bin(n) = bin(n//2) + n % 2
# 2-2. 초항 : bin(0) = 0, bin(1) = 1

def bin(n):
    if n <= 1:
        return n
    return str(bin(n//2))+str(n%2)

print(bin(1024))