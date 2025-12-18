print("loại bỏ trùng lặp")
n = int(input("nhập số phân tử:"))
danh_sach = []
for i in range (n):
    phan_tu = input(f"nhập số phần tử thứ {i+1}:")
    danh_sach.append(phan_tu)
ket_qua = []
for phan_tu in danh_sach:
    da_co = False
    for item in ket_qua:
        if item in ket_qua:
            da_co = True
            break
    if not da_co :
        ket_qua.append(phan_tu)
print(f"danh sách sau khi loại bỏ trùng :{ket_qua}")