import random

def main():
    # 初始化节点，边
    edge = list()
    result = list()
    node = [[i] for i in range(8)]
    initMap(edge)
    # 设置最小值
    min = len(edge)
    # 随机算法 进行56次测试
    for i in range(56):
        while (1):
            # 随机找一条边，返回其两个端点
            index = random.randint(0, len(edge) - 1)
            A, B = edge[index]
            mergeNode(A, B, edge, node)
            if len(node) <= 2:
                break
        if len(edge) <= min:
            result = edge
            min = len(edge)
        # 重新初始化edge和node
        edge = list()
        initMap(edge)
        node = [[i] for i in range(8)]
    # 输出结果
    print(result)

def initMap(edge: list):
    addEdge(0, 1, edge)
    addEdge(0, 2, edge)
    addEdge(0, 3, edge)
    addEdge(1, 2, edge)
    addEdge(1, 3, edge)
    addEdge(2, 3, edge)
    addEdge(3, 4, edge)
    addEdge(3, 5, edge)
    addEdge(4, 5, edge)
    addEdge(4, 6, edge)
    addEdge(4, 7, edge)
    addEdge(5, 6, edge)
    addEdge(5, 7, edge)
    addEdge(6, 7, edge)
    return edge

# 删去B，添加到A中
def mergeNode(A, B, edge, node):
    # node表匹配
    A = matchNode(node, A)
    B = matchNode(node, B)
    # edge中删除对应边
    for i in A:
        for j in B:
            if (i, j) in edge:
                edge.remove((i, j))
            elif (j, i) in edge:
                edge.remove((j, i))
    # node 表修改
    transNode(node, A, B)

def addEdge(A, B, edge):
    if A > B:
        edge.append((B, A))
    elif B > A:
        edge.append((A, B))

def matchNode(mergeList, A):
    for i in mergeList:
        if A in i:
            return i

def transNode(mergeList, A, B):
    A.extend(B)
    mergeList.remove(B)

if __name__ == "__main__":
    main()
