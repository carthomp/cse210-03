from jumper.word import Word
from jumper.parachute import Parachute
from jumper.terminal_service import Terminal_Service

class Director():
    """
    """
    def __init__(self):
        """
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
        """
        self.term_service.welcome()
        self.tries = self.current_parachute.get_tries()
        parachute = self.get_parachute(self.tries)
        self.term_service.display_parachute(parachute)
        self.current_word.pick_word()
        word = self.current_word.set_word()
        self.term_service.fill_incomplete_word(word)
        #self.get_input()
        self.do_game_loop()
        self.end_game()
    
    def get_parachute (self,tries):
        parachute = self.current_parachute.draw(tries)
        return parachute

    def do_game_loop(self):
        """
        """
        while (self.keep_playing):
            self.term_service.display_line()
            guess = self.term_service.take_guess()
            word = self.current_word.set_word()
            guess_status = self.term_service.compare_guess(word, guess)
            number_word = len(word)
            if guess_status:
                pass
            else:
                self.current_parachute.set_tries()
            tries = self.current_parachute.get_tries()
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
        """
        if self.won:
            print("You win! Congratulations!")
        else:
            print("Game over!")
            print(f"The word was: {self.current_word.set_word()}")