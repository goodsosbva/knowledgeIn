# num = int(input())

"""b = num // 100
s = (num % 100) // 10
i = (num % 100) % 10

print(b, s, i)"""
chk = True
for i in range(100, 1000):
    a = i // 100
    b = (i % 100) // 10
    c = (i % 100) % 10
    i = str(i)
    q = i[0]
    w = i[1]
    e = i[2]
    if int(q) == a:
        if int(w) == b:
            if int(e) == c:
                continue
    else:
        print(i, i[0], i[1], i[2], a, b, c)
        chk = False
        break

print(chk)
