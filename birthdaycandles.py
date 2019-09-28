import math
def birthdayCakeCandles(ar,n):
    count=0
    e=max(ar)
    for i in ar:
        if i==e:
            count=count+1
    return count


n=int(input())
ar=list(map(int,input().split()))
if n>=1 and n<=pow(10,5):
    for i in ar:
        if i>=1 and i<=pow(10,7):
            x=birthdayCakeCandles(ar,n)
            break

print(x)
