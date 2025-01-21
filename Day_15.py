#Day 15: Introduction to Networking
#Project: Write a simple TCP client-server application using Python’s socket module.
#A project to demonstrate how to create a basic TCP client using Python's socket module.

#Step 1: Import the socket module
import socket  

#Step 2: Define the function to start the client
def start_client(host="127.0.0.1", port=12345):

#Step 3: Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    
#Step 4: Connect to the server
    client_socket.connect((host, port))  
    print(f"Connected to server at {host}:{port}")  

#Step 5: Allow user to send messages to the server
    while True:
        message = input("Enter message (type 'exit' to quit): ")  # Get user input
        client_socket.send(message.encode())  # Send message to server
        
        if message.lower() == "exit":
            break  #Close connection if user types 'exit'

        response = client_socket.recv(1024).decode()  #Receive response from server
        print(f"Server: {response}")  # Print server response  

#Step 6: Close the connection
    client_socket.close()  

#Step 7: Run the client if this file is executed directly
if __name__ == "__main__":
    start_client()