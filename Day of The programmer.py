def dayOfProgrammer(y):
    if y >= 1700 and y <= 2700:
        if y < (1918):
            if y % 4 == 0:
                print(f"12.09.{y}")
            else:
                print(f"13.09.{y}")
        elif y == 1918:
            print(f"27.09.{y}")
        else:
            if ((y % 4 == 0) and (y % 100 != 0)) or (y % 400 == 0):
                print(f"12.09.{y}")
            else:
                print(f"13.09.{y}")



y=int(input())
dayOfProgrammer(y)
