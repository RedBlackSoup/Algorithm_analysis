import numpy as np
w=[6,6,6,6,16]
P=20 # 行长度

# badness=  (P-∑wi) ³
dp=[0]*(len(w)+1)
for i in range(1,len(w)+1):
    min=float('inf')
    for j in range(i):
        sumW=0
        for m in range(j,i):
            sumW+=w[m]
        if sumW>P:
            continue
        min=min if min<dp[j]+(P-sumW)**3 else dp[j]+(P-sumW)**3
    dp[i]=min
print(dp)