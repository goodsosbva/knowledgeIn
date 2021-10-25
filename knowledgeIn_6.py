"""
# 6
1부터 1000까지라는 제한을 둘 방법을 모르겠어서요 ㅠㅠㅠ
while문을 삽입해야 하나요?
아니면 for문이 잘못되었을까요?
아니면 제 코드 자체가 잘못되었을까요?

예제문제는
"리스트를 이용하여 1부터 1000사이의 숫자들의 약수의 개수를 출력하는 프로그램을 만들어라"
입니다.
"""

number = int(input("숫자를 입력하세요:"))
Data = []
count = 0
if 1 <= number <= 1000:
    for i in range(1, number + 1):
        if number % i == 0:
            Data.append(i)
            count += 1
    print("1에서 %d사이 숫자의 약수의 개수는 %d개 입니다." % (number, count))
else:
    print("number 올바르게 입력해주세요!")

