# Alexander Dinh, 17921667, Alexis Padilla, 36931764
# connectfour_console.py

import connectfour
import connectfour_shared

if __name__ == '__main__':
    game = connectfour.new_game()
    connectfour_shared.print_board(game)
    connectfour_shared.print_instructions()

    while True:
        move = connectfour_shared.get_proper_move(game)
        try:

            game = connectfour_shared.player_move(game, move)
            if connectfour.winner(game) == connectfour.RED:
                print('Red wins!')
                break
            if connectfour.winner(game) == connectfour.YELLOW:
                print('Yellow wins!')
                break

        except:
            print('ERROR: Invalid move. Please try again.')
