"""
아래와 같이 start 값 4부터 end 값 29 사이의 정수 중에서
모든 짝수값을 리스트로 생성하여 리턴하는 함수 def getEvenList(start, end): 코드를 작성하여 업로드 하시오.
"""

start = 4
end = 29
res = []

for i in range(start, end + 1):
    if i % 2 == 0:
        res.append(i)

print(res)

"""
예를들면 제가 1 과2와3을 입력하고
0번째 배열에는 1 1번째 배열에는 2 가들어가게
그리고 0~2번째 배열에 1~9까지 랜덤한 수를 넣고싶을때는 어떻게 하나요? 
"""
import random


ans = []
for i in range(3):
    input_n = int(input())
    ans.append(input_n)
print(ans)
ans.insert(0, 1)
ans.insert(1, 2)
print(ans)
# randomNum = random.randrange(1,9) 랜덤 함수 사용하는 법
for i in range(3):
    ans.insert(i, random.randrange(1, 9))
print(ans)


"""
Create a function that takes in x, y, and z then calculates the following:

x2+y2+z2
"""



