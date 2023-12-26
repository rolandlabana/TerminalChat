import socket
import threading

# Function to handle client connections
def handle_client(client_socket):
    while True:
        # Receive message from the client
        client_message = client_socket.recv(1024).decode('utf-8')
        print(f"Received from client: {client_message}")
        
        # Exit loop if client sends 'exit'
        if client_message.lower() == 'exit':
            break
        
        # Send a response to the client
        server_message = input("Enter your message: ")
        client_socket.send(server_message.encode('utf-8'))

    # Close the client socket
    client_socket.close()

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name and port
host = '127.0.0.1'
port = 9999

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)
print("Server listening on port 9999...")

while True:
    # Accept incoming connection
    client_sock, addr = server_socket.accept()
    print(f"Connection established with {addr[0]}:{addr[1]}")

    # Create a new thread to handle the client connection
    client_thread = threading.Thread(target=handle_client, args=(client_sock,))
    client_thread.start()

