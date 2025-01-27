#Day 22-23: Building a Simple Port Scanner
#Project: A Basic Port Scanner
#A program to demonstrate how to scan open ports on a target machine using the socket module.

#Step 1: Import the necessary libraries
import socket

#Step 2: Define a function to scan ports on a target machine
def scan_ports(target, start_port, end_port):
    print(f"\n🔍 Scanning {target} for open ports...\n")

#Loop through the specified range of ports
    for port in range(start_port, end_port + 1):
        # Step 3: Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Timeout to prevent long waits

#Step 4: Try to connect to the port
        result = s.connect_ex((target, port))
        if result == 0:  # If connection is successful
            print(f"Port {port} is open!")
        s.close()  #Close the connection

    print("\n🔹 Port scanning complete.")

#Step 5: Main program execution
if __name__ == "__main__":
    print("🖥️ Simple Python Port Scanner")

#Step 6: Get user input for the target machine and port range
    target = input("\nEnter the target IP or domain (e.g., 'example.com' or '192.168.1.1'): ")
    start_port = int(input("Enter the starting port (e.g., 1): "))
    end_port = int(input("Enter the ending port (e.g., 1024): "))

#Call the scanning function
    scan_ports(target, start_port, end_port)