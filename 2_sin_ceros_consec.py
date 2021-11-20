n_k=input()
a=n_k.split(" ")
# print(a)
n=a[0]
k=a[1]

array=[]
# n -> longitud cadena
# k -> # de ceros
def recursion(n,k,cadena,stri):
	global array
	if n<0:
		return 1
	if k<0:
		return 1
	if n==0 :#and k==0:
		# cadena=cadena+"1"
		# return 1-
		if stri=="1":
			cadena=cadena+"1"
		else:
			cadena=cadena+"0"
			k=k-1
		print("n="+str(n))
		print("k="+str(k))
		print(cadena)
		if k>=0:
			array.append(cadena)


	else:
		print(cadena)
		# array.append(cadena)
		# array.append(cadena)
		if stri=="1":
			cadena=cadena+"1"
		else:
			cadena=cadena+"0"
			k=k-1
		return recursion(n-1,k,cadena,"0"),recursion(n-1,k,cadena,"1")
		# else:
			# cadena=cadena+"0"

			# recursion(n-1,k-1,cadena,"0")

recursion(int(n)-1,int(k),"","0")
recursion(int(n)-1,int(k),"","1")
print(array)
print(len(array))