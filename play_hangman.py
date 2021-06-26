import Hangman
while True:
	Hangman.Game().play()
	if input("New game? y/n: ") == "n":
		break
