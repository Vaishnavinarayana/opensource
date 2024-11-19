import math
x, n = map(int, input().split())
capacity = x * 100
shortfall = max(0, n - capacity)
newplanes = (shortfall + 99) // 100
print(newplanes)
