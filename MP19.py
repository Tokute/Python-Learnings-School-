# CODE IS VERY SCUFFED (FIRST TIME USING FUCNTIONS AND I DIDN'T KNOW USING  GLOBAL VARIABLES INSIDE FUNCTIONS WAS BAD

menu_prices = []

def titlepage():
	print("\n", "-"*4, "ChicBurg Mart", "-"*4, sep="")
	print("[1] Meals\n[2] Pasta\n[3] Burger\n[4] Dessert\n[5] Drinks\n[0] Exit")

def meals():
	global menu_prices
	print('-'*4, "Meals", '-'*4, sep=" ")
	meals_menu = ["[A] 1 Piece Chicken with Rice", "[B] 2 Piece Chicken with Rice", "[C] 6 Pieces Nuggets with Fries", "[D] 2 Piece Burger Steak with Rice"]
	meals_prices = [99, 170, 100, 109]
	menu_prices.extend(meals_prices)
	for meal in meals_menu:
		print(meal)

def pasta():
	global menu_prices
	print("\n", "-"*4, "Pasta", "-"*4, sep=" ")
	pasta_menu = ["[A] Cream Carbonara", "[B] Classic Spaghetti", "[C] Traditional Pancit", "[D] Extra Large Spaghetti"]
	pasta_prices = [99, 89, 90, 85]
	menu_prices.extend(pasta_prices)
	for pasta in pasta_menu:
		print(pasta)
	

def burger():
	global menu_prices

	print("\n", "-"*4, "Burger", "-"*4, sep=" ")
	burger_menu = ["[A] Original Burger", "[B] Double Burger", "[C] Special Cheeseburger", "[D] Orignial Burger Lettuce"]
	burger_prices = [60, 110, 90, 150]
	menu_prices.extend(burger_prices)
	for burger in burger_menu:
		print(burger)

def dessert():
	global menu_prices
	print("\n", "-"*4, "Dessert", "-"*4, sep=" ")
	dessert_menu = ["[A] Vanilla Ice Cream", "[B] Chocolate Ice Cream", "[C] Jelly-Filled Donut", "[D] Nut-Filled Donut(Bavarian)"]
	dessert_prices = [50, 60, 50, 80]
	menu_prices.extend(dessert_prices)
	for dessert in dessert_menu:
		print(dessert)

def drinks():
	global menu_prices
	print("\n", "-"*4, "Drinks", "-"*4, sep=" ")
	drinks_menu = ["[A] Coca Cola", "[B] Royal", "[C] Sprite", "[D] Boba Tea/Milk Tea"]
	drinks_prices = [40, 35, 40, 60]
	menu_prices.extend(drinks_prices)
	for drink in drinks_menu:
		print(drink)


def calculate_order():
	global menu_prices
	global user_choice

	order_quantity = int(input("Quantity?: "))
	total_price = menu_prices[user_choice] * order_quantity
	print(f"Your order total is: {total_price:,.2f}")
	user_cash = int(input("Amount Tendered: "))
	user_change = user_cash - total_price

	if user_change >= 0:
		print(f"Your change is Php {user_change:,.2f}")
	else:
		print("Not enough cash. Try again.")

retry = -99

# RUNNING CODE BELOW

user_menu = ""

while True:
	titlepage()
	try:
		user_menu = int(input("CHOICE: "))

	except ValueError:
		print("Invalid Input.")
	
	match (user_menu):
		case 0: # Exit
			print("Thank you for visiting ChicBurg Mart")
			break
		case 1: # Meals
			while True:
				meals()
				try:
					menu_choice = input("CHOICE: ")
					match menu_choice.upper():
						case 'A':
							user_choice = 0
							calculate_order()
						case 'B':
							user_choice = 1
							calculate_order()
						case 'C':
							user_choice = 2
							calculate_order()
						case 'D':
							user_choice = 3
							calculate_order()
					retry = input("Would you like to try again? (y/n): ")
					if retry.lower() == 'y':
						continue
					elif retry.lower() == 'n':
						break
					else:
						print("Invalid Input")
						break
					retry = -99


				except ValueError:
					print("Invalid Choice")
		case 2: #pasta
			while True:
				pasta()
				try:
					menu_choice = input("CHOICE: ")
					match menu_choice.upper():
						case 'A':
							user_choice = 0
							calculate_order()
						case 'B':
							user_choice = 1
							calculate_order()
						case 'C':
							user_choice = 2
							calculate_order()
						case 'D':
							user_choice = 3
							calculate_order()
					retry = input("Would you like to try again? (y/n): ")
					if retry.lower() == 'y':
						continue
					elif retry.lower() == 'n':
						break
					else:
						print("Invalid Input")
						break
					retry = -99
				except ValueError:
					print("Invalid Choice")
		case 3: # burger
			while True:
				burger()
				try:
					menu_choice = input("CHOICE: ")
					match menu_choice.upper():
						case 'A':
							user_choice = 0
							calculate_order()
						case 'B':
							user_choice = 1
							calculate_order()
						case 'C':
							user_choice = 2
							calculate_order()
						case 'D':
							user_choice = 3
							calculate_order()
					retry = input("Would you like to try again? (y/n): ")
					if retry.lower() == 'y':
						continue
					elif retry.lower() == 'n':
						break
					else:
						print("Invalid Input")
						break
					retry = -99


				except ValueError:
					print("Invalid Choice")
		case 4: # dessert
			while True:
				dessert()
				try:
					menu_choice = input("CHOICE: ")
					match menu_choice.upper():
						case 'A':
							user_choice = 0
							calculate_order()
						case 'B':
							user_choice = 1
							calculate_order()
						case 'C':
							user_choice = 2
							calculate_order()
						case 'D':
							user_choice = 3
							calculate_order()
					retry = input("Would you like to try again? (y/n): ")
					if retry.lower() == 'y':
						continue
					elif retry.lower() == 'n':
						break
					else:
						print("Invalid Input")
						break
					retry = -99


				except ValueError:
					print("Invalid Choice")
		case 5: # drinks
			while True:
				drinks()
				try:
					menu_choice = input("CHOICE: ")
					match menu_choice.upper():
						case 'A':
							user_choice = 0
							calculate_order()
						case 'B':
							user_choice = 1
							calculate_order()
						case 'C':
							user_choice = 2
							calculate_order()
						case 'D':
							user_choice = 3
							calculate_order()
					retry = input("Would you like to try again? (y/n): ")
					if retry.lower() == 'y':
						continue
					elif retry.lower() == 'n':
						break
					else:
						print("Invalid Input")
						break
					retry = -99


				except ValueError:

					print("Invalid Choice")
