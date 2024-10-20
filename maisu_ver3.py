x = int(input("購入する商品の金額を入れて下さい"))
n = int(input("払うお金を入れてください"))

while x > n:
    if x > n:
        n1 = x - n
        n1 = int(input("金額が不足しています あと%d円入れてください" %n1))
        n += n1
    else:
        break

value_yen = [500,100,50,10]
num_yen = [10,10,10,10]
oturi_yen = [0]*4

oturi_all= n - x

print("--------------------------------------")

print("おつりの合計は%d円です" %oturi_all)

for i in range(4):
    #上から500,100,50,10円の順でおつりの計算
    if oturi_all % value_yen[i] != 0:
        oturi_yen[i] = oturi_all//value_yen[i]
        num_yen[i] = num_yen[i] - oturi_all//value_yen[i]
        oturi_all = oturi_all % value_yen[i]
    elif oturi_all % value_yen[i] == 0:
        oturi_yen[i] = oturi_all//value_yen[i]
        num_yen[i] = num_yen[i] - oturi_all//value_yen[i]
        oturi_all = 0

for i in range(4):
    print(f"{value_yen[i]}円は{oturi_yen[i]}枚" )

print("--------------------------------------")

print("自販機内の硬貨の枚数です")
for i in range(4):
    print(f"{value_yen[i]}円は{num_yen[i]}枚" )

print("--------------------------------------")