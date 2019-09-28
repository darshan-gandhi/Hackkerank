from datetime import date

t=int(input())
arr=[]
for i in range(t):
    print(f"the value of i is {i}")
    n=int(input())
    for j in range(n):
        x=input().split()
        print(x)
        arr.append(x)
        int(arr)
    save=[]
    for k in range(n):
        save.append(date(arr[i][1])-date(arr[i][0]))
        print(save)







