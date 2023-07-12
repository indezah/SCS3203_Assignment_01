import socket
import sys

if(len(sys.argv) != 2):
    print('Usage: python3 {} <port>'.format(sys.argv[0]))
    sys.exit()
    
# Define the server's IP address and port
SERVER_IP = '127.0.0.1'  # Loopback address for localhost
SERVER_PORT = int(sys.argv[1])

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific IP address and port
server_socket.bind((SERVER_IP, SERVER_PORT))

# Listen for incoming connections
server_socket.listen(1)
print('Server is listening on {}:{}'.format(SERVER_IP, SERVER_PORT))

# Accept a client connection
client_socket, client_address = server_socket.accept()
print('Accepted connection from {}:{}'.format(client_address[0], client_address[1]))

# Receive data from the client
data = ''
while(data != 'q'):
    data = client_socket.recv(1024)
    if(data.decode() == 'q'):
        break
    print('Received data from client:', data.decode())


# Close the connection
client_socket.close()
server_socket.close()
