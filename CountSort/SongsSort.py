import numpy as np

def countSort(A):
    Max=max(A)
    Min=min(A)
    bucket=dict()
    temp=dict()
    SA=list()
    for i in range(Min,Max+1):
        bucket[i]=0
    for x in A:
        bucket[x]+=1
    for i in range(Min,Max+1):
        if bucket[i]>0:
            SA.extend(bucket[i]*[i])
    return SA

A=[6,6,3,2,1,1,0,4]
print(countSort(A))