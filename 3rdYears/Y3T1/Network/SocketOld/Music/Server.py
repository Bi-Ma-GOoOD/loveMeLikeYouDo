from socket import *

# Define Host, Port server
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12000
i = 0

# Dictionary of available songs
dic_songs = {
    "1": "Shape of You by Ed Sheeran",
    "2": "Despacito by Luis Fonsi",
    "3": "Uptown Funk by Mark Ronson",
    "4": "Perfect by Ed Sheeran",
    "5": "Closer by The Chainsmokers",
    "6": "Thinking Out Loud by Ed Sheeran",
    "7": "Sorry by Justin Bieber",
    "8": "See You Again by Wiz Khalifa",
    "9": "Roar by Katy Perry",
    "10": "Dark Horse by Katy Perry"
}

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
            song_list = "\n".join([f"{key}: {value}" for key, value in dic_songs.items()])
            client_socket.sendall(song_list.encode())

            # Receive the song choice from the client
            choice = client_socket.recv(1024).decode().strip()
            if choice in dic_songs:
                song_name = dic_songs[choice]
                response = f"You chose {song_name}. Enjoy the music!"
            else:
                response = "Invalid choice. Please choose a valid song."
            
            client_socket.sendall(response.encode())
    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        print(f"Client at address {client_address[1]} disconnected.")
        # Close the client socket
        client_socket.close()

while True:
    # Accept a new client connection
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")
    # Handle the client in a separate function
    handle_client(client_socket)
