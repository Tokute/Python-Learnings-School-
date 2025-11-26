user_input = input("Enter a word: ")

vowels = ['A', 'E', 'I', 'O', 'U']

for char in user_input.upper():
    if char in vowels:
        continue
    else:
        print(char, end="")