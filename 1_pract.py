n_d=input().split()

# print(a)
n=int(n_d[0])
d=int(n_d[1])

total=n
def recursion(dias_restantes,a,b,c):
	global total
	if a==0:
		return 0
	if dias_restantes<=0:
	# total=total+a+b+c
		return 1
	else:
		# a=a*2

		a_hijos=1*a+0*b+1*c
		b_hijos=3*a+2*b+0*c
		c_hijos=1*a+2*b+4*c
		total=total+a_hijos+b_hijos+c_hijos
		return recursion(dias_restantes-1,a_hijos+a,b_hijos+b,c_hijos+c)#+recursion(a,dias_restantes-1)

# print("final")
asd=recursion(d,n,0,0)
# print(asd)
print(total)