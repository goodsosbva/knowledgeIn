n = int(input())

a = 1
b = 1
fibo = [a, b]

for i in range(2, n):
    fibo.append(fibo[i-1] + fibo[i-2])

for j in range(n):
    if (j + 1) % 2 == 0:
        print(fibo[j])


