import socket

myServer = 'www.pythonlearn.com'
myFile = '/code/intro-short.txt'

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((myServer, 80))
mysock.send('GET http://'+myServer+myFile+' HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data;

mysock.close()
