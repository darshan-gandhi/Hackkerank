def gradingStudents(grades):
    for i in grades:
        if i >= 0 and i <= 100:
            # print(i)
            x = 0
            if int(i) >= 35:
                # print(i)
                x = i % (5)
                # print(str(x))
                if x >= 3:
                    i = i + (5 - (x))
                    # print(str(i))
                    sec.append(i)
                else:
                    sec.append(i)
            else:
                sec.append(i)
n=int(input())
grades=[]
sec=[]
x=0
if n>=1 and n<=60:
    for i in range(n):
        grades.append(int(input()))

gradingStudents(grades)
print(*sec,sep="\n")

