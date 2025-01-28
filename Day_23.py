#Day 22-23: Building a Simple Port Scanner using Nmap
#Project: A Basic Port Scanner
#A program to demonstrate how to scan open ports using Nmap.

#Step 1: Import the necessary library
import nmap

#Step 2: Define a function to scan ports
def scan_ports(target, start_port, end_port):
    nm = nmap.PortScanner()
    print(f"\nScanning {target} for open ports...\n")

    nm.scan(target, f"{start_port}-{end_port}")

    for port in nm[target]['tcp']:
        if nm[target]['tcp'][port]['state'] == 'open':
            print(f"Port {port} is open!")

    print("\nPort scanning complete.")

#Step 3: Main program execution
if __name__ == "__main__":
    print("Nmap Port Scanner")

    target = input("\nEnter the target IP or domain: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    scan_ports(target, start_port, end_port)