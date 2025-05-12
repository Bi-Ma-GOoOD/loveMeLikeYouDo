import socket

def connect_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 1115))
    
    while True:
        # Receive the list of songs from the server
        song_list = client.recv(4096).decode('utf-8')
        print("Available songs:")
        print(song_list)
        
        # Allow user to choose an option
        print("\nOptions:")
        print("I - Information about the application")
        print("Y - Select a song to play")
        print("N - Exit")
        command = input("Enter your choice: ")
        client.send(command.encode('utf-8'))
        
        if command == "I":
            # Receive and display application information
            info = client.recv(1024).decode('utf-8')
            print(info)
        elif command == "Y":
            # Allow user to select a song
            song_id = input("Enter the ID of the song to play: ")
            client.send(song_id.encode('utf-8'))
            
            # Receive and display the response for lyrics choice
            response = client.recv(1024).decode('utf-8')
            print(response)
            
            lyrics_choice = input("Enter your choice (P for prompt, C for file): ")
            client.send(lyrics_choice.encode('utf-8'))
            
            if lyrics_choice == "P":
                lyrics = b""
                while True:
                    chunk = client.recv(1024)
                    if chunk == b'EOF':
                        break
                    lyrics += chunk
                print("Lyrics:")
                print(lyrics.decode('utf-8'))
            elif lyrics_choice == "C":
                with open("test01.txt", 'wb') as file:
                    while True:
                        data = client.recv(1024)
                        if data == b'EOF':
                            break
                        file.write(data)
                print("Lyrics file received as 'test01.txt'")
        elif command == "N":
            # End the client session
            response = client.recv(1024).decode('utf-8')
            print(response)
            client.close()
            break
        else:
            # Invalid command
            print("Invalid command. Please enter 'I', 'Y', or 'N'.")

if __name__ == "__main__":
    connect_to_server()
