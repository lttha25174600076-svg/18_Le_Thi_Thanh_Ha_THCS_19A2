print("tìm cặp số có tổng bằng X")
n = int(input("nhập số phần tử:"))
danh_sach = []
for i in range(n):
    so = int(input(f"nhập số thứ {i + 1}:"))
    danh_sach.append(so)
x = int(input("nhập giá trị X :"))
cac_cap = []
for i in range(n):
    for j in range (i+1,n):
        if danh_sach[i] + danh_sach[j] == x:
            cac_cap.append((danh_sach[i],danh_sach[j]))
print(f"các cặp số có tổng bằng {x}:{cac_cap}")