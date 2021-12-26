n_d=input().split()

# # print(a)

n=int(n_d[0])
animal=[]
mares=[]

for i in range(0,n):
	n_d=input().split()
	# animal=int(n_d[0])
	# mar=int(n_d[1])
	animal.append(int(n_d[0]))
	mares.append(int(n_d[1]))

# array=[1,2,3,3,2]
# mares=[1,2,1,2,2]
# value_index = array.index(3)	

# print(value_index)
# print(animal)
# print(mares[1])


count=0
for i in range(0,len(animal)):
	# mares=0
	Mojado_2_mares=False
	Mojado_1_mar=False
	animal_actual=animal[i]
	mar_actual=mares[i]


	for j in range(0, len(animal)):
		# if animal_actual==animal[j]:
			# 
		if animal_actual==animal[j] and i!=j:
			if mar_actual!=mares[j]:
				if Mojado_1_mar==True:
					
					break

				Mojado_1_mar=True
				count=count+1

	# 	# Mojado_1_mar=True
	# 	# if Mojado_1_mar=True and mar[i]!=mares:
	# 	# print(mar)
	# 	# print(mares[j])
	# 	if mares[j]!=mar and :
			
	# 		Mojado_2_mares=True
	# 		count=count+1
	# 		# mo
	# 		break
print(count)
	