import socket
import select
import sys
import errno
HEADER= 10
IP = socket.gethostbyname(socket.gethostname())
PORT = 5050

myUsername = input("Username: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

username = myUsername.encode('utf-8')
usernameHeader = f"{len(username):<{HEADER}}".encode('utf-8')
client_socket.send(usernameHeader+username)
while True:
    message = input(f'{myUsername}: ')
    if message:
        message = message.encode('utf-8')
        messageHeader = f"{len(message):<{HEADER}}".encode('utf-8')
        client_socket.send(messageHeader+message)

    try:
        while True:
            usernameHeader = client_socket.recv(HEADER)
            if not len(usernameHeader):
                print('Connection closed by the server')
                sys.exit()
            usernameLength = int(usernameHeader.decode('utf-8'))
            username = client_socket.recv(usernameLength).decode('utf-8')
            messageHeader = client_socket(HEADER)
            messageLength = int(messageHeader.decode('utf-8'))
            message = client_socket.recv(messageLength).decode('utf-8')
            print(f"{username}: {message}")

    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()

        continue

    except Exception as e:
        print('Reading error: '.format(str(e)))
        sys.exit()
