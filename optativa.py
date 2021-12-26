with open( 'file.txt',"r") as my_file:
	a=my_file.readline().strip().split(' ') 
	b=my_file.readline().strip().split(' ') 

n=int(a[0])
k=int(a[1])
cadena=b[0]



# n_d=input().split() 
# cadena=input() 
# n=int(n_d[0])
# k=int(n_d[1])




cont=k
letras=0
maxim_rama=0
maxim_rama2=0

i=0
# while i<n:

for j in range(0,n):
	letras=0
	for i in range(j,n):
		print(cadena[i])
		print(i)
		print(cont)
		print(letras)
		print("   ")

		# print(j)
		if cadena[i]=="A":
			cont=cont-1
		else:
			letras=letras+1 
		if letras>maxim_rama:
			maxim_rama=letras
				
		if cont<0:
			# print("a")
			letras=0
			cont=k
		i=i+1

# cont=k
# letras=0
# # maxim_rama=0
# maxim_rama2=0
# i=n-1
# while i>=0:
# 	# pass
# 	print(cadena[i])
# 	print(i)
# 	print(cont)
# 	print("   ")
# 	# print(j)
# 	if cadena[i]=="A":
# 		cont=cont-1
# 	else:
# 		letras=letras+1 
# 	if letras>maxim_rama2:
# 		maxim_rama2=letras
			
# 	if cont<0:
# 		print("a")

# 		letras=0
# 		cont=k
# 	i=i-1
			# letras=letras+1
print(maxim_rama)
# print(maxim_rama2)

# # animal