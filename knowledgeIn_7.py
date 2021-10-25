# 7
"""
왜 이름 enter하면 바로 break되지않고 번호까지 enter눌러야 break가 될까요?
홍길동 = 010-1111-2222
김미숙 = 010-2222-3333
이렇게 출력되야하는데 왜 딕셔너리랑 같이 나오나요 ?
"""

people = {}

while True :
    name = input("이름:")
    if name == '':
        print("=====연락처 목록=====")
        print(people)
        break
    number = input("번호:")
    people[name] = number

