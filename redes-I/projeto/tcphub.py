from socket import *
from threading import Thread
import time
import sys
import struct
import os

class ListenServers(Thread):

	def __init__(self, num):
		Thread.__init__(self)
		self.num = num
		self.portsAvailable = []

	def contactServer(self, serverPort):
		serverName = 'localhost'
		try:
			clientHubSocket = socket(AF_INET, SOCK_STREAM)
			print('Initiating TCP connection with server', serverName, 'over port', serverPort, '...')
			clientHubSocket.connect((serverName,serverPort))
			print('Closing TCP connection...')
			clientHubSocket.close()
			return True
		except:
			print('Could not make a connection to the server', serverPort)
			return False

	def run(self):
		serverPort = 12001
		hubSocket = socket(AF_INET,SOCK_STREAM)
		hubSocket.bind(('',serverPort))
		hubSocket.listen(1)
		print('The Hub is ready to receive from Servers')


		while 1:
			connectionSocket, addr = hubSocket.accept()
			print('Connected to server', addr)
			port = struct.unpack('i',connectionSocket.recv(4))[0]
			print('Port received:', port)
			if not self.contactServer(port):
				if port not in self.portsAvailable:
					self.portsAvailable.append(port)
				response = 'OK'
			else:
				print("Port", port,"is already available")
				response = "Port is already available"

			print("Ports available: ",self.portsAvailable)
			print()
			connectionSocket.send(response.encode())
			connectionSocket.close()


