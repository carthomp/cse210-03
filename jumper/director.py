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
    
    def start_game(self):
        """
        """
        self.term_service.welcome()
        tries = self.current_parachute.get_tries()
        parachute = self.get_parachute(tries)
        self.term_service.display_parachute(parachute)
        self.do_game_loop()
    
    def get_parachute(self, tries):
        parachute = self.current_parachute.draw(tries)
        return parachute

    def get_input(self):
        """
        """
    
    def do_game_loop(self):
        """
        """
        while (self.keep_playing):
            guess = self.term_service.take_guess()
            word = self.current_word.word
            guess_status = self.term_service.compare_guess(word, guess)
            if guess_status:
                pass
            else:
                self.current_parachute.set_tries()
                tries = self.current_parachute.get_tries()
                parachute = self.get_parachute(tries)
                self.term_service.display_parachute(parachute)
            if self.end_game():
                break
    
    def end_game(self):
        """
        """
        if not self.keep_playing:
          print('Game over!')
          return True