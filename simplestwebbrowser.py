import socket


mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #establishing the socket

#connecting to the homepage of the hackerrank Website
mysock.connect(('www.hackerrank.com',80))

#encoding info from the page
cmd='GET htpps://www.hackerrank.com \r\n\r\n'.encode()
mysock.send(cmd)


while True:
    #receive the 512 char from the page
    data=mysock.recv(512)
    if len(data) < 1:               #break when server stop sending signals
        break
    print(data.decode(),end='')         #decode and print the data


#while server stops sending data ,end the connection.
mysock.close()

