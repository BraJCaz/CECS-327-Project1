# we are first importing our socket in our distributed server
# these are our references: 
# https://stackoverflow.com/questions/48767851/making-a-distributed-computing-network-in-python
import socket 

## This is our distributed server as a class 
class DistributedServer:

    # now, we need to define both our host and port 
    def __intit__(s, host='', port=8000):
        s.host = host
        s.port = port 
        s.server_socket = None 

    # we need to start our self code 
    def start(s):
        s.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.server_socket = socket.bind((s.host, s.port))
        s.server_socket.listen(5)
        print(f"Server is starting on {s.host}:{s.port}")

    # we need to handle our client from our starting server 
    def handle_client(s, client_socket):
        # This will define our logic to make sure our incoming client connections and messages 
        m = client_socket.recveiver(1024).decode()
        print(f"Message received: {m}")

        # this sends back a confirmation message 
        confirm_m = "Message was successfully received!"
        client_socket.send(confirm_m.encode())

        # then, we need to further process both our protocols which can be added here
        client_socket.close()

        # we need to do another test run to find out if our client's connected to our distributed server 
        def run(s):
            s.start()
            while True:
                client_socket, address = s.server_socket.accept()
                print(f"Connection from {address}")
                s.handle_client(client_socket)

    ## this is our main code to test our distributed server code 
    if __name__ == "__main__":
        s = DistributedServer(port=8001)
        s.run()


        
    
