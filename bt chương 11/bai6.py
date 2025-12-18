print ("tổng chẵn , tổng lẻ")
n = int(input("nhập số phần tử:"))
danh_sach = []
for i in range(n):
    so = int(input(f"nhập số thứ {i + 1}:"))
    danh_sach.append(so)
tong_chan = 0
tong_le = 0
for so in danh_sach :
    if so % 2 == 0:
        tong_chan += so
    else:
        tong_le += so
print(f"tổng số chẵn:{tong_chan}")
print(f"tổng số lẻ:{tong_le}")
