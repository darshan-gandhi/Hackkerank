for i in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	m=a[n-1]
	b=0
	for i in range(2,len(a)+1):
		# print(f"the value of i is {i}")
		# print(a[-i])
		if a[-i]>m:
			b+=1
			# print("count is increased")
		m=min(m,a[-i])
		# print(f"m is {m}")
	print()
	print(b)
