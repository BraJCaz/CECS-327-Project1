# this is our main server file 
import argparse
from distrubted_server import distributedserver
import logging 

# This will configure logging 
logging.basicConfig(filename='project.log', level=logging.DEBUG, 
                    format='%a(asctime)s - %(levelname)s - %(message)s')

# this will start our server 
<<<<<<< HEAD
def start_server(p):
    "This will initialixed and run the distributed server on the port we're going to use."
    s = distributedserver(p=p)
=======
def start_server(port):
    "This will initialixed and run the distributed server on the port we're going to use."
    s = distributedserver(port=port)
>>>>>>> 8ebf020 (<comments)
    s.run() 

# this is our main code 
def main(): 
    # This is our passed argument from our terminal for customization 
    parser = argparse.ArgumentParser(
        description="The main server's starting for our distributed networking project.")
<<<<<<< HEAD
    parser.add_argument("--port," type=int, default=8000,
=======
    parser.add_argument("--port", type=int, default=8000,
>>>>>>> 8ebf020 (<comments)
                        help="Port for the server to run on it.")
    
    args = parser.parse_args()

    # This is starting the server with specified (or default) arguments 
    start_server(args.port)

if __name__ == "__main__":
    main() 
