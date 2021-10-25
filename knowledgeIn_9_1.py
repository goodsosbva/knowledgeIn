"""
q4
"""
# from itertools import permutations
from itertools import combinations


inputs = input()
target = int(input())

items = []
numbers = []
for i in range(len(inputs)):
    items.append(int(inputs[i]))

print(items)
# list(permutations(items, 2))
for i in range(1, len(inputs)):
    n = list(combinations(items, i))
    numbers.extend(n)

print(numbers[1][0])
print(numbers)