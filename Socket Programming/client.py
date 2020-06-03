import socket as sk

c_socket = sk.socket()    ## Creates socket for client.

c_socket.connect(('localhost',9991))   ## It takes only one argument- a tuple of address(server's) and port number(service port number).


c_name= input('Please enter your name:')
c_socket.send(bytes(c_name,'utf-8'))

print(c_socket.recv(1024).decode()) #It receives the response sent by server. IT takes one arguement= size of response

