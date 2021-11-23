import math


n_d=input().split()

# print(a)
n=int(n_d[0])
d=int(n_d[1])

total=0
def recursion(a,dias_restantes):
	global total
	if dias_restantes<=1:
		total=total+a
		return a
	else:
		total=total+a

		a=a*2
		return recursion(a,dias_restantes-1)#+recursion(a,dias_restantes-1)

# print("final")
asd=recursion(n,d)
print(asd)
print(total)