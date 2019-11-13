# import the random package so we can generate a random AI choice
from random import randint
from gameFunctions import winlose, gameVars, compare


while gameVars.player is False:
	print("                           ")
	print("~*~*~*~*~*~*~*~*~*~*~*~*~*~")
	print("                           ")
	print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
	print("                           ")
	print("~*~*~*~*~*~*~*~*~*~*~*~*~*~")
	print("                           ")
	print("Choose your weapon!\n")
	print("                           ")
	print("~*~*~*~*~*~*~*~*~*~*~*~*~*~")
	print("                           ")
	player=input("choose rock, paper or scissors: \n")
	print("                           ")
	print("~*~*~*~*~*~*~*~*~*~*~*~*~*~")
	print("                           ")

	# "compare." links the compare page. "compareChoices" links the function
	compare.compareChoices (player)
	
	if gameVars.player_lives is 0:
		winlose.winorlose("lost")

	elif gameVars.computer_lives is 0:
		winlose.winorlose("won")

	else:
		player = False
		gameVars.computer = gameVars.choices[randint(0,2)]