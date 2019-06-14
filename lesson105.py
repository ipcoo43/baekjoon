# 12의 약수

n = 12
r = []
for i in range(1,n+1): # 1부터 n+1까지 원소 i에 대해
    if n % i == 0:     # n을 i로 나눠 나머지가 0일때
        r.append(i)    # r에 i를 추가하라
print(f'{n}의 약수는 {r}')

def divisior():
    n = 12
    for i in range(1,n+1):
        if n % i == 0:
            print(i, end=' ')
divisior()
print()

def divisior(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=' ')
divisior(12)
print()

for i in range(2,13):
    divisior(i)
    print()