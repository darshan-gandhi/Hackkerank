import math
def miniMaxSum(arr):
    smin = 0
    smax = 0
    arr.sort()
    for i in range(1, len(arr)):
        smax = smax + arr[i]

    arr.reverse()
    for i in range(1, len(arr)):
        smin = smin + arr[i]
    print(str(smin) +" " + str(smax))


arr=[]
arr=list(map(int,input().split()))

for i in arr:
    if i>=1 and i<=pow(10,9):
        miniMaxSum(arr)
        break


