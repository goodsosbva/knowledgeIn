"""저장 코드랑 반환하는 코드를 어떻게 작성해야하는지 모르겠어요ㅜ"""


def sum(n):
    ret = 0
    # 1부터 n까지의 합을 저장할 변
    for i in range(n + 1):
        ret += i
    return ret


# 결과값 반환
# result = sum(10)
# print(result)


from collections import Counter
lst = [10, 30, 40, 50, 30, 30, 20, 20, 20, 10, 30]
res = []

#1
res = Counter(lst)
res1 = []
for key, val in res.items():
    if val == 1:
        res1.append(key)
print(res1)


# 2
n_lst = set(lst)
print(list(n_lst))


# 3
ans = Counter(lst)
for key, val in res.items():
    if val > 1:
        print(key, ":", val, "회")



