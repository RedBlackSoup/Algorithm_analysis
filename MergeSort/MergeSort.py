import numpy as np
import matplotlib.pyplot as plt
import datetime
from scipy.optimize import curve_fit


def MergeSort(A):
    if len(A) <= 1:
        return A
    else:
        mid = len(A) // 2
        LA = A[:mid]
        RA = A[mid:]
        SLA = MergeSort(LA)
        SRA = MergeSort(RA)
        SA = Merge(SLA, SRA)
        return SA


def Merge(L, R):
    A = []
    left = 0
    right = 0
    # Merge
    while left < len(L) and right < len(R):
        if L[left] < R[right]:
            A.append(L[left])
            left += 1
        else:
            A.append(R[right])
            right += 1
    # copy the rest of L or R
    if left >= len(L):
        A.extend(R[right:])
    else:
        A.extend(L[left:])
    return A


def func(x, a, b, c):
    return a * x * np.log(x) + b * np.log(x) + c


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
        arr = MergeSort(arr)
        # 结束时间
        eT = datetime.datetime.now()
        # 计算时间差
        dT += (eT - sT).total_seconds()
    T.append(dT)

popt, pcov = curve_fit(func, n, T)  # 进行参数拟合
plt.title('MergeSort')
plt.scatter(n, T, marker='x', color='red', s=40)
plt.plot(n, func(n, *popt), label='f(x) = n*log(n)')
plt.legend()
plt.show()

# 伪代码部分
# def mergesort(A):
#     # divide the array A into subarray L and R
#     mergesort(L)
#     mergesort(R)
#     return merge(L,R)
#
# def merge(L, R):
#     #define the pos in array L and R
#     while posL < len(L) and posR < len(R):
#         if L[posL] < R[posR]:
#             add the element into sequence A
#             posL forward
#         else:
#             add the element into sequence A
#             posR forward
#     # copy the rest of L or R to A
#     return A