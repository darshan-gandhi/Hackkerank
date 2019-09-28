n=int(input())
if n>=5 and n<=(2*pow(10,5)):
    arr=list(map(int,input().split()))
    print(arr)
x=0
count=0
arr.sort()
print(arr)
new=[]
for i in range(len(arr)):
    x=arr[i]
    count=0
    print("the ele is"+ str(x))
    for j in range(i+1,len(arr)):

        if x==arr[j]:
            print("the element is" + str(x))
            count += 1
            print(count)
        else:
            count=count+1
            break
            # new.append(count)
    new.append(count)
print(new)