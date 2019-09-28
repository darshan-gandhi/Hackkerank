import math
def balancedSum(arr):
    for i in range(0, len(arr)):
        temp1 = i
        sum1 = 0
        sum2 = 0
        if i >= 0 and i <= n:
            if arr[i] >= 1 and arr[i] <= (2 * pow(10, 4)):
                for k in range(temp1):
                    if temp1 == 0:
                        sum1 = 0
                    else:
                        sum1 = sum1 + arr[k]
                for l in range(temp1 + 1, n):
                    sum2 = sum2 + arr[l]
                if sum1 == sum2:
                    yn.append("YES")
                    break
    if sum1 != sum2:
        yn.append("NO")
    return yn

T=int(input())
temp1=0
sum1=0
sum2=0
yn=[]
if T>=1 and T<=10:
    for j in range(T):
        n = int(input())
        if n>=1 and n<=pow(10,5):
            arr = list(map(int, input().split()))
            balancedSum(arr)
print(*yn,sep="\n")