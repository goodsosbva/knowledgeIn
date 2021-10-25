# 5
"""
만약에 output의 첫 줄이 xyzabc이렇게 되어있는데
그 다음줄을 첫줄의 길이만큼 z부터 알파벳을 순서대로 더하고 싶으면 어떻게 하나요
z 는 주어져있고 나머지는 a 부터 정렬이에요!
"""

output = "xyzabc"


res = []  # 정답
# z 만 빼기
for i in range(len(output)):
    if output[i] == "z":
        res.append(output[i])
        output = output[:i] + output[i + 1:]
        break

# z 빼고 정렬
s = sorted(output)

# res.append(sort(output))

for i in s:
    res += i

for i in res:
    print(i, end="")

