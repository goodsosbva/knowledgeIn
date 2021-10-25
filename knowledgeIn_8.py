# 8
"""
4개의 양의 정수 a, b, c, d를 입력받아서a, b를 더한 값과c, d를 사칙연산으로 계산한 값 중동일한 값이 있다면,
(+, -, *, /) 순서대로어떤 사칙연산을 이용하였는지 출력하고동일한 값이 없다면 incorrect를 출력하는 프로그램을 작성하세요*
나누기연산(/)은 소수점을 제외한 값으로 계산[입력 예시1]2351[출력 예시1]*/[입력 예시2]3115[출력 예시2]incorrect
"""
"""a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)"""
numbers = input()
a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])
d = int(numbers[3])

target = a + b
answer = []

if target == c + d:
    answer.append("+")
if target == c - d:
    answer.append("-")
if target == c * d:
    answer.append("*")
if target == c // d:
    answer.append("/")

if len(answer) == 0:
    print("incorrect")
else:
    print(answer)

