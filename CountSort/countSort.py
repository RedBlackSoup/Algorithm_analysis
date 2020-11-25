import numpy as np
import matplotlib.pyplot as plt
import datetime
from scipy.optimize import curve_fit

def countSort(A):
    Max=max(A)
    Min=min(A)
    bucket=dict()
    SA=list()
    for i in range(Min,Max+1):
        bucket[i]=0
    for x in A:
        bucket[x]+=1
    for i in range(Min,Max+1):
        if bucket[i]>0:
            SA.extend(bucket[i]*[i])
    return SA

def StableCoutSort(A):
    Max=max(A)
    Min=min(A)
    bucket=dict.fromkeys(range(Min,Max+1),0)
    temp=bucket.copy()
    SA=[0]*len(A)
    for i in A:
        # bucket[i]+=1
        bucket[i]=bucket.get(i,0)+1
    for i in range(Min,Max+1):
        temp[i]=bucket[i]+temp.get(i-1,0)
        # if i==Min:
        #     temp[i]=bucket[i]
        # else:
        #     temp[i]=bucket[i]+temp[i-1]
    for i in reversed(A):
        if temp[i]>-1:
            temp[i]-=1
            SA[temp[i]]=i
    return SA

n = np.array([1000, 10000, 100000, 1000000, 10000000])  # 排序的数组规模,分别为1k,10k,100k,1M,10M
T = list()  # 记录排序所用时间
for i in n:
    print(i)
    # 时间差
    dT = 0
    for j in range(10):
        # 生成随机数组,范围为0-10M.
        arr = np.random.randint(i, size=i)
        # 开始时间
        sT = datetime.datetime.now()
        arr = StableCoutSort(arr)
        # 结束时间
        eT = datetime.datetime.now()
        # 计算时间差
        dT += (eT - sT).total_seconds()
    T.append(dT)

print(n)
print(T)
z1 = np.polyfit(n, T, 1)
x = np.arange(1, 10000000, 1)
y = z1[0] * x + z1[1]
plt.title('CountSort')
plt.scatter(n, T, marker='x', color='red', s=40)
plt.plot(x, y)
plt.show()

# StableCoutSort(A):
# # define bucket, count as hash list
#     for i in A:
#         bucket[i] = the number of elements of A
#     for i in range(Min,Max+1):
#         count[i] = the index of i in result
#     for i in reversed(A):
#         count[i] -= 1
#         SA[count[i]] = i
#     return SA
