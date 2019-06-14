# If Else

# O(1)
def simple_if_condition(n):
    i = n
    if i == 0:
        i += 1
    print(i)

# O(1)
def if_else_condition(n):
    i = n
    if i == 0:
        i += 1
    elif i == 1:
        i += 2
    print(i)

# O(n)
def if_else_condition2(n):
    i = n
    if i > 0:
        for j in range(1,n):
            print(j)
    elif i < 0:
        i += 2
    print(i)

# O(n^2)
def if_else_condition3(n):
    i = n
    if test_func(n) > 0:
        for j in range(1,n):
            print(j)
    elif i < 0:
        i += 2
    print(i)

# O(n)
def test_func(n):
    for j in range(1,n):
        print(j)