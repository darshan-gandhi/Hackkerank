n,a=input().rstrip().split()
n=int(n)
a=int(a)
a=a-1
arr=list(map(int,input().rstrip().split()))
count=0
if arr[a]!=0:
    count+=1
    print("self thief there so increment by 1")

# for i in range(1,len(arr)):
#     if a==0:
#         if i!=(n-1):
#             if arr[a+i]!=0:
#                 count+=1
#     elif a==(n-1):
#         if i!=(0):
#             if arr[a-i]!=0:
#                 count+=1
                # print("this is the count getting printed")
    # else:
    #     if ((a-i)!=0) and ((a+i)!=(n-1)):
    #         if (arr[a-i]!=0) and (arr[a+i]!=0):
    #             count+=1
start=a
for i in range(1,len(arr)-1):
    # print(f"the value of i is {i}")
    if ((start-i>=0) and (start+i)<=(n-1)):
        if (arr[start-i]!=0) and (arr[start+i]!=0):
            count+=2
            # print("i also get printed")
            # print(f"this count is getting printed")
        # elif (arr[start-i]!=0) or (arr[start+i]!=0):
        #     count+=1
    elif ((start-i)<0):
        # print(start-i)
        if (start+i<=(n-1)):
            if (arr[start+i]!=0):
                count+=1
                # print(count)
                # print("hello there")
    elif ((start+i)>=(n-1)):
        # print(start+i)
        if (start-i)>=0:
            print(start - i)
            if(arr[start-i]!=0):

                count+=1
                print(count)
                print("wwhatsipp bitch")
# print(count)

