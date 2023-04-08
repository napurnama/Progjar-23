from socket import *
import socket
import threading
import datetime
import logging
from multiprocessing.pool import ThreadPool


def run(connection):
    res=""
    logging.warning("THIS IS THE RUN!")
    while True:
        try:
            data = connection.recv(32)
            if data:
                data = data.decode()
                if data[-2:] == '\r\n':
                    now = datetime.datetime.now()
                    now = now.time().strftime('%H:%M:%S')
                    res = "JAM " + now + '\r\n'
                    connection.sendall(res.encode())
                    res = ""
                else:
                    res = "ERR 404: {}".format(data)
                    connection.sendall(res.encode())
                    break
            connection.close()
            
        except OSError as e:
            pass
    connection.close()



class Server(threading.Thread):
    def __init__(self, ip, port, pool_size):
        self.ip = ip
        self.port = port
        self.pool_size = pool_size
        self.pool = ThreadPool(processes=pool_size)
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind((self.ip, self.port))
        self.my_socket.listen(self.pool_size)
        while True:
            self.connection, self.client_address = self.my_socket.accept()
            now = datetime.datetime.now().time().strftime('%H:%M:%S')
            logging.warning("connection from {0} at {1}".format(self.client_address, now))

            # run(self.connection)
            self.the_clients.append(self.pool.apply_async(run, args=(self.connection, )))



def main():
	svr = Server('localhost', 45000, 10)
	svr.start()

if __name__=="__main__":
	main()