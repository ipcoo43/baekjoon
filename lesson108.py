# 소수 카운트 
def check_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

for i in range(1,10):
    if check_prime(i):
        print(i, end=' ')
print()

cnt = 0
for i in range(1,10):
    if check_prime(i):
        cnt +=1
print(cnt)

def cnt_prime(a,b):
    cnt = 0
    for i in range(a,b):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
        if flag:
            cnt += 1
    return cnt
print(cnt_prime(12,24))

def cnt_prime(a,b):
    cnt = 0
    for i in range(a,b):
        if check_prime(i):
            cnt += 1
    return cnt
print(cnt_prime(12,24))