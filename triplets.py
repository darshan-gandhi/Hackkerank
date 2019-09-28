arr1=input('enter 3 numbers for first')
arr1.split()
arr2=input('enter 3 numbers for second')
arr2.split()

count1=0
count2=0

for i in range(3):
    if arr1[i] > arr2[i]:
        count1=count1+1
        print(str(count1)  + "for first" + str(i))

    elif arr2[i] > arr1[i]:
        count2=count2+1
        print(str(count2) + "for second" + str(i))
    else :
        continue

ans=[count1,count2]
print(ans)