# Alexander Dinh, 17921667, Alexis Padilla, 36931764
# connectfour_ui.py

import connectfour
import connectfour_shared
import connectfour_sp
import socket


def _run_user_interface() -> None:
    'Connects client to server and runs the game'
    host = _read_host()
    port = _read_port()
    # host = 'woodhouse.ics.uci.edu'
    # port = 4444
    username = _read_username()

    connection = None

    try:
        print('Connecting to Connect 4 server...')
        connection = connectfour_sp.connect(host, port)
        print('Connection Successful: ' + host + ', port ' + str(port))

        connectfour_sp.login(connection, username)
        _run_game(connection)

    except socket.gaierror:
        # exception for wrong host
        print('Connection failed: invalid host.')

    except TimeoutError:
        # exception for wrong port
        print('Connection failed: invalid port.')

    finally:
        print('Closing connection...')
        connectfour_sp.close(connection)

    print('Goodbye!')


def _read_host() -> str:
    'Gets server host address'
    while True:
        host = input('Host: ').strip()
        if host == '':
            print('You need to specify a host, please')
        else:
            return host


def _read_port() -> int:
    'Gets port of target server'
    while True:
        try:
            port = int(input('Port: '))

            if port < 0 or port > 65535:
                print('That is not a valid port; must be 0-65535')
            else:
                return port

        except ValueError:
            print('That is not a valid port; must be 0-65535')


def _read_username() -> str:
    'Returns user-specified username only if in correct format'
    while True:
        username = input('Username: ').strip()

        if username == '':
            print('That is not a username; please try again')

        elif ' ' in username:
            print('Please enter a username without spaces')

        else:
            return username


def _run_game(connection: connectfour_sp.GameConnection) -> None:
    'Game loop: creates new connectfour instance and handles player/AI moves'

    connectfour_sp.start_AI(connection)
    game = connectfour.new_game()
    connectfour_shared.print_board(game)
    connectfour_shared.print_instructions()

    while True:
        try:
            server_msg = connectfour_sp.read_line(connection) # must wait for server to send READY
            # print('Response from server: ' + server_msg)

            if server_msg == 'WINNER_RED':
                print('Red wins!')
                break

            if server_msg == 'WINNER_YELLOW':
                print('Yellow wins!')
                break

            if connectfour_shared.player_turn(game) == 'RED':
                message = connectfour_shared.get_proper_move(game)
                connectfour_sp.write_line(connection, message)
                game = connectfour_shared.player_move(game, message)

            elif connectfour_shared.player_turn(game) == 'YELLOW':
                game = connectfour_shared.player_move(game, server_msg)

        except:
            pass


if __name__ == '__main__':
    _run_user_interface()
