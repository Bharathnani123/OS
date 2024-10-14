import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 1234)
    client_socket.connect(server_address)

    data = client_socket.recv(1024)
    print("Received from server:", data.decode('utf-8'))
    
    message = "Hello, Server! This is the client."
    client_socket.sendall(message.encode('utf-8'))
    
    server_response = client_socket.recv(1024)
    print("Received from server:", server_response.decode('utf-8'))
    
    client_socket.close()

if __name__ == "__main__":
    start_client()
