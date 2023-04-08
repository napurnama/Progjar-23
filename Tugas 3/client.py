import socket
import logging

logging.basicConfig(level=logging.INFO)

try:
    addr_fam = socket.AF_INET
    stream = socket.SOCK_STREAM
    sock = socket.socket(addr_fam, stream)
    server_address = ('localhost', 45000)
    logging.info(f"connecting to {server_address}")
    sock.connect(server_address)

    message = 'TIME\r\n'
    logging.info(f"sending {message}")
    sock.sendall(message.encode())
    data = sock.recv(16)
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
    sock.close()