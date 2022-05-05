def naiveStringMatcher(T, P):
    # 각각 총문자열의 길이를 구합니다
    n = len(T)
    m = len(P)
    # n - m + 1을 하는 이유는 총 길이 n에 m만큼 빼야 인덱스 에러가 안나기 때문입니다
    for shift in range(n - m + 1):
        # 문자열 T를 탐색합니다
        # 현재 인덱스 위치 shift에서 + m만큼의 구간 동안
        # 즉, T를 [idx: idx + m]자른 문자열이 타겟 패턴인 P의 문자열과 같다면
        # 패턴이 일치한다는 뜻입니다
        if P == T[shift:shift + m]:
            print('패턴 일치 shift=', shift)

    # 이건 저도 왜 있는지 모르겠네요?
    # 주석 처리 해도 작동합니다..
    # for i in range(n - m + 1):
    #     j = 0
    #     while (j < m):
    #         if T[i + j] == P[j]:
    #             j += 1
    #         else:
    #             break

"""
hello hi hi my name is kwon~ ? what you dont hear my name ok one more kwon not kown kwon!!! ok? 
"""
T = input('T(Text) 입력:')
P = input('P(Pattern) 입력:')

print('T(Text)=', T)
print('P(Pattern)=', P)

naiveStringMatcher(T, P)