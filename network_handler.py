# This is our network handler code 
import socket 

class NetworkHanlder: 
    # this is our init with our port address 
    def __init__(s, host='', port=8000):
        s.host = host 
        s.port = port 
        s.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this is our bind and listen from our socket to both our host and port 
    def bind_and_listen(s):
        s.socket.bind((s.host, s.port))
        s.socket.listen(8)
        print(f"Network is listening {s.host}:{s.port}")
    # this makes sure our connection's accepted 
    def connection_accepted(s):
        client_socket, address = self.socket.accept()
        return client_socket, address 
    # this makes sure our message is fully sent 
    def send(s, client_socket, m):
        client_socket.send(m.encode())
    # this checks if our message is received 
    def receive(s, client_socket, buffer_size=1024):
        return client_socket.recv(buffer_size).decode()
    # anycast is usede for both our protocols: broadcast and unicast 
    def anycast(s, m, optimal_node):
        s.send(optimal_node, m)
    # we're not doing multicast for this project 
    def multicast(s, m, group_nodes):
        for node in group_nodes:
            s.send(node, m)
    # this will close our network handler code 
    def close(s, client_socket):
        client_socket.close() 
