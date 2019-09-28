def countApplesAndOranges(s,t,a,b,ad,bd):
    counta = 0
    counto = 0
    orange = 0
    ap = 0

    if (int(s) >= 1 and int(s) <= pow(10, 5)) and (int(t) >= 1 and int(t) <= pow(10, 5)) and (
            int(a) >= 1 and int(a) <= pow(10, 5)) and (int(b) >= 1 and int(b) <= pow(10, 5)) and (
            int(m) >= 1 and int(m) <= pow(10, 5)) and (int(n) >= 1 and int(n) <= pow(10, 5)) and (int(a)<int(s)<int(t)<int(b)):
        for i in ad:
            if int(i)>=pow(-10,5) and int(i)<=pow(10,5):
                ap = int(a) + i
                # print(ap)
                if ap >= int(s) and ap <= int(t):
                    counta = counta + 1
        for j in bd:
            if j>=pow(-10,5) and j<=pow(10,5):
                orange = int(b) + j
                if orange >= int(s) and orange <= int(t):
                    counto = counto + 1
    print(counta)
    print(counto)

s,t=(input().split())
a,b=(input().split())
m,n=(input().split())
ad=[]
bd=[]

ad=list(map(int,input().split()))
bd=list(map(int,input().split()))
#print(ad)
#print(bd)
countApplesAndOranges(s,t,a,b,ad,bd)