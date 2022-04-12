# 사칙연산해서 만들 수 있는 수의 개수와 그 결과들
"""
20210724
100

답 = 2
"""

nums, n = list(input()), int(input())

length = len(nums)
ops = ['+', '-', '*', '/', '']
op_list = []

for i in range(length-1, 0, -1):
    nums.insert(i, f'op_list[{i-1}]')



"""
루프를 돌 때마다 cnt가 증가하는데, 
이 값을 5진수로 변환한 뒤 다섯 가지의 연산자('+', '-', '*', '/', '')를 변환된 값의 각 자리에 따라 할당하면 
모든 경우의 수에 대한 연산을 수행할 수 있기 때문입니다.
"""


def base_5(num):
    q, r = divmod(num, 5)
    if q:
        return str(base_5(q))+str(r)
    return str(r)


cnt = 0
while True:
    idx = f'{base_5(cnt):>0{length-1}}'
    op_list.clear()
    for i in range(length-1):
        op_list.append(ops[int(idx[i])])
    exp = ''
    for i in range(len(nums)):
        exp += str(eval(nums[i]))
    try:
        if eval(exp) == n:
            print(exp)
    except:
        pass
    if op_list.count('') == length-1:
        break
    cnt += 1