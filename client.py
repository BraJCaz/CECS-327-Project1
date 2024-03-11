''' 
-----------------------------------------------------------------------------------------------------------------------
References: 
    Python Socket Programming Tutorial - https://www.youtube.com/watch?v=3QiPPX-KeSc
    Python TCP Server Accepting Connections and Broadcasting Commands - 
    https://stackoverflow.com/questions/41785969/python-tcp-server-accepting-connections-and-broadcasting-commands
    TCP/IP Client and Server - https://pymotw.com/2/socket/tcp.html
-----------------------------------------------------------------------------------------------------------------------
'''

# Import these dependencies so that we can have the server to connect to a client
import socket 
import sys 

# we're going to define our sending message to our server 
def send_message(host, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as send:
        send.connect((host, port))
        send.sendall(message.encode())
        data = send.receive(1024)

    # the message received from the server will be sent to the client 
    print("Message received from server:", data.decode())

host = "0.0.0.0"
port = 12345
message = "Hello fellow Nodes"
send_message(host, port, message)
