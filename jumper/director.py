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
    
    def start_game(self):
        """
        """
        self.term_service.welcome()
        self.tries = self.current_parachute.get_tries()
        parachute = self.get_parachute()
        self.term_service.display_parachute(parachute)
        #self.get_input()
        self.do_game_loop()
        self.end_game()
    
    def get_parachute(self):
        parachute = self.current_parachute.draw(self.tries)
        return parachute

    def do_game_loop(self):
        """
        """
        while (self.keep_playing):
            guess = self.term_service.take_guess()
            word = self.current_word.set_word
            guess_status = self.term_service.compare_guess(word, guess)
            number_letters = len(word)
            if guess_status:
                tries = self.current_parachute.get_tries()
                parachute = self.get_parachute(tries)
                self.term_service.display_parachute(parachute)   
            else:
                self.current_parachute.set_tries()
                tries = self.current_parachute.get_tries()
                parachute = self.get_parachute(tries)
                self.term_service.display_parachute(parachute)
            for i in number_letters:
                if guess.lower() == i.lower():
                    print (guess.upper(), end='')
                else:
                    print ("_", end='')

            print ()
            if self.end_game():
                break
    
    def end_game(self):
        """
        """
        if not self.keep_playing:
          print('Game over!')
          return True