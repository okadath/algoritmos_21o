import math


arr=int(input())

def recursion(i):
	if i==1:
		print("base")
		print(i)
		return 1
	else:
		
		if i%2==0:
			print("par")
			print(i)
			print(combinatoria(i))
			return recursion(int(i/2))+recursion(int(i/2))
		else:
			print("impar")
			print(i)
			return recursion(int(math.ceil(i/2)))+recursion(int(math.floor(i/2)))
					# return (i)
		# return recursion(combinatoria(i))+recursion(combinatoria(i-1))


def factorial(num): 
    if num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact

def combinatoria(n):
	return factorial(n)/(factorial(n-2)*factorial(2))

print("final")
print(recursion(arr))