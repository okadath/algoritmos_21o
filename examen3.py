# with open('file.txt', "r") as my_file:
# 	a = my_file.readline()  

# n_ini = int(a) 



n_ini = int(input()) 
 

def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            # print("No es primo", n, "es divisor")
            return False
    # print("Es primo")
    return True

b=False



def recursion(n):
	# div=n
	b=es_primo(n)
	# print(b)
	# print(n)
	# print(n_ini)
	if n==1:
		print("0 0")
	if  b==True and n==n_ini:
		print(str(n)+" 0" )
		# return  
	else:
		for  val in range(2, n+1):
			# print(val)
			primo_1=es_primo(val)
			if primo_1==True:
				primo_2= n_ini -val
				# print(primo_2)
				val_primo_2=es_primo(primo_2)
				if val_primo_2==True:
					# print("caso 2")
					print(str(primo_2)+" "+str(val))
					return True
			elif val==n_ini:
				print("0 0")
				return True



recursion(n_ini)


# def recursion(arreglo,lenn):
# 	temp=[]
# 	for i in range(0,lenn):
# 		# print(lenn-i-1)
# 		temp.append(arreglo[lenn-i-1])
# 	# print(temp)
# 	arreglo=temp
# 	if lenn==2:
# 		c=[arreglo[0],arreglo[1]]
# 		# print(c)
# 		return c
# 	else:
# 		mitad=lenn/2 
# 		a=arreglo[0:int(lenn/2)]
# 		b=arreglo[int(lenn/2):lenn]
# 		return recursion(a,int(lenn/2))+recursion(b,int(lenn/2))

# var=recursion(cadena,n)



# for i in var:
# 	print(i+" ", end="" , flush=True)