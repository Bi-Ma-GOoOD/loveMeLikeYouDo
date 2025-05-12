# import socket

# def connect_to_server():
#     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client.connect(('127.0.0.1', 1115))
    
#     while True:
#         # Receive the list of songs from the server
#         song_list = client.recv(4096).decode('utf-8')
#         print("Available songs:")
#         print(song_list)
        
#         # Allow user to choose an option
#         print("\nOptions:")
#         print("I - Information about the application")
#         print("Y - Select a song to play")
#         print("N - Exit")
#         command = input("Enter your choice: ")
#         client.send(command.encode('utf-8'))
        
#         if command == "I":
#             # Receive and display application information
#             info = client.recv(1024).decode('utf-8')
#             print(info)
#         elif command == "Y":
#             # Allow user to select a song
#             song_id = input("Enter the ID of the song to play: ")
#             client.send(song_id.encode('utf-8'))
            
#             # Receive and display the response for lyrics choice
#             response = client.recv(1024).decode('utf-8')
#             print(response)
            
#             lyrics_choice = input("Enter your choice (P for prompt, C for file): ")
#             client.send(lyrics_choice.encode('utf-8'))
            
#             if lyrics_choice == "P":
#                 lyrics = b""
#                 while True:
#                     chunk = client.recv(1024)
#                     if chunk == b'EOF':
#                         break
#                     lyrics += chunk
#                 print("Lyrics:")
#                 print(lyrics.decode('utf-8'))
#             elif lyrics_choice == "C":
#                 with open("rec6.txt", 'wb') as file:
#                     while True:
#                         data = client.recv(1024)
#                         if data == b'EOF':
#                             break
#                         file.write(data)
#                 print("Lyrics file received as 'rec6.txt'")
#         elif command == "N":
#             # End the client session
#             response = client.recv(1024).decode('utf-8')
#             print(response)
#             client.close()
#             break
#         else:
#             # Invalid command
#             print("Invalid command. Please enter 'I', 'Y', or 'N'.")

# if __name__ == "__main__":
#     connect_to_server()

"""version 02"""
import socket

def receive_file(client_socket):
    header = client_socket.recv(1024).decode('utf-8').strip()
    new_file_name, file_size = header.split(':')
    file_size = int(file_size)
    received_size = 0

    with open(new_file_name, 'wb') as file:
        while received_size < file_size:
            data = client_socket.recv(1024)
            if not data:
                break
            file.write(data)
            received_size += len(data)
    print(f"Lyrics file received as '{new_file_name}'")
    connect_to_server()

def temp_func():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 1115))
    
    while True:
        song_list = client.recv(4096).decode('utf-8')
        print("Available songs:")
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
                new_file_name = input("Enter the name of the file to save lyrics: ")
                client.send(new_file_name.encode('utf-8'))
                receive_file(client)
                print("What's next?")
        elif command == "N":
            response = client.recv(1024).decode('utf-8')
            print(response)
            client.close()
            break
        else:
            print("Invalid command. Please enter 'I', 'Y', or 'N'.")

def connect_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 1115))
    
    while True:
        song_list = client.recv(4096).decode('utf-8')
        print("Available songs:")
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
                new_file_name = input("Enter the name of the file to save lyrics: ")
                client.send(new_file_name.encode('utf-8'))
                receive_file(client)
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