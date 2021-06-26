from random import randint
from things import *
with open("hangmanwordlist.txt") as f:
    words = f.readlines()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

class Game:
    """Represents a game of hangman"""
    def __init__(self):
        """Create a game of hangman.
        Generates a random word from hangmanwordlist.txt,
        and initializes the game board."""
        with open("hangmanwordlist.txt") as f:
            words = f.readlines()
        self.word = words[randint(1,len(words))][:-1]
        self.num_round = 0
        self.word_guessed = False
        self.letters = [' ' for letter in self.word]
        self.victim = {x: " " for x in
                       ['head', 'body', 'larm', 'rarm', 'lleg', 'rleg']}
        self.alphabet = [' ' for letter in alphabet]
        self.wrongs = 0
        self.done = False

    def play(self):
        """Play the game of hangman.
        Runs self.round() in a loop until the word has been guessed,
        then prints a victory statement and whether the player
        really won or not.
        """
        self.num_round += 1
        while True:
            if self.done:
                print("Word was " + self.word.upper())
                break
            if self.word_guessed:
                print("YOU WIN! \n"
                      + "Guessed " + self.word.upper() + " with "
                      + str(self.wrongs) + " incorrect guesses.")
                if self.wrongs >= 7:
                    print("Unfortunately, you took too long and "
                          + "the man was hung.")
                break
            self.round()


    def round(self):
        """Main game loop. Prints the board, gets a guess as input,
        checks the guess against the word, prints a message
         if guess is wrong, then updates things as needed.
         """
        self.print()
        guess = input("Guess: ")
        if guess.isalpha():
            if guess == "exit" or guess == "stop":
                self.done = True
            elif guess.isupper():  # user is guessing the word
                if guess.lower() == self.word:
                    self.word_guessed = True
                else:
                    print("\nSorry, word is not " + guess)
                    self.wrongs += 1
                    self.num_round += 1
                    self.update_victim()

            elif guess.islower() and len(guess) ==1:
                # user is guessing a letter
                if occurs := char_occurrences(self.word, guess):
                    for i in range(len(occurs)):
                        self.letters[occurs[i]] = guess.upper()
                    if self.letters.count(' ') == 0:
                        self.word_guessed = True
                else:
                    print("\nSorry, no " + guess)
                    self.wrongs += 1
                    self.update_victim()

                self.num_round += 1
                self.alphabet[alphabet.index(guess)] = guess
            else:  # user messed up
                print("\nInvalid guess; use lower case for a letter (\'e\'), "
                      + "and upper case to guess the word (\'JAZZ\')")
        else:
            print("\nInvalid guess; use only letters")

    def update_victim(self):
        """Update the victim dictionary with the number of wrong guesses."""
        hangmen = {
            1: {'head': 'O'},
            2: {'body': '|'},
            3: {'larm': '/'},
            4: {'rarm': '\\'},
            5: {'lleg': '/'},
            6: {'rleg': '\\'},
            7: {'head': '@'}
        }
        self.victim.update(hangmen.get(self.wrongs, {}
                                       ))

    def print(self):
        """Print a beautiful render of the current game state."""
        print("\n      _______  \n"
              + "      |----\|     " + " ".join(self.alphabet[:6]) + "\n      "
              + self.victim.get('head')
              + "     |     " + " ".join(self.alphabet[6:12]) + "\n     "
              + self.victim.get('larm') + self.victim.get('body')
              + self.victim.get('rarm')
              + "    |     " + " ".join(self.alphabet[12:18]) + "\n     "
              + self.victim.get('lleg') + " " + self.victim.get('rleg')
              + "    |     " + " ".join(self.alphabet[18:24]) + "\n"
              + "    _______/|\_       " + " ".join(self.alphabet[24:]) + "\n"
              + "    |---------|\n"
              + "\n"
              + "  " + "   ".join(self.letters) + " \n"
              + " " + " ".join(["___" for i in self.letters]) + "\n"
              )

def __main__():
    while True:
        Game().play()