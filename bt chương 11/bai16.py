def bai16():
    print("dếm tần suất ký tự")
    chuoi = input("nhập chuỗi:")
    ky_tu_list =[]
    so_lan_list = []
    for ky_tu in chuoi:
        tim_thay = False
        for i in range (len(ky_tu_list)):
            if ky_tu_list[i] == ky_tu:
                so_lan_list[i] += 1
                tim_thay = True
                break
        if not tim_thay:
            ky_tu_list.append(ky_tu)
            so_lan_list.append(1)
    print("tần suất xuất hiện:")
    for i in range(len(ky_tu_list)):
        print(f"'{ky_tu_list[i]}:{so_lan_list[i]}")
if __name__=="__main__":
    bai16()
    
