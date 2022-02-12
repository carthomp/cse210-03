# Director 
Responsibility: (start the game, do the game loop, end it if it's over, call other classes/methods to do things, ask if they want to play again with a new word) [PARENT]
```
    Attributes:
    --+ keep_playing (bool)
    --+ play_again (string)
    --+ current_word (instance of Word class)
    --+ current_parachute (instance of Parachute class)
    --+ term_service (instance of Terminal Service)
    Methods:
    --+ start_game
    --+ show_incomplete_word
    --+ get_input
    --+ do_game_loop
    --+ end_game
```
---
# Terminal Service 
Responsibility: (input and output from console, including guesses) [CHILD]
```
    Methods:
    --+ welcome
    
    --+ take_guess
    --+ display_parachute
    --+ display_game_over
```
---
# Word 
Responsibility: (provide a random word from a word list for the puzzle) [CHILD]
```
    Attributes:
    --+ word_list (list of strings)
    --+ word (string)
    Methods:
    --+ pick_word
    --+ set_word
```
---
# Parachute
Responsibility: (draw the parachute, tell Director if the player loses, calculate guesses) [CHILD]
```
    Attribute:
    --+ parachute (string)
    Methods:
    --+ update_parachute
    --+ set_parachute
    --+ update_lives
```