import socket
import time

SERVER_ADDRESS = '192.168.0.17'  
SERVER_PORT = 1337

DATA = b"THIS IS AN IMPORTANT AND SECRET MESSAGE"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        client_socket.sendto(DATA, (SERVER_ADDRESS, SERVER_PORT))
        print(f"Sent {len(DATA)} bytes to {SERVER_ADDRESS}:{SERVER_PORT}")

        # repeat every 5 seconds
        time.sleep(5)

except KeyboardInterrupt:
    print("Client shutting down...")
finally:
    print("socket turned off")
    client_socket.close()
