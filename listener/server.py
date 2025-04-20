import socket

SERVER_ADDRESS = '0.0.0.0'
SERVER_PORT = 1337

LOCAL_IP = "192.168.0.17"
BUFFER_SIZE = 1024
    
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind((SERVER_ADDRESS, SERVER_PORT))
print(f"UDP server is listening on {LOCAL_IP}:{SERVER_PORT}")

try:
    while True:
        data, client_address = server_socket.recvfrom(BUFFER_SIZE)
        if not data:
            break
        print(f"Received {len(data)} bytes from {client_address}: {data.decode()}")
        response = "WELL RECEIVED".encode()
        server_socket.sendto(response, client_address)
        print(f"Received {len(data)} bytes from {client_address}: {data.decode()}")

except KeyboardInterrupt:
    print("Server shutting down...")
finally:
    print('socket turned off')
    server_socket.close()
