#!/usr/bin/python

# -*- coding: utf-8 -*-

import socket
import sys
import os
from struct import *
import subprocess
from datetime import datetime

from banner import *

# Limpa a tela ao executar a Aplicação
subprocess.call('clear', shell=True)

banner() #Chama o Banner da Aplicação

# Convertendo uma string de 6 caracteres de endereco ethernet
# em uma sequencia hexadecimal separada por dois pontos (Padrão do Endereço MAC
def eth_addr(a):
    b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (
        ord(a[0]), ord(a[1]), ord(a[2]), ord(a[3]), ord(a[4]), ord(a[5]))
    return b

# Criando um AF_PACKET do tipo raw_socket
# Definindo ETH_P_ALL   0x0003  /*todos os pacotes.*/
try:
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
except socket.error as msg:
    print('Socket could not be created. Error Code: ' +
          str(msg[0]) + 'Message ' + msg[1])
    sys.exit()

# Recebendo os Pacotes
while True:
    packet = s.recvfrom(65565)

    # String dos pacotes com tuplas
    packet = packet[0]

    # Analisando o cabecalho Ethernet
    eth_length = 14

    eth_header = packet[:eth_length]
    eth = unpack('!6s6sH', eth_header)
    eth_protocol = socket.ntohs(eth[2])
    print('Destination MAC: ' + eth_addr(packet[0:6]) +
          '\nSource MAC: ' + eth_addr(packet[6:12]) +
          '\nProtocol: ' + str(eth_protocol))

    # Analisar os Pacotes IP com o protocolo = 8
    if eth_protocol == 8:
        # Analisar o cabecalho IP
        # Capiturando os primeiros 20 caracteres do cabecalho IP
        ip_header = packet[eth_length:20 + eth_length]

        # Agora desenpacota os dados
        iph = unpack('!BBHHHBBH4s4s', ip_header)

        version_ihl = iph[0]
        version = version_ihl >> 4
        ihl = version_ihl & 0xF

        iph_length = ihl * 4

        ttl = iph[5]
        protocol = iph[6]
        s_addr = socket.inet_ntoa(iph[8])
        d_addr = socket.inet_ntoa(iph[9])

        print('Version: ' + str(version) +
              ' IP Header Length: ' + str(ihl) +
              ' TTL: ' + str(ttl) +
              ' Protocol: ' + str(protocol) +
              ' Source Address: ' + str(s_addr) +
              ' Destination Adress: ' + str(d_addr))

        # Protocolo TCP
        if protocol == 6:
            t = iph_length + eth_length
            tcp_header = packet[t:t+20]

            # Agora desenpacota os dados
            tcph = unpack('!HHLLBBHHH', tcp_header)

            source_port = tcph[0]
            dest_port = tcph[1]
            sequence = tcph[2]
            acknowledgement = tcph[3]
            doff_reserved = tcph[4]
            tcph_length = doff_reserved >> 4

            print('Source Port: ' + str(source_port) +
                  ' Dest. Port: ' + str(dest_port) +
                  ' Sequence Number: ' + str(sequence) +
                  ' Acknowledgement: ' + str(acknowledgement) +
                  ' TCP Header Length: ' + str(tcph_length))

            h_size = eth_length + iph_length + tcph_length * 4
            data_size = len(packet) - h_size

            # Pegar os dados do pacote
            data = packet[h_size:]

            print('Data: ' + data)

        # Pacotes ICMP
        elif protocol == 1:
            u = iph_length + eth_length
            icmp_length = 4
            icmp_header = packet[u:u+4]

            # Agora desenpacota os dados
            icmph = unpack('!BBH', icmp_header)
            icmp_type = icmph[0]
            code = icmph[1]
            checksum = icmph[2]

            print('Type: ' + str(icmp_type) +
                  ' Code: ' + str(code) +
                  ' Checksum: ' + str(checksum))

            h_size = eth_length + iph_length + icmp_length
            data_size = len(packet) - h_size

            # Pegar os dados do pacote
            data = packet[h_size:]

            print('Data: ' + data)

        # Protocolo UDP
        elif protocol == 17:
            u = iph_length + eth_length
            udph_length = 8
            udp_header = packet[u:u+8]

            # Agora desenpacota os dados
            udph = unpack('!HHHH', udp_header)

            source_port = udph[0]
            dest_port = udph[1]
            length = udph[2]
            checksum = udph[3]

            print('Source Port: ' + str(source_port) +
                  ' Dest. Port: ' + str(dest_port) +
                  ' Length: ' + str(length) +
                  ' Checksum: ' + str(checksum))

            h_size = eth_length + iph_length + udph_length
            data_size = len(packet) - h_size

            # Pegando os dados do pacote
            data = packet[h_size:]

            print('Data: ' + data)

    # Algum outro pacote IP com IGMP
    else:
        print('Protocol other than TCP/UDP/ICMP')
    print
