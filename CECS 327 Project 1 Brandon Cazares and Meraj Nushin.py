## Brandon Cazares - 025775800
## Meraj Nushin - 029155839
## CECS 327 Sec 2 Project 1 : A Bite of Distributed Communication 
## For this project, we're going to use Docker to create 4 nodes and create a distributed network with our master server  
## As our protocols, we're going to do broadcast and unicast design  

# As for our sources, we used StackOverflow and phpBB (forum software)
## https://stackoverflow.com/questions/65709087/is-there-a-way-to-distinguish-unicast-and-multicast-when-receiving-udp-datagram
## https://forums.naturalpoint.com/viewtopic.php?t=13472
## Unicast code 
import socket as socket 
import struct as struct 

SOCKET_BUFFSIZE = 0x100000

host = "172.224.42.53"
destination_ip = "192.168.1.202" # This is our server address which will be set to unicast 
# this is our host 
listen_all = True 
source_port = 3478 # this is our command port 
destination_port = 46692 # this is our data port 
# now we're going to create our sockets to connect to our server address 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
s.connect((destination_ip, destination_port)) ## this will use the server address to connect 
# our first setsockopt will have our socket reuse our address 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# our second setsockppt will have our socket read into our buffer size 
s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, SOCKET_BUFFSIZE)

## now we need to set to non-blocking 
s.setblocking(0)

## this socket will connect without an error, but it doesn't read any data 
while True:
    try: 
        # This doesn't read any data at all
        message, addr = s.recvfrom(SOCKET_BUFFSIZE) 
    except:
        pass
    else: 
        print(message, "\n")
