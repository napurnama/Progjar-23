import socket
import logging
from threading import Thread
import time

logging.basicConfig(level=logging.INFO)

class Client(Thread):
    def __init__(self, ip, port):
        self.addr_fam = socket.AF_INET
        self.stream = socket.SOCK_STREAM
        self.sock = socket.socket(self.addr_fam, self.stream)
        self.ip = ip
        self.port = port
        Thread.__init__(self)

    def run(self):
        logging.info("Client running on thread {}", self.ident)
        try:
            server_address = (self.ip, self.port)
            logging.info(f"connecting to {server_address}")
            self.sock.connect(server_address)
            message = 'TIME\r\n'
            logging.info(f"sending {message}")
            self.sock.sendall(message.encode())
            data = self.sock.recv(16)
            if data:
                data = data.decode()
                if data[-2:] == '\r\n' and len(data) == 14:
                    logging.info(f"{data}")
            else:
                logging.info(f"ERROR: Invalid Server Response Format")              
        except Exception as ee:
            logging.info(f"ERROR: {str(ee)}")
            exit(0)
        finally:
            logging.info("closing")
            self.sock.close()

if __name__ == "__main__":
    for i in range(1000):
        clt = Client("localhost", 45000)
        clt.start()