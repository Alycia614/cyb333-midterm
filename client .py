import socket
HOST = '127.0.0.1'
PORT = 65432
def start_client():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))
            print(f"[client] Connected to server at {HOST}:{PORT}")

            while True:
                message = input("Enter message (or 'exit' to quit): ")
                if message.lower() == 'exit':
                    print("[client] disconnecting...")
                    break
                client_socket.sendall(message.encode())
                data = client_socket.recv(1024)
                print(f"[client] Received: {data.decode()}")
    except ConnectionRefusedError:
        print("[client error] Server is not running or connection refused.")
    except Exception as e:
        print(f"[client error] {e}")