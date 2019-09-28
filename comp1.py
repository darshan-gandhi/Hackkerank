def splitTheArray(val):
    save = []
    main1 = []
    # answer=arr[0]
    answer = 0
    x = 0
    extra=[]
    for i in range(len(val)):
        if int(val[i])>2 and int(val[i])<=pow(10,6):
            i = x
            for j in range((i+1), len(val)):
                x = 0
                y = 0
                answer = 0
                x = val[i]
                y = val[j]
                answer = gcd(val[i], val[j])
                # print(answer)
                if answer > 1:
                    # save.clear()
                    print(f"the val of i is {i} and j is {j}")
                    # print(f"the value of is}")
                    save = val[i:j + 1]
                    print(save)
                    main1.append(save)
                    print(main1)
                    x = j + 1
                    if main1[-1] not in extra:
                        extra.append(main1[-1])
                        print(extra)
                    break
                else:
                    print(f"the val of i {i}")
                    save= val[i:j]
                    print(save)
                    main1.append(save)
                    x=j
                    extra.append(main1[-1])
                    print(extra)
                    if i==-1:
                        extra.append(val[-1])
                    break
                    # print(f"the x val is {x}")

            # print(answer)
            # for k in range(x,y+1):
            #     print(f"the val of i is {i} and j is {j}")
            #     print(f"the value of is {arr[k]}")
            #     save.append(arr[k])
            #     main1.append(save)
            #     print(main1)
            # print(main1)
    print(len(extra))


def gcd(a, b):
    # print(f"the value is {a} and {b}")
    x=0
    while int(b) > 0:
        x=int(a)%int(b)
        # print(x)
        a, b = b,x
    # print(a)
    return int(a)


n=int(input())
val=[]
for i in range(n):
    if n>=1 and n<=pow(10,5):
        val.append(int(input()))

# print(arr)
# print(arr)
splitTheArray(val)