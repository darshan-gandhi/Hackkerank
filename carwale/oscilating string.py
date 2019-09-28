s=input()

arr=list(s)
new=[]
arr.sort()
count=len(arr)
while(count!=0):
    for i in arr:
        if i not in new:
            new.append(i)
            arr.remove(i)
    arr.reverse()
    for i in arr:
        if i not in ne:
            new.append(i)
            arr.remove(i)
    count=count-1
for i in new:
    print(i,end="")