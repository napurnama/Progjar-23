from socket import *
import socket
import threading
import datetime
import sys
import logging


class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        res=""
        logging.warning("THIS IS THE RUN!")
        while True:
            try:
                data = self.connection.recv(32)
                if data:
                    data = data.decode()
                    if data[-2:] == '\r\n':
                        now = datetime.datetime.now()
                        now = now.time().strftime('%H:%M:%S')
                        res = "JAM " + now + '\r\n'
                        self.connection.sendall(res.encode())
                        res = ""
                    else:
                        res = "ERR 404: {}".format(data)
                        self.connection.sendall(res.encode())
                        break
                self.connection.close()
                
            except OSError as e:
                pass
        self.connection.close()



class Server(threading.Thread):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind((self.ip, self.port))
        self.my_socket.listen(200)
        while True:
            self.connection, self.client_address = self.my_socket.accept()
            now = datetime.datetime.now().time().strftime('%H:%M:%S')
            logging.warning("connection from {0} at {1}".format(self.client_address, now))

            clt = ProcessTheClient(self.connection, self.client_address)
            logging.warning("created new thread to start")

            clt.start()
            self.the_clients.append(clt)



def main():
	svr = Server('localhost', 45000)
	svr.start()

if __name__=="__main__":
	main()