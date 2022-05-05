numbers = map(int, input("정수들을 입력하세요 : ").split(","))

numberlist = list(numbers)
list1 = sorted(numberlist)
list2 = sorted(numberlist, reverse=True)

result = []
for i in range(len(numberlist)):
    result.append(list1[i] * list2[i])

print(result)