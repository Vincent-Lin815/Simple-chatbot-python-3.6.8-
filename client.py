import socket

HOST = '127.0.0.1'
PORT = 8888

# create a socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# initiatively connect with HOST 
client.connect((HOST, PORT))

# message input
print(str(client.recv(1024), encoding = 'utf-8'))

while True:

    data = input('What do you want to ask:')
    client.sendall(data.encode())
    if data == 'q':
        break
    else:

        # message from server    
        serverMessage = str(client.recv(1024), encoding = 'utf-8')
        print('Server:', serverMessage)

client.close()

