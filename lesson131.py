# plot()

import matplotlib.pyplot as plt

plt.figure(figsize=(5,3), dpi=120) # 그래픽 크기 및 해상도 조절

plt.rc('font', family='D2Coding') # 한글 폰트 설정
plt.plot([1,2,3,4])
plt.plot([4,3,2,1])

plt.title('제목') # 제목 넣기

plt.xlim(0,3) # x축 값 범위
plt.ylim(1,4) # y축 값 범위

plt.xticks(range(4),['가','나','다','라',]) # x축 내용
plt.yticks(range(5)) # y축 내용

plt.xlabel('x축') # x축 레이블
plt.ylabel('y축') # y축 레이블

plt.legend() # 범례
plt.savefig('data.png') # 파일 저장

plt.show()  # 그래프 보여주기