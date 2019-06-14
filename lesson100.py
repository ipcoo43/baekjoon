# 문제 : 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력 : 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10) ( 2, 3 )
# 출력 : 첫째 줄에 A+B를 출력한다. ( 5 ) 
# 사용 함수 : list(map(func, *tterables)), str.split(seq=none, maxsplit=-1)

a, b = map(int, input('>>> ').split())
print(a + b)  # 2 3 => 5

# map은 원본 리스트를 변경하지 않고 새 리스트 생성
# list(map(함수, 리스트))
# tupe(map(함수, 튜플))
# map(func,*iterables)
# list, dictionary와 같은 iterable한 데이터를 인자로 받다
# list 안의 개별 item을 함수의 인자로 전달하여 
# 결과를 list로 형태로 반환해 주는 함수

def func(x):      # 인자로 받은 정수를 
    return x * 2  # 2배로 곱하여 반환

print(list(map(func, [1,2,3,4])))  # [2, 4, 6, 8]
x = {1:10, 2:20, 3:30}
print(list(map(func, x))) # [2, 4, 6]
print(list(map(func, [x[i] for i in x]))) # [20, 40, 60]

# 실수가 저장된 리스트가 있을때 
# 이 리스트의 모든 요소를 정수로 변환하려면 어떻게 할까?
a = [1.2, 2.5, 3.7, 4.6]
# range(len(a))를 사용하여 인덱스를 가져온다
for i in range(len(a)): # 가져온 인덱스로 요소 하나 하나에 대해
    a[i] = int(a[i]) # 접근한 뒤 int로 변환하여 다시 저정
print(a)  # [1, 2, 3, 4]

# 매번 for 반복문으로 반복하면서 요소를 변환하려니 번거롭다
# 이때 map를 사용하면 편리하다
b = [1.2, 2.5, 3.7, 4.6]
print(list(map(int,b)))  # [1, 2, 3, 4]
# 리스트의 모든 요소를 int로 변환후에 map의 결과를 list로 생성

# map에는 list뿐만 아니라 반복 가능한 객체를 넣을 수 있다.
print(list(map(str,range(5)))) # ['0', '1', '2', '3', '4']

# map이 반환하는 map 객체는 iterator라서 변수 여러개 저장(unpacking) 가능
# a,b=map(int,input().split())
x = input('>>> ').split() # input().split()의 결과는 문자열 리스트
m = map(int,x) # list의 요소를 int로 변환, 결과를 map object
a,b = m  # map object는 변수 여러 개에 저장할 수 있다.
print(a,b) 


# split 문자열을 나눌 수 있다
# str.split(seq=none, maxsplit=-1)
# seq : 분리할 문자열 구분자
# maxsplit : 분리할 문자열 개수를 지정할 때 사용
# 만약 1을 입력하면 maxsplit + 1 더해 져서 2개로 분리 된다
# massplit으로 값을 입력하지 않으면 기본값 -1이 들어 갑니다.
# 분리하는 순서는 앞에서 차례대로 된다.
print('1,2,3,4'.split(',',maxsplit=2)) # ['1', '2', '3,4']
print('1,2,3,4'.split(',')) # ['1', '2', '3', '4']

x,y,z = 'a,b,c'.split(',') # 분리 개수만큼 변수 지정하면 각각의 변수로 저장
print(x,y,z)  # a b c