print("dịch chuyển list")
n = int(input("nhập số phần tử :"))
danh_sach = []
for i in range(n):
    phan_tu = input(f"nhập phần tử thứ {i+1}:")
    danh_sach.append(phan_tu)
k = int(input("nhập số vị trí dịch chuyển:"))
ket_qua = [""] * n
for i in range(n):
    vi_tri_moi = (i + k) % n
    ket_qua[vi_tri_moi] = danh_sach[i]
print(f"list sau khi dịch {k} vị trí:{ket_qua}")