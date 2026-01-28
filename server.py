import socket
import threading
import nltk
from nltk.corpus import wordnet

# NOTE:
# WordNet data should be downloaded once during environment setup.
# These lines are intentionally commented to avoid repeated downloads on every run.
# nltk.download('wordnet', quiet=True)
# nltk.download('omw-1.4', quiet=True)  # Improves definition coverage


def get_definition(word):
    """
    Fetches the definition of a word using WordNet.
    Replaces spaces with underscores to support multi-word terms.
    """
    word = word.replace(' ', '_')
    synsets = wordnet.synsets(word)

    # Return the most common meaning if available
    return synsets[0].definition() if synsets else "Definition not found."


def handle_client(client_socket, addr):
    """
    Handles communication with a single client.
    Runs in a separate thread for each connected client.
    """
    print("Connected with", addr)
    try:
        while True:
            # Receive data from client (TCP stream)
            data = client_socket.recv(1024).decode().strip()

            # Client explicitly requested termination
            if data == "__exit__":
                break

            # Process client request
            meaning = get_definition(data)

            # Send response back to client
            client_socket.sendall((meaning + "\n").encode())

    finally:
        # Ensure socket is closed even if an error occurs
        client_socket.close()
        print("Disconnected", addr)


# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind server to localhost on port 9999
server_socket.bind(('localhost', 9999))

# Allow up to 5 pending client connections
server_socket.listen(5)

print("Server running...")

# Main server loop: accept clients and handle them concurrently
while True:
    client, addr = server_socket.accept()

    # Start a new thread for each client connection
    threading.Thread(
        target=handle_client,
        args=(client, addr),
        daemon=True  # Ensures threads exit when server shuts down
    ).start()
