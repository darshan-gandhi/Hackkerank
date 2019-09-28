def timeConversion(time1):
    if time1[0] >= "01" and time1[0] <= "12":
        if time1[1] >= "00" and time1[1] <= "59":
            if time1[2] >= "00" and time1[2] <= "59":
                for i in range(len(time1)):
                    if time1[i] == "PM":
                        if time1[0] != "12":
                            time1[0] = int(time1[0]) + 12
                        # print(time1)

                    elif time1[i] == "AM":
                        if time1[0] == "12":
                            time1[0] = int(time1[0]) + 12
                            if time1[0] == 24:
                                time1[0] = "00"

    if int(time1[0]) >= 00 and int(time1[0]) <= 23:
        print(str(time1[0]) + ":" + str(time1[1]) + ":" + str(time1[2]))



time=list(map(str,input().split(":")))
#print(time)
time1=time
x=time1[-1][-2:]
y=time1[-1][:-2]
time1.pop(-1)
time1.append(y)
time1.append(x)
timeConversion(time1)
