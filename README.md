# BullSniffer <img src="https://github.com/werdelesmarcio/PyTCPScan/blob/master/icon.png" width=25> 

<img src="http://img.shields.io/liberapay/receives/scorpion.svg?logo=liberapay">  <img alt="AppVeyor" src="https://img.shields.io/appveyor/ci/werdelesmarcio/BullSniffer">  [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=werdelesmarcio_BullSniffer&metric=alert_status)](https://sonarcloud.io/dashboard?id=werdelesmarcio_BullSniffer)  <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/werdelesmarcio/BullSniffer">  <img alt="GitHub" src="https://img.shields.io/github/license/werdelesmarcio/BullSniffer">  <img alt="Twitter URL" src="https://img.shields.io/twitter/url/https/twitter.com/ScorpionInc?style=social">

Repositório para a aplicação BullSniffer.

BullSniffer é uma ferramenta em fase de desnenvolvimento, voltada para estudo de redes e
é direcionada para sistemas GNU/Linux. Faz uma escuta em Promiscuous Mode e captura info
da rede onde é executado.

---

OBS.: Para usar como executável, lembrar de dar permissão de execução
**sudo chmod +x bullsniffer.py**

## Execução 
Para executar a aplicação deve passar o argumento com o host do alvo que terá
o fluxo de dados que entra e que sai dele enviados para o atacante.

**sudo ./bullsniffer**

```  ___________                               
    / ========= \                              
   /_____________\                             
  | _____________ |                            
  | | -         | |                            
  | |           | |                            
  | |___________| |__________________________  
  |_=_____________|       BULLSNIFFER        ) 
  / ::::::::::::: \       VERSION 1.0       /  
 / ::::::::::::::: \      BY: GHOST     =D-'   
(___________________)                          

Destination MAC: 00:1a:dd:ba:3d:a1
Source MAC: b4:74:9f:86:8e:7e
Protocol: 8
Version: 4 IP Header Length: 5 TTL: 64 Protocol: 6 Source Address: 192.168.1.114 Destination Adress: 172.217.172.196
Source Port: 38860 Dest. Port: 443 Sequence Number: 419090580 Acknowledgement: 1231236271 TCP Header Length: 8
Data: 

Destination MAC: b4:74:9f:86:8e:7e
Source MAC: 00:1a:dd:ba:3d:a1
Protocol: 8
Version: 4 IP Header Length: 5 TTL: 118 Protocol: 6 Source Address: 172.217.172.196 Destination Adress: 192.168.1.114
Source Port: 443 Dest. Port: 38860 Sequence Number: 1231236271 Acknowledgement: 419090580 TCP Header Length: 8
Data: ߋ��D`���0X���
�

Destination MAC: 00:1a:dd:ba:3d:a1
Source MAC: b4:74:9f:86:8e:7e
Protocol: 8
Version: 4 IP Header Length: 5 TTL: 64 Protocol: 6 Source Address: 192.168.1.114 Destination Adress: 172.217.172.196
Source Port: 38860 Dest. Port: 443 Sequence Number: 419090580 Acknowledgement: 1231237689 TCP Header Length: 8
Data: 

Destination MAC: b4:74:9f:86:8e:7e
Source MAC: 00:1a:dd:ba:3d:a1
Protocol: 8
Version: 4 IP Header Length: 5 TTL: 118 Protocol: 6 Source Address: 172.217.172.196 Destination Adress: 192.168.1.114
Source Port: 443 Dest. Port: 38860 Sequence Number: 1231237689 Acknowledgement: 419090580 TCP Header Length: 8
Data: ���.58��\��F$��`��8ń.I�?�g4ӣ�f6R.|u,���q�����\��C�4>�WԷ"�@�II/�#Z`Y�N�E�k�ӗ��)]�&Y��{�5��9

...

```

***O código-fonte está sob Licença GLP e é livre para aceita contribuição.***


<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/werdelesmarcio/BullSniffer?style=for-the-badge">   <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/werdelesmarcio/BullSniffer?style=for-the-badge">


<img src = "https://github.com/werdelesmarcio/Imagens/blob/master/Selos/OpenSource.png?raw=true" width=50 align="left"><img src = "https://github.com/werdelesmarcio/Imagens/blob/master/Selos/PoweredByLinux.png?raw=true" width =50 align="center"><img src = "https://github.com/werdelesmarcio/Imagens/blob/master/Selos/SoftwareLivre.png?raw=true" width=50 align="right">
