# Alexander Dinh, 17921667, Alexis Padilla, 36931764
# connectfour_sp.py
import socket
from collections import namedtuple

GameConnection = namedtuple('GameConnection', ['socket', 'socket_in', 'socket_out'])
WELCOME = 0


class LoginError(Exception):
    pass


def connect(game_host: str, game_port: int) -> GameConnection:
    game_socket = socket.socket()
    game_socket.connect((game_host, game_port))

    game_socket_in = game_socket.makefile('r') # pseudo-files
    game_socket_out = game_socket.makefile('w')

    return GameConnection(
        socket=game_socket,
        socket_in=game_socket_in,
        socket_out=game_socket_out)


def write_line(connection: GameConnection, line: str) -> None:
    connection.socket_out.write(line + '\r\n')
    connection.socket_out.flush()


def read_line(connection: GameConnection) -> str:
    return connection.socket_in.readline()[:-1]


def login(connection: GameConnection, username: str) -> WELCOME:
    login_msg = 'I32CFSP_HELLO ' + username
    write_line(connection, login_msg)

    response = read_line(connection)
    if response.startswith('WELCOME '):
        return WELCOME
    else:
        raise LoginError()


def start_AI(connection: GameConnection) -> None:
    write_line(connection, 'AI_GAME')


def close(connection: GameConnection) -> None:
    connection.socket.close()
    connection.socket_in.close()
    connection.socket_out.close()
