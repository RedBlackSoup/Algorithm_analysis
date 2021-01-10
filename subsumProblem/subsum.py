import sys

def subset_sum(A,k=0):
    for i in range(1,2**len(A)):
        pick=list(mask(A,bin(i)[2:]))
        if(sum(pick))==k:
            yield pick
def mask(A,m):
    em=m.zfill(len(A))
    nlist=[]
    for i,v in enumerate(em):
        if v!='0':
            nlist.append(A[i])
    return nlist
    # m=m.zfill(len(A))
    # return map(lambda x:x[0], filter(lambda x:x[1]!='0',zip(A,m)))

A=[-7,-3,-2,5,2,8]
it=subset_sum(A)
# print(list(it))
while True:
    try:
        print (next(it), end=" ")
    except StopIteration:
        sys.exit()

#     subset = []
#     str=Binary(i) #将i转换成二进制字符串
#     for word in str
#         if word is 1
#             Add the element to subset
#
#     binLst=bin(i)[2:] #bin()方法将十进制整数转换成二进制字符串，同时前加'0b'，如Bin(6)转换为'0b110'
#     binLst=binLst.zfill(len(A))# zfill()方法将返回指定长度字符串，对于位数不足的二进制字符串前补'0'