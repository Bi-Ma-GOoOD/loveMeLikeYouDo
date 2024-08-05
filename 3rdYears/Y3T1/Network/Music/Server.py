from socket import *

# Define Host, Port server
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12000
i = 0

# List of available songs
songs = ["song1", "song2", "song3", "song4"]
show = ["lala", "lulu", "lele", "lolo"]

# Create a TCP/IP socket
server_socket = socket(AF_INET, SOCK_STREAM)
# Bind the socket to the address and port
server_socket.bind((SERVER_HOST, SERVER_PORT))

# Server is listening
print('\n^.^ Server Activated ^.^\n')
# Listen for incoming connections
server_socket.listen(5)
print(f"Server listening on {SERVER_HOST} : {SERVER_PORT}")

def handle_client(client_socket):
    global i
    numberClient = i
    try:
        while True:
            # Send the list of songs to the client
            client_socket.sendall("\n".join(show).encode())

            # Receive the song choice from the client
            choice = client_socket.recv(1024).decode()
            # choice = recv_choice.lower()
            if choice.lower() in songs:
                response = f"You chose {choice}. Enjoy the music!"
            else:
                response = "Invalid choice. Please choose a valid song."
            
            client_socket.sendall(response.encode())
    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        print(f"Client {numberClient} disconnected.")
        i = i - 1
        # Close the client socket
        client_socket.close()

while True:
    # Accept a new client connection
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from client {i} -> {client_address}")
    # Increment the number of clients
    i = i + 1
    # Handle the client in a separate function
    handle_client(client_socket)