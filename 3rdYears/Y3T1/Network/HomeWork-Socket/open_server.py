import socket
import threading
from datetime import datetime
import os

# Dictionary of songs
SONGS = {
    1: "Hit-Me-Where-the-Heart-Is",
    2: "I-Like-the-Way-You-Kiss-Me",
    3: "Power-Is-Power",
    4: "Stress-Out",
    5: "Sweather-Weather"
}

# Dictionary of song lyrics file paths
LYRICS_FILES = {
    1: "D:\\AB-BiMaGOoOD\Tob-taun\\3rdYears\\Y3T1\\Network\\SERVER\\HitMeWhereTheHeartIs.txt",
    2: "D:\\AB-BiMaGOoOD\\Tob-taun\\3rdYears\\Y3T1\\Network\\SERVER\\ILikeTheWayYouKissMe.txt",
    3: "D:\\AB-BiMaGOoOD\\Tob-taun\\3rdYears\\Y3T1\\Network\\SERVER\\PowerIsPower.txt",
    4: "D:\\AB-BiMaGOoOD\\Tob-taun\\3rdYears\\Y3T1\\Network\\SERVER\\StressOut.txt",
    5: "D:\\AB-BiMaGOoOD\\Tob-taun\\3rdYears\\Y3T1\\Network\\SERVER\\SweatherWeather.txt"
}
# Check song count for modified
SONG_COUNT = [0, 0, 0, 0, 0, 0]

def send_file(client_socket, file_path, new_file_name):
    try:
        file_size = os.path.getsize(file_path)
        header = f"{new_file_name}:{file_size}".encode('utf-8')
        header += b' ' * (1024 - len(header))  # Pad the header to 1024 bytes

        client_socket.send(header)

        with open(file_path, 'rb') as file:
            while (chunk := file.read(1024)):
                client_socket.send(chunk)
        client_socket.send(b'EOF')
        print("BiMaGOoOD : File transfer complete")
    except Exception as e:
        client_socket.send(f"Error: {e}".encode('utf-8'))

def handle_client_connection(client_socket, addr):
    try:
        while True:
            song_list = "\n".join([f"{key}: {value}" for key, value in SONGS.items()])
            client_socket.send(song_list.encode('utf-8'))
            
            command = client_socket.recv(1024).decode('utf-8')
            print(f"BiMaGOoOD : Received command: {command} from {addr[1]}")
            if command == "I":
                info = "This is song's list you can read all lyric's song that server has, or you can download lyric's song file\n- - - - - - - - - -\n\n"
                client_socket.send(info.encode('utf-8'))
            elif command == "Y":
                song_id = client_socket.recv(1024).decode('utf-8')
                print(f"BiMaGOoOD : Received song ID: {song_id} from {addr[1]}")
                if song_id.isdigit() and int(song_id) in SONGS:
                    selected_song = SONGS[int(song_id)]
                    client_socket.send(f"Selected {selected_song}. Do you want to read lyrics in the (P)prompt or as a (C)file? (P/C)".encode('utf-8'))
                    
                    lyrics_choice = client_socket.recv(1024).decode('utf-8')
                    print(f"BiMaGOoOD : Received lyrics choice: {lyrics_choice} from {addr[1]}")
                    if lyrics_choice == "P":
                        lyrics_path = LYRICS_FILES[int(song_id)]
                        songs_name = SONGS[int(song_id)]
                        SONG_COUNT[int(song_id)] += 1
                        if SONG_COUNT[int(song_id)] == 1:
                            print(f"BiMaGOoOD : This is a first time to call {songs_name}.")
                            print(f"BiMaGOoOD : {songs_name} was modified at time {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
                            print(f"BiMaGOoOD : Status code 200 - accepted")
                        elif SONG_COUNT[int(song_id)] >= 1:
                            print(f"BiMaGOoOD : Status code 304 - Not Modified and move permanently")
                        try:
                            with open(lyrics_path, 'r') as file:
                                while (chunk := file.read(1024)):
                                    client_socket.send(chunk.encode('utf-8'))
                            client_socket.send(b'EOF')
                            print(f"BiMaGOoOD : Sent EOF marker to {addr[1]} for stop transfer file to command prompt.")
                        except Exception as e:
                            client_socket.send(f"BiMaGOoOD : Error reading file: {e} from {addr[1]}".encode('utf-8'))
                    elif lyrics_choice == "C":
                        file_path = LYRICS_FILES[int(song_id)]
                        new_file_name = client_socket.recv(1024).decode('utf-8')
                        print(f"BiMaGOoOD : Received new file name: {new_file_name} from {addr[1]}")
                        send_file(client_socket, file_path, new_file_name)
                    else :
                        client_socket.send(b"SERVER : Goodbye!")
                        client_socket.close()
                        logout_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
                        print(f"BiMaGOoOD : (DISCONNECTION) - Client from address {addr[1]} was disconnected at \t\t{logout_time}.")
                        break
                else:
                    print(f"BiMaGOoOD : Song not found from {addr[1]}")
                    response = "Song not found"
                    client_socket.send(response.encode('utf-8'))
            elif command == "N":
                client_socket.send(b"SERVER : Goodbye!")
                client_socket.close()
                logout_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
                print(f"BiMaGOoOD : (DISCONNECTION) - Client from address {addr[1]} was disconnected at \t\t{logout_time}.")
                break
            else:
                print(f"BiMaGOoOD : Status code 404 - Error command\nBiMaGOoOD : Invalid command from {addr[1]}")
                # client_socket.send(b"Invalid command. Please enter 'I', 'Y', or 'N'.")
    except ConnectionResetError:
        print(f"BiMaGOoOD : (DISCONNECTION) - Client from address {addr[1]} was disconnected unexpectedly.")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # server.settimeout(60)
    server.bind(('127.0.0.1', 1115))
    server.listen(5)
    print("\n\t\t* * * Server activated * * *")
    print("\t\tServer listening on port 1115")

    while True:
        client_socket, addr = server.accept()
        login_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        print(f"BiMaGOoOD : (CONNECTION) - Accepted connection from {addr} at \t\t{login_time}")
        client_handler = threading.Thread(target=handle_client_connection, args=(client_socket, addr))
        client_handler.start()

if __name__ == "__main__":
    start_server()