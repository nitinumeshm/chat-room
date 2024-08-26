#!/usr/bin/env python3

## Python program to implement the server side of the Chat Room

import socket
import threading

"""
First Argument AF_INET: It is the address domain of the socket.
This is used when we have an Internet Domain with any two hosts
Second Argument SOCK_STREAM: It is a type of socket, where data or characters are read in a continuous flow
"""

## Function to handle multiple clients

def handle_client(conn, addr):
    print(f"New connection from {addr}")   ## Receive data from the client
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Client {addr}: {data.decode()}")
        reply = input("You: ")
        conn.sendall(reply.encode())       ## Send data to the client
    conn.close()


## Creating a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## Binding the socket to an address and port
server_socket.bind(('localhost', 12345))

## Listening for incoming connections
server_socket.listen(100)                  ## Listening upto 100 connections


while True:
    conn, addr = server_socket.accept()    ## Accept a connection
    client_thread = threading.Thread(target = handle_client, args = (conn, addr))
    client_thread.start()
