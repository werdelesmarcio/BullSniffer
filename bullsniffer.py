#!/usr/bin/env python

# -*- coding: utf-8 -*-

import socket
import sys
import os
import subprocess
from datetime import datetime

#Limpa a tela ao executar a aplicacao
subprocess.call('clear', shell=True)

print("     _________                               ")
print("    / ======= \                              ")
print("   /___________\                             ")
print("  | ___________ |                            ")
print("  | | -       | |                            ")
print("  | |         | |                            ")
print("  | |_________| |__________________________  ")
print("  |_=___________|       BULLSNIFFER        ) ")
print("  / ::::::::::: \       VERSION 1.0       /  ")
print(" / ::::::::::::: \      BY: GHOST     =D-'   ")
print("(_________________)                          ")
print

	
host = raw_input("Digite o alvo: ")

if host == "":
	print("\n [!]ERROR: Missing input arguments.")
	print(" [!]Target not set.")
	print(" [!]Exiting application.\n")
	sys.exit(1)


# criando um raw socket e um bind para uma interface publica
if os.name == "nt":
    socket_protocol = socket.IPPROTO_IP
else:
    socket_protocol = socket.IPPROTO_ICMP

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

sniffer.bind((host, 0))

# queremos capturar o cabecalho do ip
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# se estivermos no Windows, nos temos que enviar um IOCTL
# para setar o modo promiscuo
if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# lendo o pacote
print sniffer.recvfrom(65565)

# se estivermos no Windows, temos que desligar o modo promiscuo
if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
