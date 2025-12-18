print("hàng có tổng lớn nhất")
dong = int(input("nhập số dòng :"))
cot = int(input("nhập số cột"))
ma_tran = []
print("nhập ma trận:")
for i in range(dong):
    hang =[]
    for j in range(cot):
        so = int(input(f"phần tử [{i}][{j}]:"))
        hang.append(so)
    ma_tran.append(hang)
hang_max = 0
tong_max = 0
for i in range(dong):
    tong_hang = 0
    for j in range(cot):
        tong_hang += ma_tran[i][j]
    if i == 0 or tong_hang > tong_max :
        tong_max = tong_hang
        hang_max = i
print(f"hàng{hang_max} có tổng lớn nhất:{tong_max}")
print(f"các phần tử hàng {hang_max}:{ma_tran[hang_max]}")
