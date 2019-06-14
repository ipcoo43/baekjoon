# 파일 입출력
# open() : 파일 여는 함수
# close() : 파일 닫는 함수
# 파일 열기 모드의 종류
# 'r' : read, 읽기 모드
# ex) f = open('data.txt')
# 'w' : write, 쓰기 모드
# ex) f = open('file.txt', 'w')
# 'a' : append, 추가(이어쓰기) 모드
# ex) f = open('file.txt', 'a')

f = open('data.txt',encoding='utf-8')
print(f.read())
f.close()
print()

f = open('data.txt',encoding='utf-8')
for row in f:
    print(row)
f.close()
print()

f = open('today.txt', 'w' ,encoding='utf-8')
f.write('원하는 내용을 입력해주세요!!!\n')
f.write('오늘은 무엇을 드실건가요?\n')
f.close()

f = open('today.txt', 'a',encoding='utf-8')
for i in range(5) :
     f.write('저는 치킨이 좋아요!!!!\n')
f.close()

f = open('today.txt',encoding='utf-8')
for row in f:
    print(row.strip())
f.close()