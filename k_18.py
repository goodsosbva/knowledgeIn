"""2.다음은 사칙연산을 수행하는 함수이다."""


def func(a, b, mode="+"):
    if mode == "+":

        return a + b

    elif mode == "-":

        return a - b

    elif mode == "*":

        return a * b

    else:

        return a / b


# print(func(1, 5))  # 6
# print(func(1, 5, mode='*'))  # 5


"""
이 문제에 답이 되는 프로그램 좀 작성해주세요
힌트에 부합하는 답좀 부탁드립니다!!
"""


# 버블 정렬
def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(arr)


"""n = int(input("숫자 몇개?"))
arr = []
for _ in range(n):
    arr.append(int(input("숫자 입력: ")))
print("초기: ", arr)
bubble_sort(arr)"""


def llist(a,b):
    for i in range(a):
        j = int(input('%d: ' %(i + 1)))
        b.append(j)
    return b


# llist(1, [])


def evalQ(a, b, c, x):
    ans = a * (x ** 2) + (b * x) + c

    return ans


# print(evalQ(1, 2, 3, 4))
"""
두개의 코드의 실행결과를 알고 싶은데 자꾸오류가 떠서요ㅠㅠ

1. a=np.array(range(20)).reshape(4,5)
print(a.shape, a.ndim, a.size)

2. a=np.array([1,2,3])
b=np.array([4,5,6])
d=np.devide(a,b)
e=np.multiply(a,b)
print(d)
print(e)
"""
import numpy as np

a=np.array(range(20)).reshape(4,5)
print(a.shape, a.ndim, a.size)

a=np.array([1,2,3])
b=np.array([4,5,6])
d=np.divide(a,b)  # divide할려는거 아니신지?
e=np.multiply(a,b)
print(d)
print(e)
