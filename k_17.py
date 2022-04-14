"""함수 만드는 과젠데 밑에 사진처럼 만들었는데
전혀 실행이 안되네요 ㅠㅠㅠㅠ 어떻게 해야 정답인지
가르쳐주시면 감사하겠습니다ㅏㅏ 급해요 ㅠ
"""


def interSum(startNum, endNum):
    Sum = 0
    for i in range(startNum, endNum + 1):
        Sum += i

    return Sum


answer = interSum(5, 100)
print(answer)


"""
파이썬 주차장 프로그램 만드려고 하는데 어떻게 해야할 지 모르겠습니다...

주차가능한 차 10대로 하고 시작하면 환영인사가 출력되고
현재 주차가능한 대수 와 메뉴를 선택할 수 있게 합니다. 1은 입차, 2는 출차, 3은 프로그램 종료
입차 선택시 주차 가능한지 알려주고 입차 후 주차 가능 대수 감소
출차 선택시 주차 가능 대수 증가

제가 간단하게 만든 건데 여기서 잘 모르겠습니다... 도와주세요
"""


print (" 방문을 환영합니다. ")
car = 10

while True:
    menu = int(input("번호 입력(1:입차, 2:출차), 3 : 프로그램 종료 : "))

    if menu == 1:
        if car < 10:
            print (" 출입문이 열립니다. ")
            car += 1
            print("현재 차 대수: ", car)
        else:
            print (" 주차 불가능, 현재 차 대수: ", car)

    elif menu == 2:
        print (" 안녕히 가세요^^ ")
        car -= 1
        print("현재 차 대수: ", car)

    elif menu == 3:
        print(" 프로그램 종료합니다.")
        break
        
    else:
        print (" 다시 선택하십시오 ")