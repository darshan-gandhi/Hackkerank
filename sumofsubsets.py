n=int(input())
s=[]
for i in range(n):
    s.append(int(input()))
print(s)
count=0
d=0
for i in range(len(s)):
    sum1=0
    sum1=sum(s[i:])
    if d==sum1:
        count=count+1
print(count+1)

