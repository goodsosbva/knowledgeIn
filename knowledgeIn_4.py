# 4.
"""
두 개의 정수를 입력받아 두 숫자 사이의 홀수합계와 짝수합계를 구하는 코드를 작성하시오 .
어떻게 하나요 ㅜㅠㅜㅠㅜㅠㅜ급합니다 부탁드릴게요
"""
# 두 정수 값 입력
a, b = input().split()
a = int(a)
b = int(b)

s1 = 0
s2 = 0
# 두 정수값 사이를 반복
for i in range(a, b + 1):
    # 짝수
    if i % 2 == 0:
        s2 += i
    # 홀수
    if i % 2 == 1:
        s1 += i

print("홀: ", s1, " ","짝:", s2)