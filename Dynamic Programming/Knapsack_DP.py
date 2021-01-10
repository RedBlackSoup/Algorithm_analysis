import numpy as np
s=[3,4,5]
v=[4,5,6]
S=10
dp=np.zeros((len(s)+1,S+1))
for i in range(1,len(s)+1):
    for j in range(1, S + 1):
        if j-s[i-1]<0:
            dp[i,j]=dp[i-1,j]
        else:
            dp[i,j]=max(dp[i-1,j],dp[i-1,j-s[i-1]]+v[i-1])
print(dp)
