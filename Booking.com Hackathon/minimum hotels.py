
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    if m<=p and p<=100 and m>0 and p>0 and d>0 and d<=100:
        count=0


        new=[]



        if(p<s):
            while (p >= m):
                if p < m:
                    break
                new.append(p)
                # print(new)
                p = p - d

                store = sum(new)
                # print(store)
                if store>s:
                    break
                count += 1
            # print(new)

            while (store <= s):
                new.append(m)
                # print(new)
                store = sum(new)
                if store > s:
                    break
                # print(store)
                count = count + 1
        else:
            count=0

    return(count)

pdms = input().split()

p = int(pdms[0])

d = int(pdms[1])

m = int(pdms[2])

s = int(pdms[3])

answer = howManyGames(p, d, m, s)

print(answer)
