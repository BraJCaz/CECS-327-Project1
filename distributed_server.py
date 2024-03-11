
import socket 

## This is our distributed server as a class 
class DistributedServer:

    # Call the class constructor to pass in the parameters for the host and port 
    def __init__(self, host, port):
        self.host = host
        self.port = port 
        self.server_socket = None 
        
    #  Begin the server 
    def start(self):
        
        # Create a TCP/IP socket 
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Bind a socket to the designated address
        self.server_socket.bind((self.host, self.port))
        
        # Listens to all addresses simultainiously 
        self.server_socket.listen(8)
        
        print("Server is starting on", self.host, ":", self.port)

    # The starting server handles the client
    def handle_client(self, c_socket):
        
        # These last two lines of code will make sure 
        # that the message is received from the server
        m = c_socket.recv(1024).decode()
        print("Message received: " + m)

        # A message from the server has been verified! 
        received_message = "Message was successfully received!"
        c_socket.send(received_message.encode())

        # then, we need to further process both our protocols which can be added here
        c_socket.close()

    # Find out to test whether if the client is connected to the distributed server 
    def run(self):
        self.start()
        while True:
            c_socket, add = self.server_socket.accept()
            print("Connection from " + add)
            self.handle_client(add)

# Define the host and the port 
host = '0.0.0.0'
port = 8001
server = DistributedServer(host, port)
server.run()



        
    
