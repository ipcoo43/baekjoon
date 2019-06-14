n=12
for i in range(1,n+1):
    if n % i == 0:
        print(i,end=' ')
print()

def divisior():
    n = 12
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end = ' ')
divisior()
print()

def divisior(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end = ' ')
divisior(12)
print()
for i in range(1, 13):
    divisior(i)
    
def divisior(n):
    r = []
    for i in range(1, n+1):
        if n % i == 0 :
            r.append(i)
    return r
print(divisior(12))
for i in range(2, 13):
    print(divisior(i))          