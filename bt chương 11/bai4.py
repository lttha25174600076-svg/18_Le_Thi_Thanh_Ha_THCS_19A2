print("tìm số lớn thứ hai:")
n = int(input("nhập số phàn tử:"))
danh_sach =[]
for i in range (n):
    so = int(input(f"nhập số thứ {i+1}:"))
    danh_sach.append(so)

lon_nhat = danh_sach [0]
for so in danh_sach:
    if so > lon_nhat:
        lon_nhat = so
lon_thu_hai = None
for so in danh_sach:
    if so < lon_nhat:
        if lon_thu_hai is None or so > lon_thu_hai:
            lon_thu_hai = so
if lon_thu_hai is None:
    print("không có số lớn thứ hai")
else:
    print(f"số lớn thứ hai là:{lon_thu_hai}")