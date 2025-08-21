import math

print("enter x, x1, y, y1 to calculate the Euclidean distance")
a = float(input())
b = float(input())
c = float(input())
d = float(input())

p = math.sqrt((math.pow((a - c), 2) + math.pow((b - d), 2)))
print(p)
