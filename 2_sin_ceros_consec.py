n_k=input()
a=n_k.split(" ")
# print(a)
n=a[0]
k=a[1]

array=[]
# n -> longitud cadena
# k -> # de ceros
def recursion(n,k,cadena):
	global array
	if n==0 :#and k==0:
		# cadena=cadena+"1"
		# return 1-
		array.append(cadena)

	else:
		array.append(cadena)
		cadena=cadena+"1"
		# array.append(cadena)

		recursion(n-1,k-1,cadena)


recursion(int(n),int(0),"")
print(array)