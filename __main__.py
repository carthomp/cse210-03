from jumper.director import Director

play_again = True
while play_again:
    director = Director()
    director.start_game()
    play_again = director.do_play_again()