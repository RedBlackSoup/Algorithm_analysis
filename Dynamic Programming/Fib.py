# 楼梯问题，每次只能走1格或者2格，10阶楼梯有几种走法
# 本质上是斐波那契数列

def Fib_1(n):
    if n == 1:
        return 1
    if n==2:
        return 2
    return Fib_1(n-1)+Fib_1(n-2)
# 复杂度为O(2^n)
print(Fib_1(10))

memo={}
def Fib_2(n):
    if n in memo:
        return memo[n]
    else:
        if n<=2:
            f=n
        else:
            f=Fib_2(n-1)+Fib_2(n-2)
        memo[n]=f
    return memo[n]
print(Fib_2(10))

def Fib_3(n):
    dp=[0]*n
    for k in range(n):
        if k<=1:
            dp[k]=k+1
        else:
            dp[k]=dp[k-1]+dp[k-2]
    return dp

print(Fib_3(10))