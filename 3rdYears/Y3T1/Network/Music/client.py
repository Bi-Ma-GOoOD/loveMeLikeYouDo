import socket

# Define server address and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12000

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_HOST, SERVER_PORT))

try :
    while True :
        # Receive the list of songs from the server
        song_list = client_socket.recv(1024).decode()
        print("Available songs:")
        print(song_list)

        # Choose a song
        choice = input("Enter the name of the song you want to listen to: ")
        if choice.lower() == 'exit':
            break
        client_socket.sendall(choice.encode())

        # Receive the server's response
        response = client_socket.recv(1024).decode()
        print(response)
finally :
    # Close the socket
    client_socket.close()