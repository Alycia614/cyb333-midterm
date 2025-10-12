import socket
import time
from threading import Thread

def scan_ports(start_port, end_port, target):
    for port in range(start_port, end_port):
        try:
           if not (0 <= port <= 65535):
               print(f"[ERROR] Invalid port: {port}")
               continue
           
           with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
               sock.settimeout(1)
               result = sock.connect_ex((target, port))
               if result == 0:
                   print(f"[OPEN] Port {port}")
               else:
                   print(f"[CLOSED] Port {port}")
               time.sleep(0.1)  #Ethical delay
        except socket.gaierror:
            print(f"[ERROR] Hostname unreachable: {target}")
            break
        except Exception as e:
            print(f"[ERROR] Unexpected issue on port {port}: {e}")
def valididate_input():
    try:
        target = input("Enter target(127.0.0.1 or scanme.nmap.org): ").strip()
        start_port = int(input("start port (0-65535): "))
        end_port = int(input("end port (0-65535): "))

        if not (0 <= start_port <= 65535) or not (0 <= end_port <= 65535):
            raise ValueError("Port numbers must be between 0 and 65535.")
        if start_port >= end_port:
            raise ValueError("Start port must be less than end port.")
        
        return target, start_port, end_port
    except ValueError as ve:
        print(f"[INPUT ERROR] {ve}")
        exit()
# === Main execution===
target, start_port, end_port = valididate_input()

threads = []
for i in range(start_port, end_port, 100):
    t = Thread(target=scan_ports, args=(i, min(i+100, end_port), target))
    threads.append(t)
    t.start()
for t in threads:
    t.join()