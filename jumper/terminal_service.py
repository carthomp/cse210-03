class Terminal_Service():
    """
    """

    def __init__(self):
        """
        """
        self.guessed_letters = []
        self.incomplete_word = []

    def welcome(self):
        """
        Displays a welcome message here!
        """
        print("Welcome to the Jumper game!")
    
    def display_line(self):
        print("-----------------------------------------------------\n")
    
    def fill_incomplete_word(self, word):
        for i in range(len(word)):
            self.incomplete_word.append('_')
        print(f"This game, your word has {len(self.incomplete_word)} letters! Good luck!")

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
        correct = False
        index = 0
        for character in word:
            if character == guess:
                correct = True
                self.incomplete_word[index] = guess
            index += 1
        if correct:
            print("Good guess!")
            return True
        else:
            print("Wrong guess!")
            return False

    def display_parachute(self, parachute):
        print(parachute)
    
    def display_incomplete_word(self):
        for i in range(len(self.incomplete_word)):
            print(self.incomplete_word[i], end=" ")
        print()
    
    def check_word_complete(self):
        for i in range(len(self.incomplete_word)):
            if self.incomplete_word[i] == "_":
                return False
        return True

    def display_game_over(self, guesses):
        """
        Displays a "Game Over" message.
        """
        if guesses == 0:
            print('Game Over')
            return False
        elif guesses > 0:
            return True