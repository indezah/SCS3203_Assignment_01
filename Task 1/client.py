import socket
import sys

if(len(sys.argv) != 3):
    print('Usage: python3 {} <ip> <port>'.format(sys.argv[0]))
    sys.exit()

# Define the server's IP address and port
SERVER_IP = sys.argv[1]
SERVER_PORT = int(sys.argv[2])

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_IP, SERVER_PORT))
print('Connected to {}:{}'.format(SERVER_IP, SERVER_PORT))

data = ''
# Send data to the server
while(data != 'q'):
    data = input('Enter data to send (q to quit): ')
    client_socket.sendall(data.encode())

# Close the connection
client_socket.close()
