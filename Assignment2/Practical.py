import numpy as np
import matplotlib.pyplot as plt
import datetime
from scipy.optimize import curve_fit


def MergeSort(A):
    if len(A) <= 1:
        return A, 0
    else:
        mid = len(A) // 2
        LA = A[:mid]
        RA = A[mid:]
        SLA, SLcont = MergeSort(LA)
        SRA, SRcont = MergeSort(RA)
        SA, MergeCont = Merge(SLA, SRA)
        Count = SLcont + SRcont + MergeCont
        return SA, Count


def Merge(L, R):
    A = []
    left = 0
    right = 0
    Count = 0
    # Merge
    while left < len(L) and right < len(R):
        if L[left] < R[right]:  # 基本单位
            A.append(L[left])
            left += 1
        else:
            A.append(R[right])
            right += 1
        Count += 1
    # copy the rest of L or R
    if left >= len(L):
        A.extend(R[right:])
    else:
        A.extend(L[left:])
    return A, Count


def BubbleSort(A):
    Count = 0
    for i in range(len(A) - 1):
        Flag = True
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:  # 逆序 进行交换
                temp = A[j + 1]
                A[j + 1] = A[j]
                A[j] = temp
                Count += 1
                Flag = False
        if Flag is True:
            break
    return A, Count


n = np.array([1000, 2000,3000,4000,5000,6000,7000,8000,9000,10000])  # 排序的数组规模,分别为10k,100k,1M,10M
Count = list()  # 记录排序所用次数
T = list()  # 记录排序所用时间
for i in n:
    print(i)
    # 时间差
    dT = 0
    dtime = []
    for j in range(10):
        # 开始时间
        sT = datetime.datetime.now()
        # 生成随机数组,范围为0-10M.
        arr = np.random.randint(i, size=i)
        arr, count = BubbleSort(arr)
        dtime.append(count)
        # 结束时间
        eT = datetime.datetime.now()
        # 计算时间差
        dT += (eT - sT).total_seconds()
    Count.append(np.mean(dtime))
    T.append(dT)

for i in range(len(n)):
    print("The size of data: ",n[i])
    print("The c is: ",Count[i])
    print("The actual time is: ",T[i])

# def func(x, a, b, c):
#     return a * x * np.log(x) + b * np.log(x) + c
#
# plt.figure(1)
# plt.subplot(1, 2, 1) #图一包含1行2列子图，当前画在第一行第一列图上
# popt, pcov = curve_fit(func, n, T_Merge)  # 进行参数拟合
# plt.title('MergeSort')
# plt.scatter(n, T_Merge, marker='x', color='red', s=40)
# plt.plot(n, func(n, *popt), label='f(n) = n*log(n)')
# plt.legend()
#
# plt.figure(1)
# plt.subplot(1, 2, 2)#当前画在第一行第2列图上
# popt, pcov = curve_fit(func, n, Count_Merge)  # 进行参数拟合
# plt.title('MergeSort')
# plt.scatter(n, Count_Merge, marker='x', color='red', s=40)
# plt.plot(n, func(n, *popt), label='f(n) = n*log(n)')
# plt.legend()

plt.figure(1)
plt.subplot(1, 2, 1) #图一包含1行2列子图，当前画在第一行第一列图上

z1 = np.polyfit(n, T, 2) # n表示用n次多项式进行拟合，只返回多项式系数
p1 = np.poly1d(z1)
x1=np.arange(1, 10000, 1)
y1 =z1[0]*x1*x1+z1[1]*x1+z1[2]
plt.title('Time')
plt.scatter(n, T, marker='x', color='red', s=40)

plt.plot(x1,y1, label='f(n) = n²')
plt.legend()

plt.figure(1)
plt.subplot(1, 2, 2)#当前画在第一行第2列图上


z2 = np.polyfit(n, Count, 2) # n表示用n次多项式进行拟合，只返回多项式系数
p2 = np.poly1d(z2)
x2=np.arange(1, 10000, 1)
y2 =z2[0]*x2*x2+z2[1]*x2+z2[2]

plt.title('Count')
plt.scatter(n, Count, marker='x', color='red', s=40)
plt.plot(x2,y2, label='f(n) = n²')
plt.legend()

plt.show()


# # Bubble Sort 伪代码
# def BubbleSort(A):
#     for i from 0 to N-1:
#         for j from 0 to N-1-i:
#             if A[j] > A[j + 1]:
#             # switch A[j] and A[j+1]
#     return A