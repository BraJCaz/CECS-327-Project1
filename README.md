# CECS-327-Project1 Brandon Cazares and Meraj Nushin 

For our Project 1, we're going to build a small distibuted system with a master server and 4 different nodes 

We're allowed to code with both languages either Python or Java of our choice along with a Linux terminal 

This project has 3 main steps: different aspects of system architecture, communication protocols, and network monitoring. 

We're required to also download Docker as a requirement of this project 

Some important docker commands to know are:
1. docker builder
2. docker buildx
3. docker container
4. docker debug
5. docker image
6. docker init
7. docker node
8. docker scout
9. docker version

To understand how to code this project, we need a basic understanding of programming language, familiarity with Docker containers and Linux terminal commands along with a basic understanding of IP addresses, nodes, sockets and networking. 

For Step 1, we'll start this up by creating a container of a master server with 4 nodes with both Python code and Docker containers because those are necessary to create a distributed network with Docker 

We need to use this command: docker container ls because we need our container to implement 3 protocols for communication between the master server and 4 nodes  

For Step 2, we need to choose at least 2 out of 3 protocol designs recommended. We're going to choose broadcast and protocol design for this. 

For Step 3, we're going to track our network by monitoring all our communications with all 4 nodes and master server. 

Brandon's work: 
distributed_server.py, main_server.py, Dockerfile, CECS 327 Project 1 main code and unicast code

Meraj's work:
nodes, network_handler.py, simple_client.py, broadcast code and video recording 
