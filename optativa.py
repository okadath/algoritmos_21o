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






maxim_rama=0
lleno=0
for j in range(0,n):
	letras=0
	cont=k
	for i in range(j,n):
		print(cadena[i])
		print(j)
		if cadena[i]=="A":
			cont=cont-1
		else:
			letras=letras+1
		if i==n and cont>0:
			lleno=1
		if letras>maxim_rama:
				maxim_rama=letras
		if cont<0:
			
			break
	if lleno:
		break

			# letras=letras+1
print(maxim_rama)

# # animal