def climbingLeaderboard(scores,alice):
    for j in alice:
        if j >= 0 and j <= pow(10, 9):
            x = j
            for i in scores:
                if i >= 0 and i <= pow(10, 9):
                    scores.append(x)
                    # print(scores)
                    scores.sort()
                    scores.reverse()
                    extra = scores.index(x)
                    # print(f"the new ele is now at {extra} {x}")
                    # print(scores)
                    func1(scores, extra)
                    break

def func1(scores,extra):
    rank = 1
    ansmain=[]
    y=0
    score1.clear()
    score1.append(1)

    # print(score1)
    for i in range(1,len(scores)):
        # # print(rank)
        # y=0
        # # score1.append(rank)
        # y=(1-i)
        # if y==0:
        #     print(f"the val of i is {i}")
        #     score1.append(rank)
        #     print("i am here")
        #     print(score1)
        # else:
        #     print(f"the val of i is {i}")
            if scores[i] == scores[i - 1]:
                # print(rank)
                score1.append(rank)
            else:
                rank += 1
                # print(rank)
                score1.append(rank)
    # print(score1)
    save.append(score1[extra])

# inputs
n=int(input())
if n>=2 and n<=pow(10,5):
    scores = list(map(int, input().split()))
m=int(input())
if m>=2 and m<=pow(10,5):
    alice = list(map(int, input().split()))
save=[]

# sorting the array for the first time
scores.sort()
scores.reverse()
score1=[]
# print(scores)

#calling the func for first time
extra=0
func1(scores,extra)

#calling the func again n again
climbingLeaderboard(scores,alice)

del save[0]
print(*save,sep="\n")