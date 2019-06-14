# 입력과 출력, 그리고 변수
a=4
print(a)
print(type(a))
print(a+10)

b='4'
print(b)
print(type(b))
print(b+'10')
print(int(b) + int('10'))

name = input('>>> name : ')
older = '4'
age = int(input('>>> age : '))
print(age, older)
print(name,'님은',age + int(older),'살 처럼 보이네요')