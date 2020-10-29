import numpy as np
import matplotlib.pyplot as plt
import datetime

times=0

def binary_search(A, k):
    first = 0
    last = len(A)-1
    found = False
    while first<=last and not found:
        global times
        times+=1
        midpoint = (first + last)//2
        if A[midpoint] == k:
            found = True
        else:
            if k < A[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

def linear_search(A,k):
    found=False
    for x in A:
        if x==k:
            found=True
            break
    return found


n=[1000,10000,100000,1000000,10000000] #查找的数组规模,分别为1k,10k,100k,1M,10M
# n=np.arange(100000,10000000,100000)
T=list()#记录搜索所用的时间
for i in n:
    print(i)
    #生成的数组和目标数,共1000对
    arrlist=list()
    aimlist=list()
    #时间差
    dT=0
    for j in range(100):
        #生成随机数组,范围为0-10M,并对数组排序
        arr=np.random.randint(i,size=i)
        # arr=np.random.rand(i)
        arr.sort()
        arrlist.append(arr)
        #生成目标数
        aim=np.random.randint(1,i)
        # aim=np.random.rand(1)
        aimlist.append(aim)
    # 二分搜索开始时间
    sT = datetime.datetime.now()
    for (arr,aim) in zip(arrlist,aimlist):
        #二分搜索
        binary_search(arr,aim)
        #直接搜索
        # linear_search(arr, aim)
    # 二分搜索结束时间
    eT = datetime.datetime.now()
    # 计算时间差
    dT += (eT - sT).total_seconds()
    T.append(times/100)
    times=0



print(n)
print(T)
z1=np.polyfit(np.log(n),T,1)
x=np.arange(1, 10000000, 1)
y =z1[0]*np.log(x)+z1[1]
plt.title('Search_Analysis')
plt.scatter(n, T, marker = 'x',color = 'red', s = 40 ,label='Binary')
plt.legend()
plt.plot(x,y)
plt.show()

# z2 = np.polyfit(n, T, 1)
# p2 = np.poly1d(z2)
# yvals2=p2(n)
# plt.scatter(n, T, marker = 'x',color = 'blue', s = 40 ,label='linear')
# plt.plot(n, yvals2)