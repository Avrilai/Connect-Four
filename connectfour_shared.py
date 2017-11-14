# Alexander Dinh, 17921667, Alexis Padilla, 36931764
# connectfour_shared.py

import collections
import connectfour

GameState = collections.namedtuple('GameState', ['board', 'turn'])


def print_instructions() -> None:
    'Prints desired syntax of game commands for player and AI'
    print('INSTRUCTIONS: ')
    print('To drop a disc into a column, type "DROP [column number]"')
    print('To pop a disc from a column, type "POP [column number]"')


def print_board(game: GameState) -> None:
    'GameState is a 6x7 array, prints a rotated board so that each column is its own array'
    for col in range(1, connectfour.BOARD_COLUMNS + 1):
        print(col, end=' ')
    print()
    counter = 0
    for row in range(len(game.board[0])):
        for col in range(len(game.board)):
            if game.board[col][row] == 0:
                print('.', end=' ')

            elif game.board[col][row] == 1:
                print('R', end=' ')

            elif game.board[col][row] == 2:
                print('Y', end=' ')

            counter = counter + 1  # allows creation of the rows of the board
            if counter == connectfour.BOARD_COLUMNS:
                counter = 0
                print()
    print()


def get_proper_move(game: GameState) -> str:
    'To be used with player_move(); returns user move only if in the correct format'
    while True:
        move = input('[Turn: {}] What is your move? '.format(player_turn(game)))
        move = move.upper()

        if move.startswith('DROP ') or move.startswith('POP '):
            return move

        else:
            print('ERROR: Invalid move. Please try again.')


def player_move(game: GameState, move: str) -> GameState:
    'Prompts the player to drop a game piece into a specified column'

    mode, col = move.split(' ', 1)
    col = int(col) - 1  # account for array indexing, which starts at 0

    if mode == 'DROP':
        game = connectfour.drop(game, col)
        print_board(game)
        return game

    elif mode == 'POP':
        game = connectfour.pop(game, col)
        print_board(game)
        return game


def player_turn(game: GameState) -> str:
    'Returns the color of the player whose turn it is'
    if game.turn == 1:
        return 'RED'
    elif game.turn == 2:
        return 'YELLOW'
