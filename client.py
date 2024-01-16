
# (c) 2023 Roland Labana 
import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name and port
host = '127.0.0.1'
port = 9999

# Connect to the server
client_socket.connect((host, port))

while True:
    # Send a message to the server
    message = input("Enter your message: ")
    client_socket.send(message.encode('utf-8'))
    
    # Receive the server's response
    server_response = client_socket.recv(1024).decode('utf-8')
    print(f"Received from server: {server_response}")
    
    # Exit loop if 'exit' is entered
    if message.lower() == 'exit':
        break

# Close the client socket
client_socket.close()

