# this is our main server file 
# these are our references:
# https://stackabuse.com/serving-files-with-pythons-simplehttpserver-module/
# https://www.freecodecamp.org/news/simplehttpserver-explained-how-to-send-files-using-python/
import argparse
from distributed_server import DistributedServer
import logging 

# Configure logging
logging.basicConfig(filename='project.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Start the server 
def start_server(port):
    server = DistributedServer(port)
    server.run() 

# These lines of code gives us the description of the main server with the port number 
parser = argparse.ArgumentParser(description="The main server's starting for our distributed networking project.")
parser.add_argument("--port", type=int, default=8001, help="Port for the server to run on it.")
args = parser.parse_args()

# Starts the server with specified arguments 
start_server(args.port)
