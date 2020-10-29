import numpy as np
import matplotlib.pyplot as plt

def judge(n,r): #n 为麦田大小  #r为采样空间y
    Take=0
    arr=np.random.rand(n)
    Max_n,Max_r=max(arr),max(arr[0:r])
    for i in arr[r:]:
        if i>Max_r:
            Take=i
            break
    return False if Take<Max_n else True
hitRate=list()
#生成1000个麦穗的稻田
n=1000 #麦穗总数
test=10000 #测试次数
for r in range(1,n):
# r 为采样空间
    hit=0 #采摘到最大麦穗的次数
    for i in range(test):
        hit+=judge(n,r)
    hitRate.append(hit/test)
    print("试验次数：",test)
    print("成功率：","{:.2f}".format(hit/test*100))

x1=np.arange(0.001,1,0.001)
y1=-x1*np.log(x1)
plt.plot(np.arange(0.001,1,0.001),hitRate,label="coding")
plt.plot(x1,y1,label="match",color="red")
plt.legend()
plt.plot()

plt.show()
