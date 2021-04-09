


def RunThread(connectionSocket, addr): #함수명 인자는 connection server socket & addr
                    message = connectionSocket.recv(2048).decode()
                    print(message)

                    # Extract the path of the requested object from the message
                    # The path is the second part of HTTP header, identified by [1]
                    filename = message.split()[1]
                    print(filename)

                    # Because the extracted path of the HTTP request includes 
                    # a character '\', we read the path from the second character
                    myfile = open(filename[1:],'rb')

                    # Store the entire contenet of the requested file in a temporary buffer
                    response = myfile.read()
                    myfile.close()
                    
                    # Send the HTTP response header line to the connection socket
                    header = 'HTTP/1.1 200 OK\n'

                    if(filename.endswith(".jpg")):
                            filetype = 'image/jpg'
                    elif(filename.endswith(".mp4")):
                            filetype = 'video/mp4'
                    else:
                            filetype = 'text/html'

                    header += 'Content-Type: '+str(filetype)+'\n\n'
                    print(header)

                    connectionSocket.send(header.encode())
                    connectionSocket.send(response)
                    connectionSocket.close()
