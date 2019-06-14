# 에라토스테네스의 체
# 1) n까지 체(sieve)를 만든다
# 2) 소수(prime)를 저장할 리스트를 만든다
# 3) 체의 첫 번째 숫자, 2(i)를 저장한다
# 4) 체에서 2(i)의 배수를 지운다
# 5) n까지 3), 4)를 반복한다.

# for 반복문 사용
def eratos(n):
    sieve = [1] * (n+1)      # 1) n까지 체(sieve)를 만든다
    prime = []               # 2) 소수(prime)를 저장할 리스트를 만든다
    for i in range(2,n+1):
        if sieve[i] == 1:
            prime.append(i)  # 3) 체의 첫 번째 숫자, 2(i)를 저장한다
            for j in range(i, n+1, i):
                sieve[j] = 0 # 4) 체에서 2(i)의 배수를 지운다
    return prime
print(eratos(11))
print()