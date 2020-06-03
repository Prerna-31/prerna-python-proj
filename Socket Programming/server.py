import socket as sk

s_socket = sk.socket()     ## Two arguments need to be passed - IP version(IPv4, IPv8) and Connection type(TCP, UDP)

s_socket.bind(('localhost',9991))     # one argument = a tuple of ip address nd port number(available)

s_socket.listen(3)  # 3: The maximum no. of clients can be connected:
print('Waiting for client.......')

while True:
    c_socket,c_addr = s_socket.accept()     # returns two values. One is client socket and address(IP address, Port No.)
    c_name= c_socket.recv(1024).decode()    # recv() method receives the name send by client and decode() converts name(bytes) into string
    print('The client requested for the service is connected:',c_addr,c_name)
    c_socket.send(bytes('Welcome to the chatbox','utf-8'))  ## It sends response to the client but response always should be in objects form.
    c_socket.close()    ## Close the client connection. mandatory step to mention.



