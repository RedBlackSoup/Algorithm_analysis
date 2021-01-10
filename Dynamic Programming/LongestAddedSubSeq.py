A=[18,17,19,6,11,21,23,15]
def DP(A):
    A.insert(0,-float('inf'))
    dp=[0]*len(A)
    dp[0]=0
    for i in range(1,len(A)):
        Max=0
        for j in range(i):
            if A[j]<=A[i] and dp[j]+1>Max:
                Max=dp[j]+1
        dp[i] = Max
    return max(dp)

def printResult(A):
    print("测试样例：",A)
    print("输出的最长递增子序列长度：",DP(A))
    print("预期结果:",4)