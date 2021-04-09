# Import socket module
from socket import * 
import sys # In order to terminate the program
import threading

import HttpRequest
from HttpRequest import RunThread# httprequest에서 만든 함수명


serverSocket = socket(AF_INET, SOCK_STREAM)

serverPort = 6789


serverSocket.bind(('', serverPort))


serverSocket.listen(1)



while True:
        print('The server is ready to receive')

        
        connectionSocket, addr = serverSocket.accept()

        #쓰레드 만들어서

        thr = threading.Thread(target=HttpRequest.RunThread, args=(connectionSocket,addr,))
        print('thread : ' + thr.getName())
        thr.start()
        

	
        
serverSocket.close()
sys.exit()
