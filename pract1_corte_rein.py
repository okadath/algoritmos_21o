import math


arr=int(input())

a=0
def recursion(i):
	global a
	if i==1:
		# print("base")
		# print(i)
		return 1
	else:
		
		if i%2==0:
			# print("par")
			# print(i)
			# global a
			a=a+combinatoria(i)
			# print(combinatoria(i))
			# print(a)
			return recursion(i/2)+recursion(i/2) # sospecho que aqui debo enviar
			# la suma entre cobunatoria de i y irla sumando pero no se
			# y en el caso base usar +0
		else:
			# print("impar")
			# print(i)
			# global a
			a=a+combinatoria(i)
			# print(combinatoria(i))
			# print(a)
			return recursion(math.ceil(i/2))+recursion(math.floor(i/2))
					# return (i)
		# return recursion(combinatoria(i))+recursion(combinatoria(i-1))




def combinatoria(n):
	return math.factorial(n)/(math.factorial(n-2)*math.factorial(2))

# print("final")
recursion(arr)
print(int(a))