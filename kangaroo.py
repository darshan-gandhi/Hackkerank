def kangaroo(a,b,s,t):
    while True:
        sum1 = 0
        if (int(a) >= 0 and int(a) <= pow(10, 3)) and (int(s) >= 0 and int(s) <= pow(10, 3)) and (
                int(b) >= 1 and int(b) <= pow(10, 3)) and (int(t) >= 1 and int(t) <= pow(10, 3)):
            if (s > a) and (t > b):
                print("NO")
                break
            sum1 = (int(s) - int(a)) % (int(t) - int(b))
            if sum1 == 0:
                print("YES")
                break




a,b,s,t=input().split()
kangaroo(a,b,s,t)