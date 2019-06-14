# 소수 판별 문제
n = 11
flag = True
for i in range(2, n):
    if n % i == 0:
        flag = False
if flag:
    print('prime')
else:
    print('no prime')

def check_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
if check_prime(11):
    print('prime')
else:
    print('no prime')

for i in range(1,10):
    print(i, check_prime(i))

for i in range(1,10):
    if check_prime(i):
        print(i,end=' ')
    