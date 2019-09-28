def plusMinus(ar,n):
    countn = 0
    counto = 0
    countp = 0
    for i in ar:
        if i >= -100 and i <= 100:
            if int(i) > 0:
                countp = countp + 1
            elif int(i) < 0:
                countn = countn + 1
            else:
                counto = counto + 1
    total = n
    p = countp / total
    n = countn / total
    o = counto / total
    print(p)
    print(n)
    print(o)

ar=[]
n=int(input())
if n>=0 and n<=100:
    ar = list(map(int, input().split()))
# print(ar)

# print("pos"+ str(p) + "\nneg"+ str(n) + "\no"+ str(o) )
plusMinus(ar,n)