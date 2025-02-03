import time
from socket import *

server_name = 'localhost'
server_port = 12000

client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(1)

for sequence_number in range(1, 11):
    send_time = time.time()
    message = f'Ping {sequence_number} {send_time}'
    
    try:
        client_socket.sendto(message.encode(), (server_name, server_port))
        response, server_address = client_socket.recvfrom(1024)
        receive_time = time.time()
        rtt = receive_time - send_time
        print(f'Received: {response.decode()} | RTT: {rtt:.6f} sec')
    except timeout:
        print(f'Request {sequence_number} timed out')

    time.sleep(1)

client_socket.close()
