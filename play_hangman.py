import Hangman
input("Guess letters with a single lowercase or the word in all caps.\nPress ENTER to begin")
while True:
	Hangman.Game().play()
	if input("New game? y/n: ") == "n":
		break
