print('введите 8 чисел и программа выведет кол-во чисел которые кратны 4 и самое наибольшее число которое кратно 4:')
n = 7
count = 0
maximum = -10**12
for i in range(0, n + 1):
    x = int(input())
    if x % 4 == 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')