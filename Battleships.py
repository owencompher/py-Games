from random import randint


class Game:
    """Represents a game of battleships"""

    def __init__(self):
        self.battle_map = [[" "] * 10 for i in range(10)]
        self.display_map = [["|"] * 10 for i in range(10)]
        self.ships = [[4, 4, "battleship", ""],
                      [5, 5, "carrier   ", ""],
                      [3, 3, "cruiser   ", ""],
                      [3, 3, "submarine ", ""],
                      [2, 2, "destroyer ", ""]]
        for ship in self.ships:  # for generating the game board
            done = False
            while not done:  # process will repeat until empty spot is found and filled
                empty = True
                orient = randint(0, 1)
                if orient == 0:
                    location = [randint(0, (10 - ship[0])), randint(0, 9)]  # finds the starting spot
                    for i in range(location[0], (location[0] + ship[0])):  # of a range to try
                        if self.battle_map[i][location[1]] != " ":
                            empty = False
                    if empty:  # if those spots aren't taken
                        for i in range(location[0], (location[0] + ship[0])):  # places ship in those spots
                            self.battle_map[i][location[1]] = ship[2]
                            done = True
                    continue
                if orient == 1:
                    location = [randint(0, 9), randint(0, (10 - ship[0]))]
                    for i in range(location[1], (location[1] + ship[0])):
                        if self.battle_map[location[0]][i] != " ":
                            empty = False
                    if empty:
                        for i in range(location[1], (location[1] + ship[0])):
                            self.battle_map[location[0]][i] = ship[2]
                            done = True
                    continue
        self.hits = 0
        self.shots = 0

    def __str__(self):
        string = "\nShots fired: " + str(self.shots)
        for ship in self.ships:
            string += "\n" + ship[2] + " | " + " X" * (ship[0] - ship[1]) + " O" * ship[1] + "  " * (6 - ship[0]) + \
                      ship[3]
        return string

    def get_board(self):
        string = "\n   0  1  2  3  4  5  6  7  8  9  "
        for row in range(10):
            string += "\n" + str(row) + "--" + "--".join([x for x in self.display_map[row]]) + "--" + str(row)
        string += "\n   0  1  2  3  4  5  6  7  8  9  \n"
        return string

    def play(self):
        while self.hits < 17:
            print(self.get_board())
            guess = input("Guess: ")  # first gets player input
            if guess == "end":
                break
            guess.split()
            try:  # checks that the input is valid
                if self.battle_map[int(guess[-1])][int(guess[0])] == " ":  # checks for a miss
                    self.shots += 1
                    print(self)
                    print("miss")
                    self.display_map[int(guess[-1])][int(guess[0])] = "O"
                elif self.display_map[int(guess[-1])][
                    int(guess[0])] == "X":  # checks for a spot that has been already hit
                    self.shots += 1
                    print(self)
                    print("hit " + self.battle_map[int(guess[-1])][int(guess[0])] + " at " + guess[0] + ", " + guess[
                        -1] + " again")
                else:  # at this point the shot can only be a new hit
                    self.shots += 1
                    self.hits += 1
                    for ship in self.ships:  # runs through each ship
                        if self.battle_map[int(guess[-1])][int(guess[0])] == ship[2]:  # checks if ship was hit
                            if ship[1] > 1:  # checks that the ship isn't being sunk
                                ship[1] -= 1
                                print(self)
                                print("hit " + ship[2] + " at " + guess[0] + ", " + guess[-1])
                                self.display_map[int(guess[-1])][int(guess[0])] = "X"
                            else:  # the ship is being sunk
                                ship[1] -= 1
                                ship[3] = "sunk"
                                print(self)
                                print("sunk " + ship[2] + ", final hit at " + guess[0] + ", " + guess[-1])
                                self.display_map[int(guess[-1])][int(guess[0])] = "X"
            except ValueError:
                print(self)
                print("Bad input. Use format 'column row'")

        # once all ships have been sunk (17 unique hits) this runs
        print(
            "You won! Your score is " + str(117 - self.shots))  # score is out of 100, 100 meaning every shot was a hit.
        print(self.get_board())
