# 에라토스테네스의 체

def list_prime(n):
    sieve = [True]*n # 체 초기화: n개 요소에 True 설정(소수로 간주)
    m = int(n**0.5)  # n개의 최대 약수가 sqrt(n)이하이므로 i=sqrt(n)까지 검사
    for i in range(2, m+1):
        if sieve[i] == True:           # i가 소소인 겨우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False
    return [i for i in range(2,n) if sieve[i]==True]

print(list_prime(10))