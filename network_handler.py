# This is our network handler code 
import socket 

class NetworkHanlder: 

    def __init__(s, host='', port=8000):
        s.host = host 
        s.port = port 
        s.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def bind_and_listen(s):
        s.socket.bind((s.host, s.port))
        s.socket.listen(8)
        print(f"Network is listening {s.host}:{s.port}")

    def connection_accepted(s):
        client_socket, address = self.socket.accept()
        return client_socket, address 
    
    def send(s, client_socket, m):
        client_socket.send(m.encode())

    def receive(s, client_socket, buffer_size=1024):
        return client_socket.recv(buffer_size).decode()
    
    def anycast(s, m, optimal_node):
        s.send(optimal_node, m)

    def multicast(s, m, group_nodes):
        for node in group_nodes:
            s.send(node, m)

    def close(s, client_socket):
        client_socket.close() 