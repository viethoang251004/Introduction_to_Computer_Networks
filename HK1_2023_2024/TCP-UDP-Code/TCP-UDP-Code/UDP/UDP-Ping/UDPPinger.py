from socket import *
import time

serverName = 'localhost' 
serverPort = 12000 
clientSocket = socket(AF_INET, SOCK_DGRAM) # 创建UDP套接字，使用IPv4协议
clientSocket.settimeout(1) 

for i in range(0, 10):
	sendTime = time.time()
	message = ('Ping %d %s' % (i+1, sendTime)).encode() # 
	try:
		clientSocket.sendto(message, (serverName, serverPort)) 
		modifiedMessage, serverAddress = clientSocket.recvfrom(1024) 
		rtt = time.time() - sendTime
		print('Sequence %d: Reply from %s    RTT = %.3fs' % (i+1, serverName, rtt)) 
	except Exception as e:
		print('Sequence %d: Request timed out' % (i+1))
		
clientSocket.close() 