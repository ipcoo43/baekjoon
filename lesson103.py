# sequence(시퀀스)개체와 iterable(반복가능한 객체)의 차이
# 반복 가능한 객체는 시퀀스 객체를 포함하고 있다.
# list, tuple, rnage, string은 반복 가능한 객체 이면서 시퀀스 객체이다
# dictionary, set은 반복 가능한 객체이지만 시퀀스 객체는 아니다.
# 시퀀스 객체는 
#   - 요소의 순서가 정해져 있고
#   - 연속적(sequence)으로 이어져 있어야 한다.
# dict, set은 요소(키)의 순서로 정해져 있기 때문이다.

# 스퀀스 객체 : 요소의 순서가 정해져 있고 연속적으로 이어져 있다
# 반복 가능한 객체 : 요소의 순서와 상관없이 요소를 한 번에 하나씩 꺼낼 수 있다

# sequence object : list, tuple, range, str
# iterable object : list, tuple, range, str, dict, set

iterable = ['list', 'tuple', 'range', 'str', 'dict', 'set']
sequence = ['list', 'tuple', 'range', 'str']

print('iterable = ',list(map(str,iterable)))
print('sequence = ',list(map(str,sequence)))
