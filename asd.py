print("Exam Score Tracker")

score = 0
total_questions = 0
score_add = 0

while score_add != -1:
	try:
		score_add = int(input("Type 1 to add 1 to your score, 0 if it's wrong. Type -1 if you are done: "))
	except ValueError:
		print("Invalid Value. Try Again")
	if score_add == 1:
		score += 1
		total_questions += 1
	elif score_add == 0:
		total_questions += 1

	print("Score =", score)
	print()

print(f"Total Score: {score}/{total_questions}")