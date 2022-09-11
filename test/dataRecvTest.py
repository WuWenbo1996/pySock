import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.sendto("hello".encode("utf-8"), ("106.52.100.218", 10001))