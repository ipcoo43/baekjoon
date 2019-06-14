import csv
file = csv.reader(open('capital.csv',encoding='utf-8'))


capital = {}
for row in file:
    capital[row[0]] = row[1]

import random
n = random.choice(list(capital.keys()))
c = capital[n]

print(n + ' : ' + c)
'''
cnt = {}
for c in capital.values():
    if c in cnt:
        cnt[c] += 1
    else:
        cnt[c] = 1
    if cnt[c] > 1:
        print(c)
'''