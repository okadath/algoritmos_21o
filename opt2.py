with open('file.txt', "r") as my_file:
	a = my_file.readline().strip().split(' ')
	b = my_file.readline().strip().split(' ')

n = int(a[0])
k = int(a[1])
cadena = b[0]

caa=list(cadena)

# n_d = input().split()
# cadena = input()
# n = int(n_d[0])
# k = int(n_d[1])

cont = 0
letras = 0
maxim_rama = 0
maxim_rama2 = 0
#
back = 0
j = 0
fin = 0
lleno = False
maxx=0
val=0
j=0
aa=0
temp_i=0
i=0
for inicio in range(0, n):
	# print("inicio es" + str(inicio))
	# caa = list(cadena)
	if caa[inicio]=="D":
		cont = 0
		i=inicio
		while i<=n-1:
			i=i+1
			if cont>=k:
				break
			else:
				print(caa[i-1])
				print(i-1)
				if caa[i-1] == "A":
					# caa[i-1]="D"
					cont=cont+1
				if caa[i-1]=="D" and i==n-1:
					print("acaba")
					lleno=True
					break
	if lleno:
		maxx=n-inicio-cont
		break
	while(i<=n):
		if i==0:
			i=1
		# print(caa[i])
		if caa[i-1]=="A":
			if i==1:
				i=0
			break
		else:
			i=i+1
		# i=i+1
	fin=i-1
	val=fin-inicio-cont
	if val>maxx:
		maxx=val
		
print(maxx)
