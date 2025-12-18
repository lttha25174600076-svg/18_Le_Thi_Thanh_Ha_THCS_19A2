print("kiểm tra ma trận đối xứng")
n = int(input("nhập kích thước ma trận (n x n):"))
ma_tran = []
print("nhập ma trận:")
for i in range(n):
    hang = []
    for j in range(n):
        so = int(input(f"phần tử [{i}][{j}]:"))
        hang.append(hang)
    ma_tran.append(hang)
la_doi_xung = True
for i in range(n):
    for j in range(n):
        if ma_tran[i][j] != ma_tran[j][i]:
            la_doi_xung= False
            break
    if not la_doi_xung:
        break
if la_doi_xung:
    print("ma trận này là ma trận đối xứng")
else:
    print("ma trận này không phải là ma trận đối xứng")

