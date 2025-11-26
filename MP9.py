#Ned Markus S. Basilio
#ICT-105

print("{:^100}".format("Try-Catch Practice"))

try:
	num1 = int(input("Enter a number: "))
	num2 = int(input("Enter another number: "))
	result = num1 / num2
	print("The result of division is: {:.2f}".format(result))
except ValueError:
	print("Invalid input. Please enter an integer")
except ZeroDivisionError:
	print("Erorr: Cannot divide by zero.")
except Exception as e:
	print(f"An unexpected error has occured: {e}")
else:
	print("Division performed successfully.")
finally:
	print("Execution complete.")

print("\f{:^100}\f".format("Match Case Practice"))

try:
	print("Operators:\nAddition: +\nSubtraction: -\nMultiplication: *\nDivison: /")

	operator = input("Enter an operator: ")
	x = 5
	y = 10

	match operator:
		case '+': result = x + y
		case '-': result = x - y
		case '*': result = x * y
		case '/': result = x / y
		case _: result = "Invalid Operation"
	
	print("\nResult:", result)

except ValueError:
	print("Invalid Input")
	


