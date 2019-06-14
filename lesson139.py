# Logaithms (대수 로그)

def logarithms(n):
    i = n
    while i >= 1:
        i //= 2
        print(i)
logarithms(100)
print()

def logarithms2(n):
    i = 1
    while i <= n:
        i *= 2
        print(i)
logarithms2(100)