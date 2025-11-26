#Ned

for i in range(0, 10, 1):
	print((10-i)*" ", end="")
	for j in range(0, 5, 1):  
		print("*", end="")  
	for k in range(0, 2, 1):
		if (i == 5): # Makes the middle line
			print(i*"*", end="")
		else:
			print(i*" ", end="")
	for l in range(0, 5, 1):
		print("*", end="")
	print()










"""
for i in range(0, 10, 1):
	print((10-i)*" ", end="") # Creates space for the first diagonal of A 
	for j in range(0, 5, 1):
		print("*", end="")
	for k in range(0, 2, 1):
		if (i == 5): # Makes the middle line sa A
			print(i*"*", end="")
		else:
			print(i*" ", end="")
	for l in range(0, 5, 1):
		print("*", end="")
	print()	
"""