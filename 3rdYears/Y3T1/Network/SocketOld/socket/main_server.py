import socket
import threading
from datetime import datetime

# Dictionary of songs
SONGS = {
    1: "Song1.mp3",
    2: "Song2.mp3",
    3: "Song3.mp3"
}

# Dictionary of song lyrics
LYRICS = {
    1: "These are the lyrics for Song1",
    2: "These are the lyrics for Song2",
    3: "These are the lyrics for Song3"
}

# Dictionary of lyrics file paths
LYRICS_FILES = {
    1: "D:\\AB-BiMaGOoOD\\Tob-taun\\3rdYears\\Y3T1\\Network\\SERVER\\PowerIsPower.txt",
    2: "lyrics2.txt",
    3: "lyrics3.txt"
}

def handle_client_connection(client_socket):
    while True:
        # Send the list of songs to the client
        song_list = "\n".join([f"{key}: {value}" for key, value in SONGS.items()])
        client_socket.send(song_list.encode('utf-8'))
        
        # Receive the command from the client
        command = client_socket.recv(1024).decode('utf-8')
        
        if command == "I":
            # Send application information
            info = "Music List Application: View and select songs from a list."
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
                    lyrics = LYRICS[int(song_id)]
                    client_socket.send(lyrics.encode('utf-8'))
                elif lyrics_choice == "C":
                    file_path = LYRICS_FILES[int(song_id)]
                    with open(file_path, 'rb') as file:
                        client_socket.sendfile(file)
            else:
                response = "Song not found"
                client_socket.send(response.encode('utf-8'))
        elif command == "N":
            # End the client session
            client_socket.send(b"Goodbye!")
            client_socket.close()
            break
        else:
            # Invalid command
            client_socket.send(b"Invalid command. Please enter 'I', 'Y', or 'N'.")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 1115))
    server.listen(5)
    print("Server listening on port 1115")

    while True:
        client_socket, addr = server.accept()
        
        # Log the day and time of connection
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"Accepted connection from {addr} at {current_time}")
        
        client_handler = threading.Thread(target=handle_client_connection, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
