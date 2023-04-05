from socket import *
import socket
import threading
import time
import sys
import logging
from http import HttpServer
import multiprocessing

httpserver = HttpServer()


class ClientProcess(multiprocessing.Process):
	def __init__(self, connection, address):
		self.connection = connection
		self.address = address
		multiprocessing.Process.__init__(self)

	def run(self):
		rcv=""
		while True:
			try:
				data = self.connection.recv(32)
				if data:
					d = data.decode()
					rcv=rcv+d
					if rcv[-2:]=='\r\n':
						hasil = httpserver.proses(rcv)
						hasil=hasil+"\r\n\r\n".encode()
						self.connection.sendall(hasil)
						rcv=""
						self.connection.close()
				else:
					break
			except OSError as e:
				pass
		self.connection.close()



class Server(multiprocessing.Process):
	def __init__(self, ip, port):
		self.the_clients = []
		self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.ip = ip
		self.port = port
		multiprocessing.Process.__init__(self)

	def run(self):
		self.my_socket.bind((self.ip, self.port))
		self.my_socket.listen(200)
		while True:
			self.connection, self.client_address = self.my_socket.accept()
			clt = ClientProcess(self.connection, self.client_address)
			clt.start()
			self.the_clients.append(clt)

if __name__=="__main__":
	svr = Server('0.0.0.0', 8888)
	svr.start()

