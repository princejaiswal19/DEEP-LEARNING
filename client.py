import socket

HOST = "127.0.0.1"  
PORT = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))  

client_socket.sendall(b"Hello from Client!")

response = client_socket.recv(1024)

print(f"Received from server: {response.decode()}")

client_socket.close()