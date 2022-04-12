"""
왜 func_sum 리턴 값이 none으로 뜨는지 모르겠습니다
"""


ans = []
def func_sum(score, i, total = 0):
    i -= 1
    total += score[i]
    if i != 0:
        # 항상 리턴을 해주어야 한다.
        return func_sum(score, i, total)

    if i == 0:
        print(total)
        return total


score = [73, 95, 80, 57, 99]
i = len(score)


max_total = 0
tot = func_sum(score, i)

print("합계 점수:", tot)
print("평균 점수:", tot / i)


# gcd
def get_gcd(n,m):
    mod = m % n
    if mod != 0:
        m, n = n, mod
        return get_gcd(n, m)
    else:
        return n


n1 = int(input())
n2 = int(input())
print(get_gcd(n1, n2))




