print("đếm kí tự")
chuoi = input("nhập chuỗi:")
dem_chu = 0
dem_so = 0
dem_db = 0
for ky_tu in chuoi :
    if ('a' <= ky_tu <= 'z') or ('A' <= ky_tu <= 'z'):
        dem_chu += 1
    elif '0' <= ky_tu <= '9':
        dem_so += 1
    else :
        dem_db += 1
print(f"chữ cái :{dem_chu}")
print(f"chữ số:{dem_so}")
print(f"ký tự đặc biệt:{dem_db}")