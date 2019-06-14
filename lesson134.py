# subplot()

import matplotlib.pyplot as plt

plt.subplot(1,2,1)
plt.plot(range(10,100),'g')

plt.subplot(1,2,2)
plt.plot(range(100,1,-1),'r')

plt.show()  # 그래프 보여주기