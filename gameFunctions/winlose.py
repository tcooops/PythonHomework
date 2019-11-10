from random import randint

def winorlose(status): 
	print("called win or lose", status)
	print("You", status + "! Would you like to play again?")
	choice = input("Y / N?")
	print(choice)

	if choice == "Y" or choice == "y":
		global player_lives
		global computer_lives
		global player
		global computer

		player_lives = 5
		computer_lives = 5
		computer = choices[randint(0,2)]

	elif choice == "N" or choice == "n":
		print("You chose to quit. Better luck next time!")
		exit()
	
	else:
		print("make a valid choice, Yes or No")
		