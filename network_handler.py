# This is our network handler code 
# These are our references: 
# https://realpython.com/python-sockets/
# https://codereview.stackexchange.com/questions/128525/server-connection-handler-in-python
import socket 

class NetworkHandler: 
    # this is our init with our port address 
    def __init__(self, host='', port=8000):
        self.host = host 
        self.port = port 
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this is our bind and listen from our socket to both our host and port 
    def bind_and_listen(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(8)
        print(f"Network is listening {self.host}:{self.port}")
    # this makes sure our connection's accepted 
    def connection_accepted(self):
        client_socket, address = self.socket.accept()
        return client_socket, address 
    # this makes sure our message is fully sent 
    def send(self, client_socket, message):
        client_socket.send(message.encode())
    # this checks if our message is received 
    def receive(self, client_socket, buffer_size=1024):
        return client_socket.recv(buffer_size).decode()
    # this is our broadcast handler because that's our first protocol we chose 
    def broadcast(self, message, all_nodes):
        for node in all_nodes:
            self.send(node, message) 
    # anycast is usede for both our protocols: broadcast and unicast
    def anycast(self, message, optimal_node):
        self.send(optimal_node, message)
    # we're not doing multicast for this project 
    def multicast(self, message, group_nodes):
        for node in group_nodes:
            self.send(node, message)
    # this will close our network handler code 
    def close(self, client_socket):
        client_socket.close() 
