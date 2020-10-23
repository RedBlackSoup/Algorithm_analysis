import numpy as np
import matplotlib.pyplot as plt
import datetime


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


n = [1000,10000,100000,1000000,10000000]  # 排序的数组规模,分别为1k,10k,100k,1M,10M
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

plt.title('MergeSort')
plt.scatter(n, T, marker='x', color='red', s=40)
plt.plot(n, T)
plt.show()
