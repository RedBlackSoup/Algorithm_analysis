import numpy

class Multiple_KP:
    def __init__(self):
        self.I = 12
        self.P = [10, 12, 15, 8, 7, 14, 16, 2, 6, 13, 15, 9, 7]
        self.W = [5, 8, 7, 6, 4, 5, 8, 1, 3, 4, 6, 3, 3]
        self.K = 3
        self.Knapsacks = [15, 10, 5]

    def printAll(self):
        print("Items Number: ", self.I)
        for i in range(self.I):
            print(self.P[i]," $ -- ",self.W[i]," kg")
        print("Knapsack Number: ",self.K)
        for i in range(self.K):
            print("Size: ",self.Knapsacks[i]," kg")
    def load_test(self,index='A'):
        with open('Test.txt', 'r') as f:
            line = f.readline()
            Parament=[]
            while line:
                str=line.rstrip('\n')
                if str == index:
                    for i in range(5):
                        list_str=f.readline().rstrip('\n').split(" ")
                        lst=[]
                        for n in list_str:
                            lst.append(int(n))
                        Parament.append(lst)
                line = f.readline()
            if Parament != None:
                self.I = Parament[0][0]
                self.P = Parament[1]
                self.W = Parament[2]
                self.K = Parament[3][0]
                self.Knapsacks = Parament[4]

    def Greedy_Algorithm(self):
        Rest = self.Knapsacks.copy()
        X = [None] * self.I  # 背包
        B = []
        for i in range(self.I):
            B.append((i, self.P[i] / self.W[i]))
        # 性价比排序
        B.sort(key=lambda x: x[1], reverse=True)
        w = 0
        for item in B:
            # 余下最多->找最大 index 表示余量最大的背包序号
            index = 0
            Max = 0
            for i in range(len(Rest)):
                if Rest[i] > Max:
                    index = i
                    Max = Rest[i]
            if Rest[index] > self.W[item[0]]:
                # 加入背包 index 表示背包号
                X[item[0]] = index
                Rest[index] -= self.W[item[0]]
        # 根据 X 输出价值
        Z = self.Cal_value(X)
        print("Greed Algorithm")
        print("Choose: ", X)
        print("Value: ", Z)
        print("RestWeight: ", Rest)

    def Rotate(self, X, i, j, k):
        Temp = X[i]
        X[i] = X[j]
        X[j] = X[k]
        X[k] = Temp
        return X

    def Weight_Fes(self, X):
        Rest = self.Knapsacks.copy()
        flag = True
        for i in range(self.I):
            if X[i] != None:
                Rest[X[i]] -= self.W[i]
        for i in Rest:
            if i < 0:
                flag = False
        return flag

    def Cal_value(self, X):
        temp = 0
        for i in range(self.I):
            if X[i] != None:
                temp += self.P[i]
        return temp

    def Neighbor_Serch(self):
        X = [None] * self.I  # 背包
        Next = []
        count = 0
        while (1):
            # 计算当前价值
            Z_now = self.Cal_value(X)
            # 打印信息
            print("Iteration ", count)
            print("The resolution is ", X)
            print("The value is ", Z_now)

            # 根据X 来计算 背包剩余空间
            Rest = self.Knapsacks.copy()
            for i in range(self.I):
                if X[i] != None:
                    Rest[X[i]] -= self.W[i]
            print("RestWeight: ", Rest)
            # 开始迭代
            count += 1
            # 邻域集合
            Neighbor = []

            # 计算邻域 N(x)
            # I -> item | K -> knapsack
            # 1. 检查是否全放进去了
            Isall = True
            for i in range(self.I):
                if X[i] == None:
                    Isall = False
                    break
            # 2. 添加情况
            Isput = False
            for i in range(self.I):
                Nx = X.copy()
                Ischange = False
                for j in range(self.K):
                    if Rest[j] > self.W[i] and Nx[i] == None:
                        # 放进去
                        Isput = True
                        Ischange = True
                        Nx[i] = j
                        break
                # put i in knapsack
                if Ischange:
                    # 计算价值
                    Z = 0
                    for i in range(self.I):
                        if Nx[i] != None:
                            Z += self.P[i]
                    # 打包进邻域
                    Neighbor.append((Z, Nx))

            # 3. 轮转情况
            if Isput == False and Isall == False:
                print("------------------- begin rotate! -------------------")
                for i in range(self.I):
                    for j in range(self.I):
                        for k in range(self.I):
                            if Nx[i] == None and Nx[j] != Nx[k] and Nx[j] != None and Nx[k] != None:
                                Result = self.Rotate(Nx.copy(), i, j, k)
                                if self.Weight_Fes(Result):
                                    Neighbor.append((self.Cal_value(Result), Result))
            # 邻域排序
            Neighbor.sort(key=lambda x: x[0], reverse=True)
            print(Neighbor)
            # 邻域更新
            # 选择第一位
            if len(Neighbor):
                Next = Neighbor[0][1]
            else:
                print("No Neighbor, Break Out")
                break
            # 跳出循环
            if Neighbor[0][0] <= Z_now or Neighbor == None:
                # 打印信息
                print("-" * 20, " NeighborSearch's solution ", "-" * 20)
                print("The solution is ", X)
                print("The value is ", Z_now)
                break
            else:
                # 更新 X
                X = Next

    def Tabu_Search(self):
        X = [None] * self.I  # 背包
        Next = []
        count = 0
        Tabu = []
        Track=[]
        while (count<15):
            # 计算当前价值
            Z_now = self.Cal_value(X)
            # 打印信息
            print("Iteration ", count)
            print("The resolution is ", X)
            print("The value is ", Z_now)
            # 添加记录
            Track.append((Z_now,X))
            # 根据X 来计算 背包剩余空间
            Rest = self.Knapsacks.copy()
            for i in range(self.I):
                if X[i] != None:
                    Rest[X[i]] -= self.W[i]
            print("RestWeight: ", Rest)
            # 开始迭代
            count += 1
            # 邻域集合
            Neighbor = []

            # 计算邻域 N(x)
            # I -> item | K -> knapsack
            # 1. 检查是否全放进去了
            Isall = True
            for i in range(self.I):
                if X[i] == None:
                    Isall = False
                    break
            # 2. 添加情况
            Isput = False
            for i in range(self.I):
                Nx = X.copy()
                Ischange = False
                for j in range(self.K):
                    if Rest[j] > self.W[i] and Nx[i] == None:
                        # 放进去
                        Isput = True
                        Ischange = True
                        Nx[i] = j
                        break
                # put i in knapsack
                if Ischange:
                    # 计算价值
                    Z = 0
                    for i in range(self.I):
                        if Nx[i] != None:
                            Z += self.P[i]
                    # 打包进邻域
                    Neighbor.append((Z, Nx))

            # 3. 轮转情况
            if Isput == False and Isall == False:
                for i in range(self.I):
                    for j in range(self.I):
                        for k in range(self.I):
                            if Nx[i] == None and Nx[j] != Nx[k] and Nx[j] != None and Nx[k] != None:
                                Result = self.Rotate(Nx.copy(), i, j, k)
                                if self.Weight_Fes(Result):
                                    Neighbor.append((self.Cal_value(Result), Result))
            # 邻域排序
            Neighbor.sort(key=lambda x: x[0], reverse=True)
            # print(Neighbor)
            # 邻域更新
            # 选择第一位(检测 Tabu)
            for neighbor in Neighbor:
                # 检测是否Tabu
                if neighbor[1] not in Tabu:
                    Next = neighbor[1]
                    break
            # 更新 X 和 Tabu
            if len(Tabu) > 4:
                Tabu.pop(0)
            Tabu.append(X)
            X = Next
        # 根据Track 输出最好结果
        Track.sort(key=lambda x:x[0],reverse=True)
        print("-"*50)
        print("Tabu Search's optimalist solution: ")
        print("Solution is: ", Track[0][1])
        print("Value is: ", Track[0][0])

Test = Multiple_KP()

Test.load_test('A')
Test.printAll()
Test.Tabu_Search()

