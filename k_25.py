"""
이렇게 입력했는데 invalid syntax라고 떠요 ㅜㅜ
코드좀 알려주세요
"""

engkor_dict = dict()
while True:
    eng = input("영어단어 :")
    if eng == "":
        break
    else:
        if eng in engkor_dict:
            print(eng, "단어가 등록되어 있습니다")
            continue
        else:
            kor = input("한글 단어 :")
            engkor_dict[eng] = kor
            print("단어를 추가합니다.")

print(engkor_dict)