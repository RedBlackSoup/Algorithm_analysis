import numpy

I = 9
P = [10, 5, 3, 8, 7, 14, 16, 2, 6]
W = [5, 8, 7, 6, 4, 5, 8, 1, 3]
Weight = 20


def Greedy_Algorithm():
    X = [0] * I  # 背包
    B = []
    for i in range(I):
        B.append((i, P[i] / W[i]))

    B.sort(key=lambda x: x[1], reverse=True)
    w = 0
    for item in B:
        # 不超过总重
        if w + W[item[0]] < Weight:
            # 加入背包
            X[item[0]] = 1
            w += W[item[0]]

    # 根据 X 输出价值
    Z = 0
    for i in range(I):
        Z += X[i] * P[i]
    print("Greed Algorithm")
    print("Choose: ", X)
    print("Value: ", Z)
    print("Weight: ", w)

def Neighbor_Serch():
    X = [0] * I  # 背包
    count=0
    while (1):
        count+=1
        Neighbor = []
        # 计算当前价值
        Z_now = 0
        for i in range(I):
            Z_now += X[i] * P[i]


        for i in range(I):
            Nx = X.copy()
            if X[i] == 0:
                Nx[i] = 1
            else:
                Nx[i] = 0
            w = 0
            Z = 0
            feasible = True
            for j in range(I):
                Z += Nx[j] * P[j]
                w += Nx[j] * W[j]
            if w > Weight:
                feasible = False
            Neighbor.append((feasible, Z, Nx))

        neighbor_fea = []
        neighbor_inf = []
        for n in Neighbor:
            if n[0] == True:
                neighbor_fea.append(n)
            else:
                neighbor_inf.append(n)
        # 领域排序 根据价值
        neighbor_fea.sort(key=lambda x: x[1], reverse=True)
        neighbor_inf.sort(key=lambda x: x[1], reverse=True)
        Neighbor = neighbor_fea + neighbor_inf

        print("Iteration ",count)
        print("The resolution is ",X)
        print("The value is ",Z_now)

        # 选择第一位
        Next = Neighbor[0][2]
        # 跳出循环
        if Neighbor[0][1] <= Z_now:
            break
        else:
            # 更新 X
            X = Next

def Tabu_Serch():
    X = [0] * I  # 背包
    Next = []
    count=0
    Tabu=[]
    Track=[]
    while (count<15):

        count+=1
        Neighbor = []
        # 计算当前价值
        Z_now = 0
        for i in range(I):
            Z_now += X[i] * P[i]
        # 判断邻域
        for i in range(I):
            Nx = X.copy()
            if X[i] == 0:
                Nx[i] = 1
            else:
                Nx[i] = 0
            w = 0
            Z = 0
            feasible = True
            for j in range(I):
                Z += Nx[j] * P[j]
                w += Nx[j] * W[j]
            if w > Weight:
                feasible = False
            Neighbor.append((feasible, Z, Nx))

        neighbor_fea = []
        neighbor_inf = []
        for n in Neighbor:
            if n[0] == True:
                neighbor_fea.append(n)
            else:
                neighbor_inf.append(n)
        # 领域排序 根据价值
        neighbor_fea.sort(key=lambda x: x[1], reverse=True)
        neighbor_inf.sort(key=lambda x: x[1], reverse=True)
        Neighbor = neighbor_fea + neighbor_inf

        print("Ite. ",count)
        print("The resolution is ",X)
        print("The value is ",Z_now)

        # 选择下一solution
        for neighbor in Neighbor:
            # 检测是否Tabu
            if neighbor[2] not in Tabu:
                Next = neighbor[2]
                break
        # 更新 X 和 Tabu
        if len(Tabu)>0:
            Tabu.pop(0)
        Tabu.append(X)
        X = Next

Tabu_Serch()