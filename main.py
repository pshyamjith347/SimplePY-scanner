import socket
from datetime import datetime

def scan_ports(target):
    print("-" * 50)
    print(f"Scanning Target: {target}")
    print(f"Scanning started at: {str(datetime.now())}")
    print("-" * 50)

    # Common ports to check
    common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 445, 3306, 3389, 4444, 8080]

    try:
        for port in common_ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1) # 1 second timeout
            
            # returns an error indicator
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port}: OPEN")
            s.close()

    except KeyboardInterrupt:
        print("\n Exiting Program.")
    except socket.gaierror:
        print("\n Hostname Could Not Be Resolved.")
    except socket.error:
        print("\n Server not responding.")

if __name__ == "__main__":
    target_ip = input("Enter the IP or Hostname to scan: ")
    scan_ports(target_ip)
