import copy

a = [1, 2, 5, 3, 4]
b = copy.deepcopy(a)

b.sort()
print(a, b) # [1, 2, 3, 4] [1, 0, 3, 4]