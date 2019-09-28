def diagonalDifference(arr):
    sum1 = 0
    # sum2 = 0
    save = []
    for i in range(n):
        for j in range(n):
            if int(arr[i][j])>=-100 and int(arr[i][j])<=100:
                if i == j:
                    sum1 = sum1 + int(arr[i][j])
    # print(f"the sum is {sum1}")
    save.append(sum1)

    # sum2=sum2+int(mat[0][2])+int(mat[1][1])+int(mat[2][0])
    # # print(sum2)
    # save.append(sum2)

    sum2 = 0
    for i in range(n):
        if int(arr[i][j]) >= -100 and int(arr[i][j] )<= 100:
            sum2 = sum2 + int(arr[i][n - 1 - i])
        # print(sum2)
    save.append(sum2)
    diff = 0
    diff = abs(int(save[0]) - int(save[1]))
    print(diff)


n=int(input())
arr=[]
for i in range(n):
    row=input().split()
    arr.append(row)
# print(mat)
diagonalDifference(arr)