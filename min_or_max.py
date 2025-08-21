print("Enter four numbers:")
a = float(input())
b = float(input())
c = float(input())
d = float(input())
print('What execute: "min" or "max"')
what = input()

if what == "min":
    num = min(a, b, c, d)
    print(num)
elif what == "max":
    num = max(a, b, c, d)
    print(num)
else:
    print("Error")
