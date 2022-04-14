# 파일 리스트
"""
C:/Users/hs/PycharmProjects/pythonProject1/test/knowledgeIn/indata_30.text C:/Users/hs/PycharmProjects/pythonProject1/test/knowledgeIn/indata_31.text
"""


def main(*args):
    # 길이
    length = len(args[0]) - 1

    f = str(args[0][0])
    f = f.split("/")
    # 문서 이름 추출
    f = f[-1].split(".")
    target = "C:/Users/hs/PycharmProjects/pythonProject1/test/knowledgeIn/{}-{}.text".format(f[0], length)
    with open(target, 'w', encoding="utf-8") as outfile:
        for i in range(len(args) + 1):
            with open(args[0][i], encoding="utf-8") as file:
                for line in file:
                    outfile.write(line)


if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    main(args)