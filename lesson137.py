# Log Log N Complexity(복잡성)

import math
cnt = 0
def func(n):
    global cnt
    if n <= 2:
        return 1
    else:
        func(round(math.sqrt(n)))
        cnt += 1
        return cnt
print(func(200))