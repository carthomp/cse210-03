class Terminal_Service():
    """
    """

    def __init__(self):
        """
        """
        self.guessed_letters = []

    def welcome(self):
        """
        Displays a welcome message here!
        """
        print("Welcome to the Jumper game!")

    def take_guess(self):
        """
        Prompts the user to enter a letter, and avoids common errors such as repeated guesses
        """
        guess = input("Enter a letter: ")
        try_again = True
        while try_again:
            if len(guess) > 1:
                print("Please enter only one letter!")
                guess = input("Enter a letter: ")
                try_again = True
            elif guess in self.guessed_letters:
                print(f"You have already guessed the letter {guess}!")
                guess = input("Enter a letter: ")
                try_again = True
            else:
                try_again = False
                self.guessed_letters.append(guess)
        return guess

    def compare_guess(self, word, guess):
        if guess not in word:
            print("Wrong guess")
            return False
        elif guess in word:
            print('Keep going')
            return True

    def display_parachute(self, parachute):
        print(parachute)

    def display_game_over(self, guesses):
        """
        Displays a "Game Over" message.
        """
        if guesses == 0:
            print('Game Over')
            return False
        elif guesses > 0:
            return True
