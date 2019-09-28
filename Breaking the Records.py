n=int(input())
if n>=1 and n<=1000:
    sel=list(map(int,input().split()))


count=0
count1=count
arr=[]
min=sel[0]
max=sel[0]
for x in sel:
    if x>=1 and x<=pow(10,8):
        for j in range(len(sel)):
            arr.append(sel[j])
            for i in range(len(arr)):
                if i != 0:
                    if arr[i] > max:
                        max = arr[i]
                        count = count + 1

            for k in range(len(arr)):
                if k != 0:
                    if arr[i] < min:
                        min = arr[i]
                        count1 = count1 + 1

        print(str(count) + " " + str(count1))
        break
