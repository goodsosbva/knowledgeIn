# 지식인 질문
"""알파벳을 A~Z중에 랜덤으로 하나의 알파벳을 대문자로 받고 '소문자로 바꾸세요' 라는 문장이 나오고 정답을 입력했을때
 틀리면 '틀렸습니다.' 맞았으면 '맞았습니다.' 라고 나오는 코드를 만들어 주세요. 내공 100입니다."""
import random

alpa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P',\
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# 대문자 선택
randomWord = random.choice(alpa)
print(randomWord)
# 소문자로 변환
loweredWord = randomWord.lower()
# 정답 입력
ans = input("소문자로 바꾸세요: ")
# 판별
if loweredWord == ans:
    print("맞았습니다")
else:
    print("틀렸습니다")