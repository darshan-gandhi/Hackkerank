

def darshan(n,k,arr):
    d=0
    y=0
    save=[]
    store=[]
    s=0
    for i in arr:
        small=0
        large=0
        # print("value of i" + str(i))
        small=(i-k)
        large=(i+k)
        store.append(small)
        store.append(large)

        print(store)

        for i in range():
            if i not in save:
                save.append(i)
            # print(save)
    # print(save)
        s=len(save)
    # print(f"the len is {s}")
    return s




t=int(input())
new=[]
arr = []
brandnew=[]
for i in range(t):
    x=0
    n=0
    k=0
    n, k = input().split()
    arr.clear()
    arr = (list(map(int, input().rstrip().split())))
    arr=arr-int(k)
    print(arr)
    z=darshan(int(n),int(k),arr)
    brandnew.append(z)
for i in brandnew:
    print(i,sep="\n")
#
#
# t = int(input())
# for _ in range(t):
#     n, k = map(int,input().split())
#     a = map(int,input().split())
#     left = [i-k for i in a]
#     left.sort()
#     right = [i+k for i in a]
#     right.sort()
#     range_list = [[i-k, i+k] for i in a]
#     partial = sum([(abs(i[0]-i[1])+1) for i in range_list])
#     #print partial
#     partial_1 = []
#     #print left, right
#     #for i in left[1:]:
#     #    for j in right:
#     #        if i < j:
#     #            partial_1.append(abs(i-j)+1)
#     for i in range(len(left[1:])):
#         if left[i+1] <= right[i]:
#             partial_1.append(abs(left[i+1] - right[i])+1)
#     partial_1 = sum(partial_1)
#     #print partial_1
#     print (abs(partial-partial_1))