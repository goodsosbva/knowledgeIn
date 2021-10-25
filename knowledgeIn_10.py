"""
10. 지식인 문제
사용자에게 한자리 숫자 n을 입력 받으면 n×n 2차원 배열로 출력하고 싶은데,

만약 3을 입력받았다면

1 2 3
6 5 4
7 8 9

이런식으로 출력하려면 어떻게 해야할까요...

3일째 풀고 있는데, 답이 안나와서요...ㅠㅠㅠㅠ
제발 도와주세요...
"""
n = int(input())

array = [[0] * n for _ in range(n)]
# print(array)
number = 1

for i in range(n):
    for j in range(n):
        array[i][j] = number
        number += 1
    print(array[i])

"""
3.7번 문제를 교수님이 어떻게 풀었는지 기억이 안나서
 그냥 제 맘대로 쓰긴 했는데 (식이 제 느낌상 깔끔하지가 못한거 같아요) 
이대로 써도 되는건가요? 아니면 더 간결하게 해야 하나요? 
간결하게 할 수 있다면 어떻게 해야될까요?
"""
num = input()
print(num[0])
print(num[1])
print(num[2])




