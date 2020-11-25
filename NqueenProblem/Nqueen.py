n = 8 # 皇后数量
queenList = [] # 记录已摆放的皇后位置[col, row]
Ans=0 # 记录解的个数


def solveNQ(row):
    global Ans
    if row >= n:  # 一行行递归棋盘 当行数超出棋盘时 说明已到最后一行 返回True
        # 既然已经结束了 就应当输出结果
        printBoard()
        Ans = Ans+1
        return False
    for col in range(n):  # 遍历这一行中的每一列
        if is_safe(row, col):
            queenList.append([row, col])
            if solveNQ(row + 1):
                return True
            else:
                queenList.remove([row, col])
    return False


def is_safe(row, col):
    flag = True
    for i in range(len(queenList)):
        x, y = queenList[i]
        if abs(x - row) == abs(y - col):
            flag = False
        if y == col:
            flag = False
    return flag

def printBoard():
    print('-' * 30)
    board = []
    for i in range(n):
        board.append([0] * n)
    for i in range(len(queenList)):
        x, y = queenList[i]
        board[x][y] = 1
    for i in range(n):
        str_board=str()
        for j in range(n):
            str_board+=" "+str(board[i][j])
        print("{0:^30}".format(str_board))

solveNQ(0)
print("")
print(n,"queen problem has",Ans,"answers")