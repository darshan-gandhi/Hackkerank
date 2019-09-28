n=int(input())
arr=list(map(int,input().rstrip().split()))

# arr=[]
# for i in new:
#     if i not in arr:
#         arr.append(i)
coins=0
arr.sort()
store=[]
for i in range(len(arr)):
    sel=arr[i]
    coins=0
    for j in range(len(arr)):
        if arr[j]==sel:
            continue
        elif ((arr[j]-sel)%2==0):
            continue
        elif ((arr[j]-sel)%2!=0):
            coins+=1
            # print(f"the value of coins is increasing for addres {j}")
    store.append(coins)
# print(store)
print(min(store))