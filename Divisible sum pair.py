n,k=input().split()
n=int(n)
k=int(k)
if n>=2 and n<=100:
    arr=list(map(int,input().split()))
    # print(arr)
i=0
count=0
j=0
for p in range(len(arr)):
   if (k>=1 and k<=100) and (arr[p]>=1 and (arr[p]<=100)):
       i = p
       # print("the value of i is " + str(i))
       for j in range(i + 1, len(arr)):
           # print("the value of j is " + str(j))
           if (arr[i] + arr[j]) % (k) == 0:
               # print("addition is btwn "+ str(i)+ " "+ str(j))
               count += 1
               # print(count)


print(str(count))