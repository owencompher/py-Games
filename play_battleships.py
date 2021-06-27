import Battleships
input("Input guesses in 'column row' format.\nPress ENTER to begin")
while True:
    Battleships.Game().play()
    if input("New game? y/n: ") == "y":
        continue
    else: break
