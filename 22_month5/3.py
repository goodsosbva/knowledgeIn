# 50km 미만 : 3500원, 50~100km 미만 : 4000원, 100~300km 미만 : 4500원
#
# - 300~500km 미만 : 5000원, 500km 이상 : 6000원
#
# - 5km 미만은 서비스 하지 않음

while True:
    km = int(input("배송 거리 입력(km): "))


    if km > 500:
        print("배송료:", 6000)

    elif 500 > km > 300:
        print("배송료:", 5000)

    elif 300 > km > 100:
        print("배송료:", 4500)

    elif 100 > km > 50:
        print("배송료:", 4500)

    elif 50 > km > 5:
        print("배송료:", 3500)

    elif km < 5:
        print("배송 x")
