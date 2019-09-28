mat=[]
for i in range(3):
    row=input().split()
    mat.append(row)

sumc=0
sumr=0
sumd=0
print(mat)
sc=[]
sr=[]
sd=[]
for i in range(len(mat)):
    sumr=0
    for j in range(len(mat)):
        sumr=sumr+int(mat[i][j])
        # print(f"the sum is {sumr}")
    sr.append(sumr)
print(sr)

for j in range(len(mat)):
    sumc=0
    for i in range(len(mat)):
        sumc=sumc+int(mat[i][j])
        # print(f"the sum is {sumc}")
    sc.append(sumc)
print(sc)

for i in range(len(mat)):

    for j in range(len(mat)):
        if i==j:
            sumd=sumd+int(mat[i][j])
            # print(f"the sum is {sumd}")
            # sd.append(sumd)
        # elif (i==0 and j==2) or (i==1 and j==1) or (i==2 and j==0) :
        #     sumd=sumd+int(mat[i][j])
        #     sd.append(sumd)

sumsd=0
sumsd=sumsd+int(mat[0][2]) + int(mat[1][1])+int(mat[2][0])
sd.append(sumd)
sd.append(sumsd)
print(sd)


for i in range(len(mat)):
    for j in range(len(mat)):
        if 