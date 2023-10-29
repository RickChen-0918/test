import socket
import ssl

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
context = socket.SSLContext(ssl.PROTOCOL_TLSv1_2)
