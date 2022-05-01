import socket
import threading
import time
import hashlib
import base64
import json
import os

import joke_generator

XOR_TABLE = [bytes(a ^ b for a in range(256)) for b in range(256)]

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 4000
serv_sock.bind(("", port))
serv_sock.listen(1)
player = 0



def getMessage(client_sock):
    message = client_sock.recv(2)
    if len(message) == 0:
        return "disconnected"
    fin = message[0]&128
    length = message[1]&127
    if length == 126:
        m = client_sock.recv(2)
        if len(m)==0:
            return "disconnected"
        length = int.from_bytes(m,"big")
    elif length == 127:
        m = client_sock.recv(8)
        if len(m)==0:
            return "disconnected"
        length = int.from_bytes(m,"big")
    masking = client_sock.recv(4)
    if len(masking)==0:
        return "disconnected"
    bindata = client_sock.recv(length)
    if len(bindata)==0:
        return "disconnected"
    data = []
    for i in range(len(bindata)):
        data.append(XOR_TABLE[bindata[i]][masking[i%4]])
    try:
        return [bytes(data).decode(),fin]
    except:
        return "disconnected"
    
def sendMessage(client_sock,datalist):
    for d in datalist:
        
        data = json.dumps(d)
        sending = []
        sending.append(129)
        encodeddata = data.encode()
            
        length = len(encodeddata)
        
        if length<=125:
            sending.append(length)
        elif length>=126 and length<=65535:
            sending.append(126)
            sending.append((length>>8)&255)
            sending.append(length & 255)
        else:
            sending.append(127)
            sending.append((length>>56)&255)
            sending.append((length>>48)&255)
            sending.append((length>>40)&255)
            sending.append((length>>32)&255)
            sending.append((length>>24)&255)
            sending.append((length>>16)&255)
            sending.append((length>>8)&255)
            sending.append(length&255)
        sending = bytes(sending)
        sending += encodeddata
        client_sock.sendall(sending)
def encodeFile(f):
    try:
        file = open(f,"rb")
        file_d = base64.b64encode(file.read()).decode()
        file.close()
        return file_d
    except:
        return 0
def on_new_client(client_sock,player):
    global run
    while run:
        
        message = getMessage(client_sock)
        if message == "disconnected":
            client_sock.close()
            return
        data = message[0]
        if message[1] == 0:
            while True:
                message = getMessage(client_sock)
                if message == "disconnected":
                    client_sock.close()
                    return
                data+=message[0]
                if message[1]!=0:
                    break
        data = json.loads(data.replace("'",'"'))
        
        senddata = []
        
        #file send
        if data["type"] == 0:
            dirlist = os.listdir("FILES")
            for f in range(len(dirlist)):
                file = "FILES/{}".format(dirlist[f])
                
                fin = 0
                if f == len(dirlist)-1:
                    fin = 1
                
                senddata.append({"type":0,"file":dirlist[f],"data":encodeFile(file),"finished":fin})
        #joke game     
        elif data["type"] == 1:
            joke = joke_generator.generate_joke()
            senddata.append({"type":1,"joke":joke[0],"answer":joke[1]})
        sendMessage(client_sock,senddata)
    client_sock.close()
    

run = True
while run:
    client_sock, client_addr = serv_sock.accept()
    print(client_addr[0])
    message = client_sock.recv(1024).decode()
    key = [x for x in message.split("\r\n") if x.startswith('Sec-WebSocket-Key')][0].replace("Sec-WebSocket-Key:","",1).strip()
    websocketUpgrade = [x for x in message.split("\r\n") if x.startswith('Upgrade')][0].replace("Upgrade:","",1).strip()
    if websocketUpgrade != "websocket":
        continue
    magic_number = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
    newkey = base64.b64encode(hashlib.sha1((key+magic_number).encode()).digest()).decode()
    handshake = "HTTP/1.1 101 Switching Protocols\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Accept: {}\r\n\r\n".format(newkey)
    client_sock.send(handshake.encode())
    if client_addr[0]=="127.0.0.1" or 1==1:
        ConnectionThread = threading.Thread(target = on_new_client,args = (client_sock,player))
        ConnectionThread.start()
    
    player+=1
serv_sock.close()





