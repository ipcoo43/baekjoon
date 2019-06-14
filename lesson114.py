def b(n):
    a = []
    for i in range(n):
        if i % 2 == 0:
            a.append(i**2)
    return a

def c(n):
    return [i**2 for i in range(n) if i % 2 == 0 ]

print(b(11))
print(c(11))