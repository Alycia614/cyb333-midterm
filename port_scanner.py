import socket
import time
from threading import Thread

def scan_ports(start_port, end_port, target):
    """
    Scans a range of ports on the specified target host.
    Prints whether each port is open or closed.
    Uses a short delay between scans to avoid overwhelming the target.
    """
    for port in range(start_port, end_port):
        try:
            # Validate port range
            if not (0 <= port <= 65535):
                print(f"[ERROR] Invalid port: {port}")
                continue

            # Create a socket and attempt to connect to the port
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)  # Set timeout for connection attempt
                result = sock.connect_ex((target, port))
                if result == 0:
                    print(f"[OPEN] Port {port}")
                else:
                    print(f"[CLOSED] Port {port}")

                time.sleep(0.1)  # Ethical delay to avoid aggressive scanning

        except socket.gaierror:
            print(f"[ERROR] Hostname unreachable: {target}")
            break
        except Exception as e:
            print(f"[ERROR] Unexpected issue on port {port}: {e}")

def validate_input():
    """
    Prompts the user for a target host and port range.
    Validates the input and returns the target, start port, and end port.
    """
    try:
        target = input("Enter target (e.g., 127.0.0.1 or scanme.nmap.org): ").strip()
        start_port = int(input("Start port (0-65535): "))
        end_port = int(input("End port (0-65535): "))

        # Validate port numbers
        if not (0 <= start_port <= 65535) or not (0 <= end_port <= 65535):
            raise ValueError("Port numbers must be between 0 and 65535.")
        if start_port >= end_port:
            raise ValueError("Start port must be less than end port.")

        return target, start_port, end_port

    except ValueError as ve:
        print(f"[INPUT ERROR] {ve}")
        exit()

# === Main execution ===

# Get validated input from the user
target, start_port, end_port = validate_input()

# Create and start threads to scan ports in chunks of 100
threads = []
for i in range(start_port, end_port, 100):
    t = Thread(target=scan_ports, args=(i, min(i + 100, end_port), target))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()
