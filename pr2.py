# with open('file.txt', "r") as my_file:
# 	a = my_file.readline() 
# 	b = my_file.readline().strip().split(' ')

# n = int(a)
# cadena = b

n = int(input())
cadena = input().strip().split(' ')
# n = int(n_d[0])
# k = int(n_d[1])

# print(n)
mitad=int(len(cadena)/2)
# print(cadena[0:mitad])
# print(cadena[mitad:len(cadena)])

# print(cadena+cadena)

def recursion(arreglo,lenn):
	# global total
	# if len(arreglo)%2!=0:
	# print(len(arreglo))
	temp=[]
	for i in range(0,lenn):
		# print(lenn-i-1)
		temp.append(arreglo[lenn-i-1])
	# print(temp)
	arreglo=temp
	if lenn==2:
		c=[arreglo[0],arreglo[1]]
		# print(c)
		return c
	# if dias_restantes<=0:
	# # total=total+a+b+c
	# 	return 1
	else:
		# a=a*2
		mitad=lenn/2 
		a=arreglo[0:int(lenn/2)]
		b=arreglo[int(lenn/2):lenn]
		# mitad_1=recursion(a,int(lenn/2))
		# mitad_2=recursion(b,int(lenn/2))
		# print(len(arreglo))
		# return recursion(dias_restantes-1,a_hijos+a,b_hijos+b,c_hijos+c)#+recursion(a,dias_restantes-1)
		# return mitad_2+mitad_1
		return recursion(a,int(lenn/2))+recursion(b,int(lenn/2))

var=recursion(cadena,n)

# print(var)
for i in var:
	print(i+" ", end="" , flush=True)
# print("\n")
# print("final")
# asd=recursion(d,n,0,0)
# # print(asd)
# print(total)