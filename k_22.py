"""
-1이 입력될 때까지 학생들의  이름과 시험성적(0~100점)을 입력받아  학생들의 석차를 계산하여

학생의 이름, 시험성적, 석차를 출력하는 프로그램을 작성하라.
"""


def sol():
    people = []
    while True:
        name = input()
        if name == "-1":
            break
        score = int(input())
        people.append([name, score])


    sorted_people = sorted(people, key=lambda x: -x[1])

    for i in range(len(sorted_people)):
        print("이름:", sorted_people[i][0],"점수:", sorted_people[i][1],"석차:", i + 1)
    return


"""
임의의 양의 정수 n에 대해  다음의 s(n)을 계산하는 함수를 작성하고, 이 함수를 이용하여 

n = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10에 대한 계산결과를 출력하는 파이썬 프로그램을 작성해주세요.

s(n) = 1 + (1*2) + (1*2*3) + (1*2*3*4) + .... + (1*2*3*...*n) 
"""
n = int(input())

s = 0
for i in range(1, n + 1):
    t = 1
    for j in range(1, i + 1):
        t *= j

    s += t

print(s)
