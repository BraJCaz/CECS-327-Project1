# we are first importing our socket in our distributed server
# these are our references: 
# https://stackoverflow.com/questions/48767851/making-a-distributed-computing-network-in-python
import socket 

## This is our distributed server as a class 
class DistributedServer:

    # now, we need to define both our host and port 
    def __init__(self, host='', port=8000):
        self.host = host
        self.port = port 
        self.server_socket = None 

    # we need to start our self code 
    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket = socket.bind((self.host, self.port))
        self.server_socket.listen(8)
        print(f"Server is starting on {self.host}:{self.port}")

    # we need to handle our client from our starting server 
    def handle_client(self, client_socket):
        # This will define our logic to make sure our incoming client connections and messages 
        message = client_socket.recveiver(1024).decode()
        print(f"Message received: {message}")

        # this sends back a confirmation message 
        confirm_message = "Message was successfully received!"
        client_socket.send(confirm_message.encode())

        # then, we need to further process both our protocols which can be added here
        client_socket.close()

        # we need to do another test run to find out if our client's connected to our distributed server 
        def run(self):
            self.start()
            while True:
                client_socket, address = self.server_socket.accept()
                print(f"Connection from {address}")
                self.handle_client(client_socket)

    ## this is our main code to test our distributed server code 
    if __name__ == "__main__":
        server = DistributedServer(port=8001)
        server.run()


        
    
