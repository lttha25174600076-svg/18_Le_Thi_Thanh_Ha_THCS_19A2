print("xóa khoảng trắng thừa")
chuoi = input("nhập chuỗi:")
ket_qua = ""
co_khoang_trang = False
for ky_tu in chuoi :
    if ky_tu != " ":
        if co_khoang_trang :
            ket_qua += " "
            co_khoang_trang = False
        ket_qua += ky_tu
    else:
        co_khoang_trang = True
print(f"chuỗi sau khi xử lý:'{ket_qua}'")