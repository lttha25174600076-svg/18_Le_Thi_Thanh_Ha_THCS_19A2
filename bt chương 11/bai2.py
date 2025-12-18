print("tìm từ dài hơn n")
chuoi = input("nhập chuỗi:")
n = int(input("nhập n:"))
tu_hien_tai = ""
ket_qua = []
chuoi += " "
for ky_tu in chuoi:
    if ky_tu != " ":
        tu_hien_tai += ky_tu
    else :
        if len (tu_hien_tai) > n:
            ket_qua.append(tu_hien_tai)
        tu_hien_tai = ""
print(f"các từ dài hơn {n}: {ket_qua}")