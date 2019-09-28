def birthday(s, d, m):
    t=0
    i=0
    c=0
    for a in range(len(s)-1):
        t=0
        i=a
        print(str(i)+ "is MAIN of i")
        while i<(a+m):
            print(str(a+m) + "is main value")
            print(str(i)+"value of i is")
            t=t+s[i]
            print(t)
            i=i+1
        if t==d:
            c=c+1
            print("the count is incremented")

    return(c)

n = int(input().strip())

s = list(map(int, input().rstrip().split()))

dm = input().rstrip().split()

d = int(dm[0])

m = int(dm[1])

result = birthday(s, d, m)

print(result)