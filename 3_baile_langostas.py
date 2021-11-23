f_c=input().split()
data_init=input()
data = [int(x) for x in data_init.split(" ")]

# a=n_k.split(" ")
# print(a)
f=int(f_c[0])
c=int(f_c[1])

# print(f)
# print(c)
# print(data)
# a=[None]*f
# a=[None]*7
# print(a)
results=[]
# results=[[None]*f]*c
for i in range(0,c):
	results.append([])
# print(a)
print(results)
min_val=0
for i in range(0,c):
	print("primer ciclo")
	# print(results[i][f-1])
	# if results[i][f-1]==None:
	for j in range(0, f):
		print("inicia segundo ciclo")
		print(min_val)
		added=0

		for val in range(0, f*c):
			print (val)
			print(results)
			if data[val]==min_val:
				print("i="+str(i)+"- j="+str(j)) 
				results[i].append(min_val)
				# results[i][j]=min_val
				added=added+1
			# if added:
				# j=j-1
		if added==0:
			j=0
		min_val=min_val+1
	# else:
		# min_val=i[f-1]

print(data)

print(results)





