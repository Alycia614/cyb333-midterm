import socket

# Define the server's IP address and port number
HOST = '127.0.0.1'
PORT = 65432

"""
Simple TCP server that listens on a specified host and port.
It accepts a single client connection, receives messages, and echoes them back.
"""

# Create a TCP/IP socket using IPv4 and TCP protocol
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    try:
        # Bind the socket to the specified host and port
        server_socket.bind((HOST, PORT))

        # Start listening for incoming connections
        server_socket.listen()
        print(f"Server listening on {HOST}:{PORT}")

        # Accept a single incoming connection
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")

            # Continuously receive data from the client
            while True:
                data = conn.recv(1024)

                # If no data is received, client has disconnected
                if not data:
                    break

                # Print received data and echo it back to the client
                print(f"Received data: {data.decode()}")
                conn.sendall(data)

    # Handle any unexpected errors
    except Exception as e:
        print(f"[server] Error: {e}")
