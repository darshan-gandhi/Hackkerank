save=[]
for i in range(int(input())):
    n,m=input().split()
    n=int(n)
    m=int(m)
    store=0
    save.clear()
    for j in range(1,n+1):
        if j%m==0:
            # print(j)
            arr=list(str(j))
            save.append(int(arr[len(arr)-1]))
    print(sum(save))

