import socket

def receive_file(client_socket):
    header = client_socket.recv(1024).decode('utf-8').strip()
    new_file_name, file_size = header.split(':')
    file_size = int(file_size)
    received_size = 0

    with open(new_file_name, 'wb') as file:
        while received_size < file_size or header == b'EOF':
            data = client_socket.recv(1024)
            if not data:
                break
            file.write(data)
            received_size += len(data)
    print(f"Lyrics file received as '{new_file_name}'")

def connect_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 1115))
    
    while True:
        song_list = client.recv(4096).decode('utf-8')
        print("\n- - - - - - - - - - Song'g List - - - - - - - - - -")
        print(song_list)
        
        print("\nOptions:")
        print("I - Information about the application")
        print("Y - Select a song to play")
        print("N - Exit")
        command = input("Enter your choice: ")
        client.send(command.encode('utf-8'))
        
        if command == "I":
            info = client.recv(1024).decode('utf-8')
            print(info)
        elif command == "Y":
            song_id = input("Enter the ID of the song to play: ")
            client.send(song_id.encode('utf-8'))
            
            response = client.recv(1024).decode('utf-8')
            print(response)
            
            print("NOTE : If you want to load file from server to you, when download is complete, your client will be disconnected automically.")
            lyrics_choice = input("Enter your choice (P for prompt, C for file): ")
            client.send(lyrics_choice.encode('utf-8'))
            
            if lyrics_choice == "P":
                lyrics = b""
                while True:
                    chunk = client.recv(1024)
                    if chunk == b'EOF':
                        break
                    lyrics += chunk
                print("- - - - - Lyrics - - - - -")
                print(lyrics.decode('utf-8'))
            elif lyrics_choice == "C":
                new_file_name = input("Enter the name of the file to save lyrics: ")
                client.send(new_file_name.encode('utf-8'))
                receive_file(client)
                client.close()
                break
        elif command == "N":
            response = client.recv(1024).decode('utf-8')
            print(response)
            client.close()
            break
        else:
            print("Invalid command. Please enter 'I', 'Y', or 'N'.")

if __name__ == "__main__":
    connect_to_server()