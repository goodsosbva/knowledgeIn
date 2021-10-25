# 계산기

print("1.덧, 2. 뺄, 3. 곱, 4. 나")
n = int(input("원하는 계산 입력: "))
if  1 <= n <= 4 :
    print("계산할 숫자 두 개를 입력")
    a = int(input())
    b = int(input())


if n == 1:
    c = a + b
    print("%d + %d = %d" % (a, b, c))
elif n == 2:
    c = a - b
    print("%d - %d = %d" % (a, b, c))
elif n == 3:
    c = a * b
    print("%d * %d = %d" % (a, b, c))
# 추가 부분
elif n == 4:
    c = a / b
    print("%d / %d = %d" % (a, b, c))
else:
    print("잘못 입력했습니다! 다시 입력해주세요.")


"""
파이썬에서 x=[x1, x2] 일때 x1,x2 둘 다 소수점 3번째 자리에서 반올림해서 출력하려면 어떻게 해야 하나요?
print('%10.3f' %x)로 하니까 only size-1 arrays can be converted to Python scalars 이렇게 오류가 뜨는데 해결방법 좀 알려주세요!
"""
x1 = 1.1256
x2 = 1.1254

x = [x1, x2]

for i in x:
    print('%10.3f' % i)


"""
1부터 n까지의 합은 n(n+1)/2로 주어진다. 
1부터 100까지의 합을 구하여 출력하는 프로그램을 작성하고 실행하라. 
단 실수가 입력되면 "정수를 입력하시오" 라고 떠야된다.
"""

n = int(input())
sum = n * (n + 1) // 2
print(sum)

