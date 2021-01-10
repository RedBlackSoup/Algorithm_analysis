# 最短路径问题的dp实现
import numpy as np
v=8 # 节点个数
# 先拓扑排序
graph={
    'S':{'A':5,'B':3},
    "A":{'C':7,'D':4},
    'B':{'C':2,'D':8},
    'C':{'E':5,'F':11},
    'D':{'C':7,'E':10,'F':6},
    'E':{'G':1},
    'F':{'E':3,'G':5},
    'G':{}
}
in_degrees = dict((u,0) for u in graph)
for u in graph.values():
        for v in u.keys():
            in_degrees[v] += 1
# Q为入度为0的节点
Q = [u for u in in_degrees if in_degrees[u] == 0]
Seq=[]
while Q:
    u=Q.pop()
    Seq.append(u)
    for v in graph[u].keys():
        in_degrees[v] -= 1
        if in_degrees[v] ==0:
            Q.append(v)

dp={}
dpInfo={}
# 倒序遍历
for v in Seq[::-1]:
    if v=='G':
        dp[v]=0
    else:
        # 到达节点v 的点
        min=float('inf')
        info=str()
        for w in graph[v].keys():
            if dp[w]+graph[v][w]<=min:
                min=dp[w]+graph[v][w]
                info=w
        dp[v]=min
        dpInfo[v]=info

print(dp['S'])
result=str()
node='S'
while node:
    result+=node
    node=dpInfo.get(node,0)
print(result)