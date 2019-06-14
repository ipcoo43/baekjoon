# list comprehension
a = []
for i in range(10):
    a.append(i)
print(a)

a = [i for i in range(10)]
print(a)

a=[]
for i in range(10):
    a.append(i**2)
print(a)

a = [i**2 for i in range(10)]
print(a)

a = []
for i in range(10):
    if i % 2 == 0:
        a.append(i**2)
print(a)

a = [i**2 for i in range(10) if i % 2 == 0]
print(a)