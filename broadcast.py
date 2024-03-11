
'''
References: 
    Python Socket Programming Tutorial - https://www.youtube.com/watch?v=3QiPPX-KeSc
    Python TCP Server Accepting Connections and Broadcasting Commands - 
    https://stackoverflow.com/questions/41785969/python-tcp-server-accepting-connections-and-broadcasting-commands
    TCP/IP Client and Server - https://pymotw.com/2/socket/tcp.html
'''
    
import socket

class DistributedClass:
    
    # Define the host and the port number using the self attribute
    def __init__(self, h, p):
        self.host = h 
        self.port = p
        
    # Start the broadcast to send the message to all clients 
    def broadcast_message(self):

        # Develop a socket for the master node 
        socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Assign the IP address to the host and the port number to port
        
        # Bind the server with the IP address and a port number 
        socket.bind((self.host, self.port))
        
        # The Master server is connected to four nodes 
        socket.listen(4)
        
        # Print out the connections on the host and port number the server is listening
        print("Listening for connections on " + host + ":" + "port...")
        
        # Make an empty list for clients
        clients = [] 

        try:
            for i in range(4):
                
                # Master server accepts a connection requested from a client
                client_socket, addr = socket.accept() 
                print("Connection from " + addr + " established!")
                
                # Append the accepted connection to the client list 
                clients.append(client_socket)
            
            # Broadcast a message amongst all clients 
            for client in clients:
                
                # This line below confirms that all of the clients received the message
                message = "A message received from the client!!!"
                
                # Send a message to all clients 
                client.sendall(message)
                
        # After the broadcast ends, close all connections 
        finally: 
            
            # Loop through the client list to close their connections
            for client in clients:
                client.close()
            socket.close()
      
# Define the host and the port number  
host = '0.0.0.0'
port = 12345

# Call the class to insert the host and the port
DistributedClass(host, port)













