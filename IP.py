import socket
import struct

# Initialize socket for IPv6 datagrams
server_socket = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('', 8080))  # Binds to all interfaces on port 8080

# Allow messages from this socket to loop back for development
server_socket.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_LOOP, True)

# Construct message for joining a multicast group (e.g., ff02::abcd:1)
mreq = struct.pack("16s15s", socket.inet_pton(socket.AF_INET6, "ff02::abcd:1"), (chr(0) * 16).encode('utf-8'))
server_socket.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_JOIN_GROUP, mreq)

data, addr = server_socket.recvfrom(1024)
print(f"Received from {addr}: {data.decode('utf-8')}")
