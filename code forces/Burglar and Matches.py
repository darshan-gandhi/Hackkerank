n,m=input().rstrip().split()
n=int(n)
m=int(m)
mat=[]
for i in range(m):
    f=list(map(int,input().split()))
    # x=int(x)
    mat.append(f)
final=0
matches=0
# print(m)
# print(mat[2][1])

mat=sorted(mat,key= lambda x:x[1])
mat.reverse()
print(mat)

# for i in range((m)):
#     # print(f"the val of i is {i}")
#     mat[i][0]=mat[i][0]*(-1)
#     # print(mat)
# mat.sort()
# print(mat)
# mat.reverse()
# print(mat)
# for i in range(m):
#     mat[i][0]=mat[i][0]*(-1)
# print(mat)
atmost=n*mat[0][1]
# print(atmost)
count=0
balance=n
var=0
ans=0
for i in range(m):
    j=i
    print(f"here  j is {j}")
    if (j != (m - 1)):
        print(j)
        if (mat[j][1] == mat[j + 1][1]) and (mat[j][0] > mat[j + 1][0]):
            print("hello wrold")
            j=j+1
            i=j
            continue
    if ((mat[i][0]<=n) and (final<=atmost)):
        var=mat[i][0]
        if mat[i][0]>balance:
            var=balance
        final=final+((var)*(mat[i][1]))

        balance=(balance)-(var)
        if (final>atmost):
            break
        ans=final
        print(f"the value of ans is {ans}")

        # count=(n)-mat[i][0]
        # print(f"count is {count}")
# print(f"{ans}")
        # count=mat[i][0]
        # balance=n-count

