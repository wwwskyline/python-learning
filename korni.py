from math import *

print("Enter a, b, c separately on each line to find out if there are roots:")
a = float(input())
b = float(input())
c = float(input())
x = 0
dis = pow(b, 2) - (4 * a * c)
if dis < 0:
    print("Нет корней")
elif dis == 0:
    x = -(b / (2 * a))
    print(x)
elif dis > 0:
    x2 = 0
    x = (-b - sqrt(dis)) / (2 * a)
    x2 = (-b + sqrt(dis)) / (2 * a)
    if x < x2:
        print(x)
        print(x2)
    elif x > x2:
        print(x2)
        print(x)
