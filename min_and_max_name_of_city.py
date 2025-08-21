a = input()
b = input()
c = input()
print("Enter 3 words or 3 numbers to find out the shortest and longest among them")
sum1 = len(a)
sum2 = len(b)
sum3 = len(c)

mini = min(sum1, sum2, sum3)
maxi = max(sum1, sum2, sum3)

minname = 0
maxname = 0

if len(a) == mini:
    minname = a
elif len(a) == maxi:
    maxname = a

if len(b) == mini:
    minname = b
elif len(b) == maxi:
    maxname = b

if len(c) == mini:
    minname = c
elif len(c) == maxi:
    maxname = c


print(minname)
print(maxname)
