arr1=input('enter 3 numbers')
arr1.split()
arr2=input('enter 3 numbers for second')
arr2.split()
count=0
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
countm=0
# for i in range(3):
#     if arr1[i] > arr2[i]:
#         count1+=1
#     elif arr2[i]> arr1[i]:
#         count2+=1

if arr1[0] > arr2[0] :
    count1=1
elif arr1[0] < arr2[0] :
    count2=1
elif arr1[1] > arr2[1] :
    count3=1
elif arr1[1] < arr2[1] :
    count4=1
elif arr1[2] > arr2[2] :
    count5=1
elif arr1[2] < arr2[2] :
    count6=1
count=count1+count3+count5
countm=count2+count4+count6

ans=(count,countm)
print(ans)
