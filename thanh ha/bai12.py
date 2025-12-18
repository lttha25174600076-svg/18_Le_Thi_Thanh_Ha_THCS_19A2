def nhan_ma_tran(A,B):
    n = len(A)
    m = len(B[0])
    p = len(B)
    C = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(p):
                C[i][j] += A[i][k] * B[k][j]
    return C
A = [[1,2], [3,4]]
B = [[5,6],[7,8]]
if len(A[0]) != len(B):
    print("không nhân được")
else:
    print(nhan_ma_tran(A,B))