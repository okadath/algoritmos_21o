with open( 'file.txt',"r") as my_file:
	a=my_file.readline().strip().split(' ') 
	b=my_file.readline().strip().split(' ') 

n=int(a[0])
k=int(a[1])
cadena=b[0]




n_d=input().split()
cadena=input()
n=int(n_d[0])
k=int(n_d[1])


cont=k
letras=0
maxim_rama=0
maxim_rama2=0
#
lleno=0
back=0
j=0
fin=0

while j<=n:
	letras=0
	for i in range (j,n):
		ch=cadena[i]
		# print(i)
		if i == n and cont > 0:
			lleno = 1
		if cont>0:
			if cadena[i]=="A":
				cont=cont-1
			else:
				letras=letras+1
		else:
			if cadena[i]=="A":
				count=0
				fin=1
				break
			else:
				letras=letras+1
		if letras > maxim_rama:
			maxim_rama = letras
		# if lleno:
		# 	lleno = 0
		# 	break
	if fin=1:
		j=i
	j=j+1



cont=k
letras=0
# maxim_rama=0
back=0
j=n
lleno=0
while j>=0:
	letras=0
	# print(j)
	i=j-1
	while i>=0:
	# for i in range (n,j):
	# 	print(i)
		ch=cadena[i]
		# print(i)
		if i == n and cont > 0:
			lleno = 1
		if cont>0:
			if cadena[i]=="A":
				cont=cont-1
			else:
				letras=letras+1
		else:
			if cadena[i]=="A":
				count=0
				break
			else:
				letras=letras+1
		if letras > maxim_rama:
			maxim_rama = letras
		i=i-1
	if lleno:
		lleno=0
		break
	j=j-1

print(maxim_rama)
# print(letras)