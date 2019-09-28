n=int(input())
row=[]
mat=[]
save=[]
for i in range(n):
    row=input().split()
    # save=row
    mat.append(row)

print(mat)
store=[]
new=[]
for i in range(len(mat)):

    store.append(mat[i][0])
    new.append(store)


for i in range(len(mat)):
    store.append(mat[i][1])
    new.append(store)

for i in range(len(mat)):
    store.append(mat[i][2])
    new.append(store)


print(new[0])
extra=[]
extra=new[0]
save=extra[:3]
save1=[]
save2=[]
save1=extra[3:6]
save2=extra[6:9]


print(save)
print(save1)
print(save2)
save.reverse()
save1.reverse()
save2.reverse()

brandnew=[]
brandnew.append(save)
brandnew.append(save1)
brandnew.append(save2)

print(brandnew)
