x,y=input().split()


arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
save=[]

arr1.sort()
arr2.sort()
#print(arr1)
#print(arr2)

first=arr1[-1]
sec=arr2[0]
for i in range(first,sec+1):
   # print(i)
    for j in arr1:
        if (i%j)==0:
            save.append(i)
            print(save)
            # for k in arr2:
            #     if (k%i)==0:
            #         save.append(i)


# print(save)
# print(len(save))