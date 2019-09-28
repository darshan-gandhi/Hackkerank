def migratoryBirds(arr):
    for i in arr:
        if i >= 1 and i <= 5:
            if i not in sel:
                sel.append(i)
    # print(sel)
    c = []
    for j in sel:
        count = 0
        for i in arr:
            if i == j:
                count = count + 1
        c.append(count)

    m = c[0]
    temp = 0
    save = []
    # print(c)
    for i in range(len(c)):
        if c[i] >= m:
            m = c[i]
            # print("the max is"+ str(m))
            temp = i
    for k in range(0, temp):
        # print("the value of m here is "+ str(m))
        if c[temp - 1 - k] == m:
            temp = (temp - 1 - k)
            # print("the previous vak of index"+ str(temp))
            break

    # print(sel)
    extra = sel[temp]
    print(extra)


n=int(input())
if n>=5 and n<=(2*pow(10,5)):
    arr=list(map(int,input().split()))
    # print(arr)
x=0
count=0
sel=[]
arr.sort()
# print(arr)
# print(m)


migratoryBirds(arr)