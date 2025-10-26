import socket


HOST = "127.0.0.1"
PORT = 40001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Server listening on {HOST}:{PORT} ...")

    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break

            response = data.decode().upper()
            print(f"Received: {data.decode()} → Sending: {response}")
            # Send back
            conn.sendall(response.encode())