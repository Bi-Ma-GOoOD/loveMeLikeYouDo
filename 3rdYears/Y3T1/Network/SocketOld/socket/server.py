import socket
import threading
from datetime import datetime

# Dictionary of songs
SONGS = {
    1: "Song1.mp3",
    2: "Song2.mp3",
    3: "Song3.mp3"
}

# Dictionary of song lyrics file paths
LYRICS_FILES = {
    1: "D:\\AB-BiMaGOoOD\\Tob-taun\\3rdYears\\Y3T1\\Network\\SERVER\\PowerIsPower.txt",
    2: "lyrics2.txt",
    3: "lyrics3.txt"
}

def handle_client_connection(client_socket, addr):
    try:
        while True:
            # Send the list of songs to the client.
            song_list = "\n".join([f"{key}: {value}" for key, value in SONGS.items()])
            client_socket.send(song_list.encode('utf-8'))
            
            # Receive the command from the client.
            command = client_socket.recv(1024).decode('utf-8')
            # Check command received with the choice that server has.
            if command == "I":
                # Send application information.
                info = "Music List Application: View and select songs from a list.\n- - - - - - - - - -\n\n"
                client_socket.send(info.encode('utf-8'))
            elif command == "Y":
                # Handle song selection
                song_id = client_socket.recv(1024).decode('utf-8')
                if song_id.isdigit() and int(song_id) in SONGS:
                    selected_song = SONGS[int(song_id)]
                    client_socket.send(f"Selected {selected_song}. Do you want to read lyrics in the prompt or as a file? (P/C)".encode('utf-8'))
                    
                    # Receive the choice for reading lyrics
                    lyrics_choice = client_socket.recv(1024).decode('utf-8')
                    if lyrics_choice == "P":
                        lyrics_path = LYRICS_FILES[int(song_id)]
                        try:
                            with open(lyrics_path, 'r') as file:
                                while (chunk := file.read(1024)):
                                    client_socket.send(chunk.encode('utf-8'))
                            client_socket.send(b'EOF')
                        except Exception as e:
                            client_socket.send(f"Error reading file: {e}".encode('utf-8'))
                    elif lyrics_choice == "C":
                        file_path = LYRICS_FILES[int(song_id)]
                        try:
                            with open(file_path, 'rb') as file:
                                while (chunk := file.read(1024)):
                                    client_socket.send(chunk)
                            client_socket.send(b'EOF')  # Send a signal to indicate the end of file transmission
                        except Exception as e:
                            client_socket.send(f"Error reading file: {e}".encode('utf-8'))
                else:
                    response = "Song not found"
                    client_socket.send(response.encode('utf-8'))
            elif command == "N":
                # End the client session.
                client_socket.send(b"Goodbye!")
                client_socket.close()
                logout_time = datetime.now().strftime('%d-%Y-%m %H:%M:%S')
                print(f"(DISCONNECTION) - Client from address {addr[1]} was disconnected at \t\t{logout_time}.")
                break
            else:
                # Invalid command.
                client_socket.send(b"Invalid command. Please enter 'I', 'Y', or 'N'.")
    except ConnectionResetError:
        print(f"(DISCONNECTION) - Client from address {addr[1]} was disconnected unexpectedly.")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 1115))
    server.listen(5)
    print("\n* * * Server activated * * *")
    print("\tServer listening on port 1115")

    while True:
        # Server accepted connection.
        client_socket, addr = server.accept()
        # Create date and time when client was connected to the server.
        login_time = datetime.now().strftime('%d-%Y-%m %H:%M:%S')
        print(f"(CONNECTION) - Accepted connection from {addr} at \t{login_time}")
        # Create multiple threads for each client.
        client_handler = threading.Thread(target=handle_client_connection, args=(client_socket, addr))
        client_handler.start()

if __name__ == "__main__":
    start_server()
