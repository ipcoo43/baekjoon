# 중목되지않는 무작위 숫자 뽑기

import random

lst = []
ran_num = random.randint(1,9)
for i in range(8):
    while ran_num in lst:
        ran_num = random.randint(1,9)
    lst.append(ran_num)
#lst.sort()
print(lst)

lst2 = [1, 2, 3, 4, 5, 6]
out = random.sample(lst2,len(lst2))
print(out)