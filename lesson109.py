import math
def check_prime(n):
    for i in range(2,int(math.sqrt(n))+1): # n**0.5
        if n % i == 0:
            return False
    return True

def cnt_prime(a,b):
    cnt = 0
    for i in range(a,b):
        if check_prime(i):
            cnt += 1
    return cnt

print(cnt_prime(12, 24))