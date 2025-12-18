def bai15():
    print("tách tuple chẵn lẻ")
    n = int(input("nhập số phần tử:"))
    danh_sach = []
    for i in range(n):
        so = int(input(f"nhập số thứ {i+1}:"))
        danh_sach.append(so)
    tup_ban_dau = tuple(danh_sach)
    chan = []
    le = []
    for so in tup_ban_dau:
        if so % 2 == 0:
            chan.append(so)
        else:
            le.append(so)
    tong_chan = 0
    for so in chan :
        tong_chan += so
    tong_le = 0
    for so in le :
        tong_le += so
    tup_chan = tuple(chan)
    tup_le = tuple(le)
    print(f"Tuple ban đầu: {tup_ban_dau}")
    print(f"Tuple số chẵn : {tup_chan}, tổng = {tong_chan}")
    print(f"Tuple số lẻ:{tup_le}, tổng = {tong_le}")
if __name__ =="__main__":
    bai15()
