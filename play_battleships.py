import Battleships
while True:
    Battleships.Game().play()
    if input("New game? y/n: ") == "y":
        continue
    else: break
