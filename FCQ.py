#FQuiz

#Ned Markus S. Basilio
#ICT-105

def letter_B(character):
	for i in range(0, 50, 1): # LIMIT CONTROLS THE LENGTH (50)
		if (i == 0) or (i == 24) or (i == 49):	#determines if it prints spaces or not
			do_nothing = 0
		elif (3 <= i <= 21) or (27 <= i <= 46):	# gives curve
			print(character, 50*" " ,sep="", end=character)
		else:
			print(character, 49*" " ,sep="", end=character)
		for j in range(0, 50, 1): #prints the characters
			if (i == 0) or (i == 24) or (i == 49): 
				print(character, end="")
			else:
				print("", end="")
		print()


# int main() {

do_nothing = 0

while True:
	try:
		character = input("Please choose a character to print: ")
	except ValueError:
		print("Invalid Input")

	letter_B(character)

	repeat = input("Would you like to try again? (y/n): ")
	if repeat.lower() != 'y':
		break
	else:
		continue
	

"""
backup code
for i in range(0, 10, 1):
	if (i == 1) or (i == 2) or (i == 3) or (i == 5) or (i == 6) or (i == 7):
		print("*", 3*" " ,sep="", end="*")
	for j in range(0, 4, 1):
		if (i == 1) or (i == 2) or (i == 3) or (i == 5) or (i == 6) or (i == 7):
			print("", end="")
		else:
			print("*", end="")
		
	
	print()
"""