def countingValleys(n, s):
    result = []
    for i in s:
        result.append(i)

    # print(result)

    # result1=result
    # print(result1)
    result1 = []
    for i in result:
        if (i=='U') or (i=='D'):
            if i == 'U':
                result1.append("1")
            elif i == 'D':
                result1.append("-1")
    count = 0
    # print(result1)
    sum1 = 0
    extra=[]
    for i in range(len(result1)):
        sum1 = sum1 + int(result1[i])
        # print(f"the sum is {sum1}")
        extra.append(sum1)
        # print(extra)
        if (sum1 == 0) and (extra[i-1]<0):
            count = count + 1
            # print(f"the runnin count is {count}")
    print(count)

n=int(input())
s=input()
countingValleys(n,s)