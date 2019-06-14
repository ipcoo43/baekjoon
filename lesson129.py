# 모듈 : 함수 꾸러미

import random
fruits = ['딸기','포도','망고','두리안','블루베리']

# random.shuffle(리스트) : 리스트 섞기
random.shuffle(fruits)
print(fruits)

# random.choice(리스트) : 리스트에서 하나 뽑기
for i in range(len(fruits)):
    print(random.choice(fruits))
    
# andom.randrange(정수) : 원하는 범위에서 랜덤하게 정수 만들기
print(random.randrange(100))

# random.randint(정수1,정수2) : 원하는 정수 랜덤하게 만들기
dice = []
for i in range(10):
    dice.append(random.randint(1,6))
print(dice)