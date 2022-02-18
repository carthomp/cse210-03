from jumper.word import Word
from jumper.parachute import Parachute
from jumper.terminal_service import Terminal_Service


class Director():
    """
    Directs the management of the game by starting it and running the loop that progresses it.
    Attributes:
        keep_playing (bool) - whether the game should continue or not
        play_again (str) - stores a 'y' to play again or a 'n' to not
        current_word - instance of Word
        current_parachute - instance of Parachute
        term_service - instance of Terminal Service
        tries (int) - the number of tries
        won (bool) - whether or not the player won the game
    """

    def __init__(self):
        """
        Initializes this instance of Director.
        Arguments:
            self - an instance of the Director class.
        """
        self.keep_playing = True
        self.play_again = ""
        self.current_word = Word()
        self.current_parachute = Parachute()
        self.term_service = Terminal_Service()
        self.tries = 0
        self.won = False

    def start_game(self):
        """
        Starts the game by calling the welcome method, setting the tries, displaying
        the parachute, picking a word and storing it, and starting the game loop.
        Arguments:
            self - an instance of the Director class.
        """
        self.term_service.welcome()
        self.tries = self.current_parachute._get_tries()
        # self.show_incomplete_word()
        parachute = self.get_parachute(self.tries)
        self.term_service.display_parachute(parachute)
        self.current_word._pick_word()
        word = self.current_word._set_word()
        self.term_service.fill_incomplete_word(word)
        # self.get_input()
        self.do_game_loop()
        self.end_game()

    # def show_incomplete_word(self):

    #     for _ in range(self.number_word):
    #         self.incomplete_word = self.incomplete_word + "_"
    #     print(self.incomplete_word)
    #     print(self.word)

    def get_parachute(self, tries):
        """
        Gets the parachute string from current_parachute for use by other class methods.
        Arguments:
            self - an instance of the Director class.
            tries - the current number of wrong guesses
        """
        parachute = self.current_parachute._draw(tries)
        return parachute

    def do_game_loop(self):
        """
        The main loop of the game, which takes a guess, compares it to the word, and behaves accordingly
        to if the guess was right or wrong.
        Arguments:
            self - an instance of the Director class.
        """
        while (self.keep_playing):
            self.term_service.display_line()
            guess = self.term_service.take_guess()
            word = self.current_word._set_word()
            guess_status = self.term_service.compare_guess(word, guess)
            number_word = len(word)
            if guess_status:
                # for i in range(self.number_word):
                #     if guess == list(self.word)[i]:
                #         list_letters = list(self.incomplete_word)
                #         list_letters[i] = guess
                #         self.incomplete_word = "".join(list_letters)
                pass

            else:
                self.current_parachute._set_tries()

            # print(self.incomplete_word)
            tries = self.current_parachute._get_tries()
            if tries > 4:
                self.keep_playing = False
            else:
                parachute = self.get_parachute(tries)
                self.term_service.display_parachute(parachute)
                self.term_service.display_incomplete_word()
            if self.term_service.check_word_complete():
                self.keep_playing = False
                self.won = True

    def end_game(self):
        """
        Ends the game, displaying a certain message if the player has won, and a different one if they lost.
        Arguments:
            self - an instance of the Director class.
        """
        if self.won:
            print("You win! Congratulations!")
        else:
            print("Game over!")
            print(f"The word was: {self.current_word._set_word()}")

    def do_play_again(self):
        self.play_again = input("Would you like to play again? (y/n) ")
        if self.play_again.lower() == 'y':
            return True
        return False