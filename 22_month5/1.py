# 1. 적립금
a = 1000
b = 2000
c = 4000

A = int(input())
B = int(input())
C = int(input())

x = 10000

totalmoney = a*A + b*B + c*C
if totalmoney > x:
    print(totalmoney - x)
else:
    print(0)