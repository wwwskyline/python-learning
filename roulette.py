a = int(input("enter a number to find out its color on the roulette:"))
if 36 >= a >= 0:
    if a == 0:
        print("green")
    elif 10 >= a >= 1:
        if a % 2 == 0:
            print("black")
        else:
            print("red")
    elif 11 <= a <= 18:
        if a % 2 == 0:
            print("red")
        else:
            print("black")
    elif 19 <= a <= 28:
        if a % 2 == 0:
            print("black")
        else:
            print("red")
    elif 29 <= a <= 36:
        if a % 2 == 0:
            print("red")
        else:
            print("black")
else:
    print("input error")
