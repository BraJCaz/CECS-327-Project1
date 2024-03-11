import socket 

class NetworkHandler: 
    
    # A default constructor will assign their parameters using the self attribute  
    def __init__(self, host, port):
        self.host = host 
        self.port = port 
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    # this is our bind and listen from our socket to both our host and port 
    def bind_and_listen(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(8)
        print("Network is listening " + self.host + self.port)
        
    # this makes sure our connection's accepted 
    def connection_accepted(self):
        c_socket, add = self.socket.accept()
        return c_socket, add 
    
    # this makes sure our message is fully sent 
    def send(self, client_socket, message):
        client_socket.send(message.encode())
        
    # this checks if our message is received 
    def receive(self, client_socket, buffer_size=1024):
        return client_socket.recv(buffer_size).decode()
    
    # this is our broadcast handler because that's our first protocol that we chose 
    def broadcast(self, message, all_nodes):
        for node in all_nodes:
            self.send(node, message)
            
    # anycast is used for both our protocols: broadcast and unicast
    def anycast(self, message, optimal_node):
        self.send(optimal_node, message)
            
    # this will close our network handler code 
    def close(self, client_socket):
        client_socket.close() 
