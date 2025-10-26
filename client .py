import socket
# Define the server's IP address and port number
HOST = '127.0.0.1'
PORT = 65432

def start_client():
    """
    Starts a TCP client that connects to a server at the specified HOST and PORT.
    The client sends user input to the server and prints the server's response.
    Type 'exit' to disconnect from the server.
    """
    try:
        # Create a TCP/IP socket using IPv4 and TCP protocol
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            # Connect to the server
            client_socket.connect((HOST, PORT))
            print(f"[client] Connected to server at {HOST}:{PORT}")

            # Loop to send messages until user types 'exit'
            while True:
                message = input("Enter message (or 'exit' to quit): ")
                
                # Exit condition
                if message.lower() == 'exit':
                    print("[client] disconnecting...")
                    break

                # Send message to server
                client_socket.sendall(message.encode())

                # Receive and print server response
                data = client_socket.recv(1024)
                print(f"[client] Received: {data.decode()}")

    # Handle case where server is not running
    except ConnectionRefusedError:
        print("[client error] Server is not running or connection refused.")

    # Handle any other unexpected errors
    except Exception as e:
        print(f"[client error] {e}"
