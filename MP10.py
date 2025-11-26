#Ned Markus S. Basilio
#ICT-105

try:
	user_month = int(input("Enter your birth month: "))
	user_day = int(input("Enter your birth day: "))

	match user_month:
		case 1:
			if (1 <= user_day <= 19):
				print("Your Zodiac Sign is Capricornus (Goat)")
			elif (20 <= user_day <= 31):
				print("Your Zodiac Sign is Aquarius (Water Bearer)")
		case 2:
			if (1 <= user_day <= 18):
				print("Your Zodiac Sign is Aquarius (Water Bearer)")
			elif (19 <= user_day <= 28):
				print("Your Zodiac Sign is Pisces (Fish)")
		case 3:
			if (1 <= user_day <= 20):
				print("Your Zodiac Sign is Pisces (Fish)")
			elif (21 <= user_day <= 31):
				print("Your Zodiac Sign is Aries (Ram)")
		case 4:
			if (1 <= user_day <= 19):
				print("Your Zodiac Sign is Aries (Ram)")
			elif (20 <= user_day <= 30):
				print("Your Zodiac Sign is Taurus (Bull)")
		case 5:
			if (1 <= user_day <= 20):
				print("Your Zodiac Sign is Taurus (Bull)")
			elif (21 <= user_day <= 31):
				print("Your Zodiac Sign is Gemini (Twins)")
		case 6:
			if (1 <= user_day <= 21):
				print("Your Zodiac Sign is Gemini (Twins)")
			elif (22 <= user_day <= 30):
				print("Your Zodiac Sign is Cancer (Crab)")
		case 7:
			if (1 <= user_day <= 22):
				print("Your Zodiac Sign is Cancer (Crab)")
			elif (23 <= user_day <= 31):
				print("Your Zodiac Sign is Leo (Lion)")
		case 8:
			if (1 <= user_day <= 22):
				print("Your Zodiac Sign is Leo (Lion)")
			elif (23 <= user_day <= 30):
				print("Your Zodiac Sign is Virgo (Virgin)")
		case 9:
			if (1 <= user_day <= 22):
				print("Your Zodiac Sign is Virgo (Virgin)")
			elif (23 <= user_day <= 30):
				print("Your Zodiac Sign is Libra (Balance)")
		case 10:
			if (1 <= user_day <= 23):
				print("Your Zodiac Sign is Libra (Balance)")
			elif (24 <= user_day <= 31):
				print("Your Zodiac Sign is Scorpius (Scorpion)")
		case 11:
			if (1 <= user_day <= 21):
				print("Your Zodiac Sign is Scorpius (Scorpion)")
			elif (22 <= user_day <= 30):
				print("Your Zodiac Sign is Sagittarius (Archer)")
		case 12:
			if (1 <= user_day <= 21):
				print("Your Zodiac Sign is Sagittarius (Archer)")
			elif (22 <= user_day <= 31):
				print("Your Zodiac Sign is Capricornus (Goat)")
		case _:
			print("Invalid Month")

except ValueError:
	print("Invalid Input")
	

