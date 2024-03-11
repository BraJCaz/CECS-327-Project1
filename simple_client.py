# this is our simple client file to test our network connection 
# these are our references: 
# https://stackoverflow.com/questions/46775320/simple-python-server-client-file-transfer
# https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client
import socket 
import sys 
#import selectors 
#import types 

# we're going to define our sending message to our server 
def send_mess_to_server(host, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(message.encode())
        data = s.receive(1024)

    ## this will print our receieved message from the server 
    print(f"Message received from server: {data.decode()}")

# this is our main code to run for simple client 
if __name__ == "__main__":
    if len(sys.argv) > 4:
        print("Usage: python file simple_client.py HOST WILL PORT MESSAGE")
        
        #sys.exit(1)

    # then, we need both our host and port to send our message to our server 
        host, port, message = sys.argv[1], int(sys.argv[2]), sys.argv[3]
        send_mess_to_server(host, port, message)
