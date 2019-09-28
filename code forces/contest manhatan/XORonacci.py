t=int(input())

c=0

store=[]
for j in range(t):
    a=0
    b=0
    n=0
    i=2
    a, b, n = input().rstrip().split()
    a = int(a)
    b = int(b)
    n = int(n)
    if n==0:
        c=a
    if n==1:
        c=b
    while (i <= n):
        c = a ^ b
        # print("i come here"+ str(i))
        # print(c)
        a = b
        b = c
        i += 1
    store.append(c)
    # print(store)

for k in store:
    print(k,end="\n")
