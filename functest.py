def multiplication_table(x):
	for i in range(1, user_input+1):
		for j in range(1, user_input+1):
			print(i*j, end="\t")
		print()

def star_pattern(x):

#upper half
	for k in range(0, x): 
		for i in range(k, x-1, 1):
			print(" ", end="")
		for l in range(0, k+1, 1):
			print("*", end="")
		for p in range(0, k, 1):
			print("*", end="")
		print()

#lower half
	for a in range(0, x):
		for b in range(1, a+2, 1):
			print(" ", end="")
		for c in range(x, a+1, -1):
			print("*", end="")
		for d in range(a+2, x, 1):
			print("*", end="")
		print()
		
		
# MAIN CODE
user_input = int(input("Input a number: "))
x = user_input

star_pattern(x)
