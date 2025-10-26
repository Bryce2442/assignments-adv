import socket

HOST = "127.0.0.1"
PORT = 40001


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    message = input("Enter a message to send: ")
    client_socket.sendall(message.encode())


    data = client_socket.recv(1024)
    print("Response from server:", data.decode())