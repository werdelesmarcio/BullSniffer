#!/usr/bin/python

import socket
import os

host = "192.168.56.1"

# criando um raw socket e um bind para uma interface publica
if os.name == "nt":
    socket_protocol = socket.IPPROTO_IP
else:
    socket_protocol = socket.IPPROTO_ICMP

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

sniffer.bind((host, 0))

# queremos capturar o cabeçalho do ip
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# se estivermos no Windows, nós temos que enviar um IOCTL
# para setar o modo promíscuo
if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# lendo o pacote
print sniffer.recvfrom(65565)

# se estivermos no Windows, temos que desligar o modo promiscuo
if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
