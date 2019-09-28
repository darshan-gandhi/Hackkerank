def func1(n,m,s):
    arr=[]
    for i in range(n):
        arr.append(i)
        print(arr)


t=int(input())
inp=[]
for i in range(t):
    n,m,s=input().split()
    func1(n,m,s)