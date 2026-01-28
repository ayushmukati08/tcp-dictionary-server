import socket

# Create a TCP/IP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the dictionary server
client_socket.connect(('localhost', 9999))

try:
    while True:
        # Read user input
        word = input("Enter word (exit to quit): ").strip()

        # Prevent sending empty requests to the server
        if not word:
            print("Empty input not allowed. Please enter a word.")
            continue

        # Graceful shutdown command
        if word.lower() == 'exit':
            client_socket.send("__exit__".encode())
            break

        # Send word to server (newline used as message delimiter)
        client_socket.send((word + "\n").encode())

        # Receive and display server response
        meaning = client_socket.recv(1024).decode().strip()
        print("Meaning:", meaning)

finally:
    # Always close socket to free system resources
    client_socket.close()
