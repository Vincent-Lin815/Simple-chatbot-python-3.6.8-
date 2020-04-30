import socket
import random

# set our HOST and PORT
HOST = '127.0.0.1'
PORT = 8888

# define a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# binding the port
server.bind((HOST, PORT))
# start TCP listening, waiting for client to connect
server.listen(5)
# passively create a connection with the client
con, addr = server.accept()

con.sendall(bytes('Welcome to !(press q to quit chatting)', encoding = 'utf-8'))
while True:

    clientMessage = str(con.recv(1024), encoding = 'utf-8')
    if clientMessage == 'q':
        break
    else:
        print('Receive message is:', clientMessage)
        seed = random.randint(0, 9)

        serverMessage = [
            'What the fuck are you saying?',
            'Great minds have purpose, others have wishes.', 
            'Success is the ability to go from one failure to another with no loss of enthusiasm.', 
            'You make me sick!', 
            'What’s your problem?', 
            'Leave me alone.', 
            'Let’s cut the crap and get to the points.', 
            'Don’t bother me! I’ve had enough!', 
            'You’re impossible!', 
            'You eat with that mouth?', 
        ]
            

        # send message
        con.sendall(serverMessage[seed].encode())
        # close
server.close()

