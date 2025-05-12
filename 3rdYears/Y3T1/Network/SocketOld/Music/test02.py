import socket

# Define server address and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12000

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_HOST, SERVER_PORT))

try:
    while True:
        # Receive the list of commands from the server
        commands = client_socket.recv(1024).decode()
        print(commands)
        """Round 01"""
        # Choose a command
        choice = input("> ").strip()
        if choice.lower() == 'exit':
            break
        client_socket.sendall(choice.encode())
        """Round 02"""
        # Receive the server's response
        response = client_socket.recv(1024).decode()
        print(response)
        if choice.lower() == 'y' :
            while True:
                # Receive the list of songs from the server
                song_list = client_socket.recv(1024).decode()
                print(song_list)
                
                # Choose a song
                choice = input("Enter the number of the song you want to listen to (or 'exit' to disconnect): ").strip()
                if choice.lower() == 'exit':
                    break
                client_socket.sendall(choice.encode())

                # # Receive the server's response
                # response = client_socket.recv(1024).decode()
                # print(response)
        elif choice.lower() == 'n':
            break
finally:
    # Close the socket
    client_socket.close()
    print("Disconnected from server.")