class ListenClient(Thread):

	def __init__(self, num, threadServers):
		Thread.__init__(self)
		self.num = num
		self.threadServers = threadServers


	def servers_with_file(self, size_filename, filename, operation):
		servers = []
		for serverPort in self.threadServers.portsAvailable:
			serverName = 'localhost'

			try:
				clientHubSocket = socket(AF_INET, SOCK_STREAM)
				print('Initiating TCP connection with server', serverName, 'over port', serverPort, '...')
				clientHubSocket.connect((serverName,serverPort))
			except:
				print('Could not make a connection to the server', serverPort)
				continue

			print("Sending operation.")
			clientHubSocket.send(struct.pack('i', 2))

			print('Sending filename')
			clientHubSocket.send(struct.pack('i',size_filename))
			clientHubSocket.send(filename.encode())

			print('Waiting server response...')
			response = clientHubSocket.recv(3).decode()
			if response == 'ACK':
				print("Server", serverName, "in port", serverPort, "has the file", filename, ".")
				servers.append((serverName, serverPort))
				message = 'NCK'
				clientHubSocket.send(message.encode())
			else:
				print("Server", serverName, "in port", serverPort, "doesn't have the file", filename, ".")

			print('Closing TCP connection...')
			clientHubSocket.close()
			print('Finish.')

		return servers

	def add_files_to_servers(self, clientConnectionSocket, servers_with_file, size_filename, filename, ft_level):
		print("Receiving file from Client...")
		file = open('temp','wb')
				
		packet = clientConnectionSocket.recv(1024)
		while (packet):
			file.write(packet)
			packet = clientConnectionSocket.recv(1024)

		file.close()

		for serverPort in self.threadServers.portsAvailable:
			serverName = 'localhost'
			if (serverName, serverPort) in servers_with_file:
				continue

			try:
				clientHubSocket = socket(AF_INET, SOCK_STREAM)
				print('Initiating TCP connection with server', serverName, 'over port', serverPort, '...')
				clientHubSocket.connect((serverName,serverPort))
			except:
				print('Could not make a connection to the server', serverPort)
				continue

			try:
				file = open('temp','rb')
			except:
				print('No such file or directory named: ', filename)
				sys.exit(0)

			print("Sending operation.")
			clientHubSocket.send(struct.pack('i', 1))
			print('Sending filename.')
			print(filename)
			clientHubSocket.send(struct.pack('i',size_filename))
			clientHubSocket.send(filename.encode())
			print('Sending file to server', serverName, 'over port', serverPort, '...')
			packet = file.read(1024)
			while (packet):
				clientHubSocket.send(packet)
				packet = file.read(1024)

			file.close()
			print('File uploaded. Notifying server...')
			clientHubSocket.shutdown(SHUT_WR)

			print('Waiting server response...')
			response = clientHubSocket.recv(1024)

			print('From Server:', response.decode())

			print('Closing TCP connection...')
			clientHubSocket.close()
			print('Finish.')
			ft_level -= 1
			if ft_level == 0:
				break

		return ft_level

	def remove_files_from_servers(self, servers_with_file, size_filename, filename, ft_level_remaining):
		for server in servers_with_file:
			try:
				clientHubSocket = socket(AF_INET, SOCK_STREAM)
				print('Initiating TCP connection with server', server[0], 'over port', server[1], '...')
				clientHubSocket.connect(server)
			except OSError:
				print('Could not make a connection to the server', server)
				print(OSError)
				continue

			print("Sending operation.")
			clientHubSocket.send(struct.pack('i', 3))

			print('Sending filename')
			clientHubSocket.send(struct.pack('i',size_filename))
			clientHubSocket.send(filename.encode())

			print('Waiting server response...')
			response = clientHubSocket.recv(3).decode()
			print(response)
			if response == 'ACK':
				print("Server", server[0], "in port", server[1], "erased the file", filename, ".")
				ft_level_remaining -= 1
			else:
				print("Server", server[0], "in port", server[1], "didn't erase the file", filename, ".")


			print('Closing TCP connection...')
			clientHubSocket.close()
			print('Finish.')
			print()
			if ft_level_remaining == 0:
				break

		return ft_level_remaining

	def recover_file(self, size_filename, filename):
		file_available = False
		for serverPort in self.threadServers.portsAvailable:
			serverName = 'localhost'

			try:
				clientHubSocket = socket(AF_INET, SOCK_STREAM)
				print('Initiating TCP connection with server', serverName, 'over port', serverPort, '...')
				clientHubSocket.connect((serverName,serverPort))
			except:
				print('Could not make a connection to the server', serverPort)
				continue

			print("Sending operation.")
			clientHubSocket.send(struct.pack('i', 2))

			print('Sending filename.')
			clientHubSocket.send(struct.pack('i',size_filename))
			clientHubSocket.send(filename.encode())

			print('Waiting server response...')
			response = clientHubSocket.recv(3).decode()
			if response == 'ACK':
				print("Server", serverName, "in port", serverPort, "has the file", filename, ".")
				print("Requesting the file from server...")
				request = 'ACK'
				clientHubSocket.send(request.encode())

				file_available = True
				try:
					file = open('temp','wb')
				except:
					print("Not possible to create the file")
					sys.exit(0)

				print("Receiving file from server...")
				packet = clientHubSocket.recv(1024)
				while (packet):
					file.write(packet)
					packet = clientHubSocket.recv(1024)
				file.close()
				print("File received.")
			else:
				print("Server", serverName, "in port", serverPort, "doesn't have the file", filename, ".")

			print('Closing TCP connection...')
			clientHubSocket.close()
			print('Finish.')

			if response == 'ACK':
				break

		return file_available

	def deposit(self, clientConnectionSocket, operation):
		size_filename = struct.unpack('i',clientConnectionSocket.recv(4))[0]
		filename = clientConnectionSocket.recv(size_filename).decode()
		print('Filename:', filename)
		ft_level = struct.unpack('i',clientConnectionSocket.recv(4))[0]
		print('Tolerance Level:', ft_level)
		print()

		servers_wf = self.servers_with_file(size_filename, filename, operation)
		print('Servers with file:',servers_wf)

		ft_level -= len(servers_wf)

		response = 'ACK'
		if ft_level <= 0:
			response = 'NCK'

		clientConnectionSocket.send(response.encode())

		if ft_level < 0:
			print('Actual Tolerance Level greater than requested.')
			print('Removing files from servers...')
			print()
			ft_level = self.remove_files_from_servers(servers_wf, size_filename, filename, -ft_level)
		elif ft_level > 0:
			print('Actual Tolerance Level smaller than requested.')
			print('Adding files to servers...')
			print()
			ft_level = self.add_files_to_servers(clientConnectionSocket, servers_wf, size_filename, filename, ft_level)

		if ft_level == 0:
			response = 'OK'
		else:
			response = 'Tolerance Level not accomplished: '+str(ft_level)
		
		clientConnectionSocket.send(response.encode())

	def recovery(self, clientConnectionSocket, operation):
		size_filename = struct.unpack('i',clientConnectionSocket.recv(4))[0]
		filename = clientConnectionSocket.recv(size_filename).decode()
		print("Filename:",filename)
		print()

		file_available = self.recover_file(size_filename, filename)
		if file_available:
			response = 'ACK'
			clientConnectionSocket.send(response.encode())
			try:
				file = open('temp','rb')
			except:
				print('No such file or directory named: ', filename)
				sys.exit(0)

			print("Sending file to client...")
			packet = file.read(1024)
			while (packet):
				clientConnectionSocket.send(packet)
				packet = file.read(1024)

			file.close()
			print('File downloaded. Notifying client...')
			clientConnectionSocket.shutdown(SHUT_WR)
		else:
			response = 'NCK'
			clientConnectionSocket.send(response.encode())

	def run(self):
		serverPort = 12000
		hubSocket = socket(AF_INET,SOCK_STREAM)
		hubSocket.bind(('',serverPort))
		hubSocket.listen(1)
		print('The Hub is ready to receive from Client')

		while 1:
			clientConnectionSocket, clientAddr = hubSocket.accept()
			try:
				print('Client connection accepted')
				operation = struct.unpack('i',clientConnectionSocket.recv(4))[0]
				print()
				if operation == 1:
					print('Deposit operation')
					print()
					self.deposit(clientConnectionSocket, operation)
				elif operation == 2:
					print('Recovery operation')
					print()
					self.recovery(clientConnectionSocket, operation)

				print()
				if os.path.exists('temp'):
					os.remove('temp')
				
				print("Closing connection with Client.")
				clientConnectionSocket.close()
			except Exception as e:
				print('An error ocurred:', e)
				print("Closing connection with Client.")
				print()
				clientConnectionSocket.close()




threadServers = ListenServers(1)
threadServers.start()

threadClient = ListenClient(1, threadServers)
threadClient.start()		

