# 소수 리스트 만들기

def check_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def list_prime(n):
    prime = []
    for i in range(1,n):
        if check_prime(i):
            prime.append(i)
    return prime

print(list_prime(100))