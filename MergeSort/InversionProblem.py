def Cont_Inv(A):
    if len(A) <= 1:
        return A,0
    else:
        mid = len(A) // 2
        LA = A[:mid]
        RA = A[mid:]
        SLA,a = Cont_Inv(LA)
        SRA,b = Cont_Inv(RA)
        SA,c = Cross(SLA, SRA)
        return SA,a+b+c


def Cross(L, R):
    A = []
    left = 0
    right = 0
    count=0
    # Merge
    while left < len(L) and right < len(R):
        if L[left] < R[right]: # 非逆序
            A.append(L[left])
            left += 1
        else: # 逆序情况
            A.append(R[right])
            #增加当前L[left]及其后续元素个数的逆序数
            count+=len((L[left:]))
            right += 1
    # copy the rest 不存在比较，不需要计入逆序数
    if left >= len(L):
        A.extend(R[right:])
    else:
        A.extend(L[left:])
    return A, count

A=[1,3,2,5,6,4]
SA, result=Cont_Inv(A)
print(result)