a = int(input())
print('enter a three-digit number to find out if it is "interesting" or not')
fst = a // 100
two = (a // 10) % 10
thre = a % 10

maxi = max(fst, two, thre)
mini = min(fst, two, thre)

sred = fst + two + thre - mini - maxi
if (maxi - mini) == sred or (mini - maxi) == sred:
    print("Число интересное")
else:
    print("Число неинтересное")
