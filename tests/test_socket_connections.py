import socket
import threading

def connect_to_server(target_host, target_port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, target_port))
    # Optionally, you can send and receive data on each connection

# Define the target server's host and port
target_host = "127.0.0.1"
target_port = 5000

# Define the number of connections you want to create
num_connections = 10

# Create a list to store the connection threads
connection_threads = []

# Create and start connection threads
for _ in range(num_connections):
    connection_thread = threading.Thread(target=connect_to_server, args=(target_host, target_port))
    connection_threads.append(connection_thread)
    connection_thread.start()

# Wait for all threads to complete
for thread in connection_threads:
    thread.join()

print("All connections have been established.")
