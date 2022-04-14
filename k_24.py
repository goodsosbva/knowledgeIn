"""실행결과가

도전자이름:홍길동
가위바위보 입력:가위
비겼습니다
홍길동 1승 1무 3패

이렇게 나와야하는데
코드 좀 부탁드립니다..ㅠ
"""
import random

가위바위보 = {0:'가위', 1:'바위', 2:'보'}
name = input("도전자이름:")
w, d, l = 0, 0, 0

while True:
    me = input("가위바위보 입력:")
    if me == "그만":
        print("가위바위보 종료!")
        break
    enemy = random.choice(list(가위바위보.values()))
    print("user:", me)
    if enemy == '가위':
        print("상대는", enemy)
        if me == '가위':
            print("무승부")
            d += 1
            print(name, w, "승", d, "무", l, "패")
        elif me == '바위':
            print("승리")
            w += 1
            print(name, w, "승", d, "무", l, "패")
        else:
            print("패배")
            l += 1
            print(name, w, "승", d, "무", l, "패")

    elif enemy == '바위':
        print("상대는", enemy)
        if me == '바위':
            print("무승부")
            d += 1
            print(name, w, "승", d, "무", l, "패")
        elif me == '보':
            print("승리")
            w += 1
            print(name, w, "승", d, "무", l, "패")
        else:
            print("패배")
            l += 1
            print(name, w, "승", d, "무", l, "패")

    elif enemy == '보':
        print("상대는", enemy)
        if me == '보':
            print("무승부")
            d += 1
            print(name, w, "승", d, "무", l, "패")
        elif me == '가위':
            print("승리")
            w += 1
            print(name, w, "승", d, "무", l, "패")
        else:
            print("패배")
            l += 1
            print(name, w, "승", d, "무", l, "패")


