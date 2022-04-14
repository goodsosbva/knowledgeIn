# 변수 선언
list = []
name, phone, email = 0, 0, 0
while (True):
    command = input("명령어를 입력하세요(add,delete,search,quit,all,change)").split()
    if command[0] == "quit":
        break

    elif command[0] == "add":
        name = input("이름을 입력하세요")
        phone = input("전화번호를 입력하세요")
        email = input("이메일을 입력하세요")
        list.append([name, phone, email])

    elif command[0] == "all":
        list.sort()
        for i in list:
            print(i)

    elif command[0] == 'delete':
        # del_name = input("삭제할 사람을 입력하세요.")
        del_name = command[1]
        for i in list:
            print(i[0])
            if del_name == i[0]:
                list.remove(i)
                break
    print(list)