# 15.
"""
while문을 이용해서 임의의 개수의 성적을 받아서 평균을 계산한 후에 출력하는 프로그램을 작성.
+소수점 첫째자리에서 내림,올림,반올림 구현

실행결과
종료하려면 음수를 입력하시오
성적을 입력하시오:83
성적을 입력하시오:62
성적을 입력하시오:54
성적을 입력하시오:-1
성적 평균:66.333333333
성적 평균(내림):66
성적 평균(올림):67
성적 평균(반올림);66
"""
import math


sum = 0
cnt = 0
while True:
    n = int(input())
    if n < 0:
        break
    sum += n
    cnt += 1


print(sum / cnt)
print(math.ceil(sum / cnt))
print(math.floor(sum / cnt))
print(round(sum / cnt))


"""
저는 다음과 같이 코드를 작성했고
t = input()
a,b = input().split()
a = int(a)
b = int(b)
for t in range(a):
    for t in range(b):
        print(a+b)
t를 입력받을 때 int(t)도 써봤지만 두개 다 틀렸다고 나옵니다.
정답말고 이유만 알려주세요
아직까지 문제 지문을 100%이해하고 풀 수준은 아니라서 힘든데 거기다 다국어 문제니 지문이
더 헷갈리네요.
"""


t = int(input())

for _ in range(t):
    a, b = input().split()
    a = int(a)
    b = int(b)
    print(a + b)


"""
A : f(n) = 2*f(n-1) – 1 (n은 자연수) 식을 
ex) A는 17입니다. 로 출력되게 
파이썬에서 코딩하려면 어떻게 해야하나요ㅜㅠ? 
"""


def f(n):
    return f(n - 1)

n = 17

