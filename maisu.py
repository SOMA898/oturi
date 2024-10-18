x = int(input("購入する商品の金額を入れて下さい"))
n = int(input("払うお金を入力してください"))

oturi_all = n - x

#自販機内の硬貨の枚数(入力した分を含まない)
yen_500 = 10
yen_100 = 10
yen_50 = 10
yen_10 = 10

#上から500,100,50,10円の順でおつりの計算
if oturi_all % 500 != 0:
    amari = oturi_all % 500
    oturi_500 = oturi_all//500
    yen_500 = yen_500 - oturi_all//500
elif oturi_all % 500 == 0:
    amari = 0
    oturi_500 = oturi_all//500
    yen_500 = yen_500 - oturi_all//500

if amari % 100 != 0:
    oturi_100 = amari//100
    yen_100 = yen_100 - amari//100
    amari = amari % 100
elif amari % 100 == 0:
    oturi_100 = amari//100
    yen_100 = yen_100 - amari//100
    amari = 0

if amari % 50 != 0:
    oturi_50 = amari//50
    yen_50 = yen_50 - amari//50
    amari = amari % 50
elif amari % 50 == 0:
    oturi_50 = amari//50
    yen_50 = yen_50 - amari//50
    amari = 0

if amari % 10 != 0:
    oturi_10 = amari//10
    yen_10 = yen_10 - amari//10
    amari = amari % 10
elif amari % 10 == 0:
    oturi_10 = amari//10
    yen_10 = yen_10 - amari//10

print("--------------------------------------")

print("おつりの合計は%d円です" %oturi_all)
print("500円は%d枚" %oturi_500)
print("100円は%d枚" %oturi_100)
print("50円は%d枚" %oturi_50)
print("10円は%d枚" %oturi_10)

print("--------------------------------------")

print("自販機内の硬貨の枚数です")
print("500円は%d枚" %yen_500)
print("100円は%d枚" %yen_100)
print("50円は%d枚" %yen_50)
print("10円は%d枚" %yen_10)

print("--------------------------------------")