n=int(input())
mat=[]
for i in range(n):
    x=list(map(int,input().rstrip().split()))
    mat.append(x)

arr=[]
temp=0
i=0
while i<len(mat):
    temp=i
    print(temp)
    if temp!=len(mat)-2:
        for k in range(temp,temp+3):
            arr.append(mat[i][k])
            print(arr)


    i=i+1
        # elif i==(temp)+1:
        #     arr.append(mat[temp+1][i+1])
        #     print(arr)
        #     break
        # elif i==(temp)+2:
        #     arr.append(mat[temp+2][i])
        #     print(arr)


# print(arr)


