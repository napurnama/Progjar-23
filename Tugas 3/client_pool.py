import socket
import logging
from threading import Thread
from multiprocessing.pool import ThreadPool
import time

logging.basicConfig(level=logging.INFO)

class Client():
    def __init__(self, ip, port):
        self.addr_fam = socket.AF_INET
        self.stream = socket.SOCK_STREAM
        self.sock = socket.socket(self.addr_fam, self.stream)
        self.ip = ip
        self.port = port

def run(client):
    try:
        server_address = (client.ip, client.port)
        logging.info(f"connecting to {server_address}")
        client.sock.connect(server_address)
        message = 'TIME\r\n'
        logging.info(f"sending {message}")
        client.sock.sendall(message.encode())
        data = client.sock.recv(16)
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
        client.sock.close()

if __name__ == "__main__":
    pool = ThreadPool()
    for i in range(100):
        clt = Client("localhost", 45000)
        pool.apply_async(run, args=(clt,))