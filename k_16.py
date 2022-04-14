"""import turtle

""""""t = turtle.Pen()
t.forward(50)
t.left(90)
t = turtle.Turtle()
t.shape('turtle')
turtle.exitonclick()"""
import random


while True:
    round = int(input("몇 라?"))
    coin = ['head', 'tail']
    if round < 8 and round % 2 == 1:
        h = 0
        c = 0
        for i in range(round):
            human = input("앞, 뒤?")
            computer = random.choice(coin)
            print(human, computer)
            if  human == computer:
                h += 1
            else:
                c += 1
            print(h, ":", c)

    else:
        print("라운드는 짝수만 가능하고, 8회이상은 불가능 합니다!")
        continue


    oneco = input("찐막? ")
    print(oneco)
    if oneco == "Y" or oneco == "Yes":
        print("hi")
        continue
    else:
        real = input("정말 감?")
        if real == "Y" or real == "Yes":
            break
        else:
            oco = input("할거?")
            if oco == "Y" or oco == "Yes":
                continue
            else:
                break

