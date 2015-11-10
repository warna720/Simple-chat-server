#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import socket, select, cPickle, collections, chat_pb2

def send_data(sock, data):
    try:
        sock.send(cPickle.dumps(data))
    except:
        print("Error: probably broken pipe")
        
def recv_data(sock):
    try:
        return cPickle.loads(sock.recv(4096))
    except:
        return None
    
host, port = "127.0.0.1", 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port))
server_socket.listen(5)

print("Server listening at port " + str(port))


CONNECTION_LIST = [server_socket]
CONNECTION_DETAILS = dict()
CHANNEL_CONNECTIONS = dict()

def new_message(connections, sender_socket, nick, message):
    msg = chat_pb2.message()
    msg.text = nick + ": " + message
    for conn in connections:
        if conn is not sender_socket:
            send_data(conn, ("message", msg)) 

while True:

    #Ignoring write and error sockets.
    read_sockets, _, _ = select.select(CONNECTION_LIST, [], [])
    
    for sock in read_sockets:
        #New connection
        if sock == server_socket:
            sockfd, addr = server_socket.accept()
            CONNECTION_LIST.append(sockfd)
        
        #Message from client
        else:
            data = recv_data(sock)
            if data:
                if (data[0] == "join"):
                    Details = collections.namedtuple('Details', 'channel nick')
                    channel = data[1].channel
                    nick = data[1].nick
                    CONNECTION_DETAILS[sock] = Details(channel, nick)
                    
                    if CHANNEL_CONNECTIONS.has_key(channel):
                        CHANNEL_CONNECTIONS[channel].append(sock)
                    else:
                        CHANNEL_CONNECTIONS[channel] = [sock]
                        
                elif (data[0] == "message"):
                    channel = CONNECTION_DETAILS[sock].channel
                    nick = CONNECTION_DETAILS[sock].nick
                    msg = data[1].text
                    new_message(CHANNEL_CONNECTIONS[channel], sock, nick, msg)
                
server_socket.close()
