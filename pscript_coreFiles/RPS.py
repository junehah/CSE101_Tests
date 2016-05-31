import random

def pickPrinter(x):
	# Expects x to be 1, 2 or 3
	if x == 1:
		return "Rock"
	elif x == 2:
		return "Paper"
	else:
		return "Scissors"

def playRockPaperScissors(n):
	userWin = 0
	computerWin = 0

	for rounds in range(0,n):
		pick = int(input("Choose one: 1. Rock  2. Paper  3. Scissors\n>> "))
		while True:
			if pick != 1 and pick != 2 and pick != 3:
				pick = int(input("You have to pick 1, 2 or 3! Try again.\n>> "))
			else:
				break
		computerPick = random.randrange(1,4)

		print("You picked " + pickPrinter(pick))
		print("Computer picked " + pickPrinter(computerPick))

		if pick == computerPick:
			print("It's a tie!\n")
		elif pick == 1:
			if computerPick == 3:
				userWin += 1
				print(pickPrinter(pick) + " beats " + pickPrinter(computerPick))
				print("You win!\n")
			else:
				computerWin += 1
				print(pickPrinter(computerPick) + " beats " + pickPrinter(pick))
				print("Computer wins\n")
		else:
			if pick > computerPick:
				userWin += 1
				print(pickPrinter(pick) + " beats " + pickPrinter(computerPick))
				print("You win!\n")
			else:
				computerWin += 1
				print(pickPrinter(computerPick) + " beats " + pickPrinter(pick))
				print("Computer wins\n")

	# The rounds of play are over
	print("You won " + str(userWin) + " rounds.")
	print("Computer won " + str(computerWin) + " rounds.")
	if userWin == computerWin:
		print("You tied the computer.")
	elif userWin > computerWin:
		print("You beat the computer!")
	else:
		print("The computer beat you.")

#playRockPaperScissors(3)
