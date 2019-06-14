# list, indexing, slicing
menu = ['딸기빙수','망고빙수','블루베리빙수']
print(menu[0])
print(menu[1:2])

for item in menu:
    print(item+'!! 먹고 싶어요')

for item in range(len(menu)):
    print(menu[item]+'!! 먹고 싶어요')