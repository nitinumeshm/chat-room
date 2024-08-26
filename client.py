#!/usr/bin/env python3

## Python program to implement the Client Side of the Chat Room

import socket
import select
import sys

## Creating a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## Connecting to the server
client_socket.connect(('localhost', 12345))


while True:
    message = input("You: ")
    client_socket.sendall(message.encode())            ## Send data to the server
    data = client_socket.recv(1024)                    ## Receive data from the server
    print(f"Server: {data.decode()}")

client_socket.close()
