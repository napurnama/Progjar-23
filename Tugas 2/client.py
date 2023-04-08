import sys
import socket
import logging

#set basic logging
logging.basicConfig(level=logging.INFO)

try:
    # Create a TCP/IP socket
    addr_fam = socket.AF_INET
    stream = socket.SOCK_STREAM
    sock = socket.socket(addr_fam, stream)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 45000)
    logging.info(f"connecting to {server_address}")
    sock.connect(server_address)

    # Send data
    # message = 'TIME\r\n'
    message = "AKSDMAIWJKENDALKJWN"
    logging.info(f"sending {message}")
    sock.sendall(message.encode())
    # Look for the response
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