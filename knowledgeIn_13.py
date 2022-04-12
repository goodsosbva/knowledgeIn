"""# 1.
sum = 0
cnt = 0
for i in range(5):
    a = int(input())
    if a >= 80:
        cnt += 1
    sum += a

print("성적 평균:", sum // 5)
print("80점 넘은 학생 수: ", cnt)


# 2.
number1 = int(input())
number2 = int(input())
print(number1, '-', number2, '=', number1 - number2)


# 3.
eur = 1337.92
eur_input = float(input())
print("원화 환산: ", round(eur_input * eur, 2))


# 4.
year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(year, "년은 윤년입니다")
else:
    print(year, "년은 윤년이 아닙니다")


# 5.
movie = ['소울', '세자매', '캐롤', '커넥트', '원더우먼']
print(movie[-1])
print(movie[:3])
print(movie[2:3])
print(movie[-2:])"""

"""
문제출력해야되는데 어떻게 해야될지 모르겠어요ㅠㅠ

티셔츠 5000원, 청바지 10000원, 치마 10000원, 가디건 150000원, 자켓 20000원.
-> '20000원 이상 구매시 20%할인적용', 특정 의류 선택 시 할인 10%' 출력값을 어떻게 해야되나요ㅠㅠ
"""
clothes = [['티셔츠', 5000], ['청바지', 10000], ['치마', 10000], ['가디건', 150000], ['자켓', 20000]]


# 특정 의류가 치마라는 가정!
for dress, money in clothes:
    if money >= 20000:
        print(dress, "가 20% 할입되니다. 가격은", int(money * (80 / 100)), "원 입니다.")
    elif dress == '치마':
        print(dress, "가 10% 할입되니다. 가격은", int(money * (90 / 100)), "원 입니다.")
    else:
        print(dress, "의 가격은", money, "원 입니다.")

