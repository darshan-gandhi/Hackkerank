save=[]
t=int(input())
for i in range(t):

    N,k=input().split()
    N=int(N)
    count=0
    arr=[]
    k=float(k)
    arr=list(map(float,input().split()))
    # print(arr)
    for i in arr:
        if float(i) >= k :
            count=count+1
    # print(count)
    save.append(count)
    # print(save)
for i in save:
    print(i,sep="\n")
