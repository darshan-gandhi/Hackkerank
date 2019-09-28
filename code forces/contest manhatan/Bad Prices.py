t=int(input())
counter=0
day=[]
store=[]
save=[]
s=0
for i in range(t):
    counter=0
    n=int(input())
    arr=list(map(int,input().rstrip().split()))
    for i in arr:
        s+=i
        if s >= 150000:
            break
    save=arr.copy()
    for i in range(len(arr)-1):
        temp=save[i]
        if temp>min(arr[i:(n)]):
            counter+=1
            # print(f"the value for which is it is index {i+1}")
            continue
    print(counter)
    # store.append(counter)
# print(day)
# for i in store:
#     print(i,end="\n")

