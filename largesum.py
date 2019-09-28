def averybigsum(arr,n):
    resultmain=sum(arr)
    return resultmain


n=int(input())
if n>=1 and n<=10:
    arr=list(map(int,input().split()))
    for i in arr:
        if i>=0 and i<=pow(10,10):
            result=averybigsum(arr,n)
            print(result)
            break