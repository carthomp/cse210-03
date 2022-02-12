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
        self.current_word.pick_word()
        self.word = str(self.current_word.set_word())
        self.word = self.word.replace("['","")
        self.word = self.word.replace("']","")
        self.number_word = len(self.word)
        self.incomplete_word = ""
    
    def start_game(self):
        """
        """
        self.term_service.welcome()
        self.tries = self.current_parachute.get_tries()
        self.show_incomplete_word()
        parachute = self.get_parachute(self.tries)
        self.term_service.display_parachute(parachute)
        #self.get_input()
        self.do_game_loop()
        self.end_game()

    def show_incomplete_word(self):
        
        for _ in range(self.number_word):
            self.incomplete_word = self.incomplete_word + "_"
        print(self.incomplete_word)
        print(self.word)
    
    def get_parachute (self,tries):
        parachute = self.current_parachute.draw(tries)
        return parachute

    def do_game_loop(self):
        """
        """
        while (self.keep_playing):
            guess = self.term_service.take_guess()
            
            guess_status = self.term_service.compare_guess(self.word, guess)
            
            if guess_status:
                for i in range(self.number_word):
                    if guess == list(self.word)[i]:
                        list_letters = list(self.incomplete_word)
                        list_letters[i] = guess
                        self.incomplete_word = "".join(list_letters)
                                                  
            else:
                self.current_parachute.set_tries()

            print(self.incomplete_word)
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