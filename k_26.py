a = [10, 20, 30, 40, 0]

s = 0
for i in range(len(a) - 1):
    s += a[i]
a[-1] = s
print(a[0], "+", a[1], "+", a[2], "+", a[3], "=", s)