ma_tran = []
print ("nhập ma trận :")
n = int(input("nhập n:"))
for i in range(n):
    hang = []
    for j in range(n):
        so = int(input(f" phần tử [{i}][{j}]:"))
        hang.append(so)
    ma_tran.append(hang)
tong = 0
for i in range(n):
    j = n - 1 - i
    tong += ma_tran[i][j]
print(f"tổng đường chéo phụ:{tong}")