# N Power 5 Complexity

def func(n):
    for i in range(1, n):
        j = i
        while j < i * i:
            j += 1
            if j%i == 0:
                for k in range(0, j):
                    print(' * ',end=' ')
func(10)