# BullSniffer <img src="https://github.com/werdelesmarcio/BullSniffer/blob/master/bullsniffericon.png" width=25> 

[![Maintainability](https://api.codeclimate.com/v1/badges/52c8f10ce940f001945d/maintainability)](https://codeclimate.com/github/werdelesmarcio/BullSniffer/maintainability)   [![Test Coverage](https://api.codeclimate.com/v1/badges/52c8f10ce940f001945d/test_coverage)](https://codeclimate.com/github/werdelesmarcio/BullSniffer/test_coverage)  <img alt="AppVeyor" src="https://img.shields.io/appveyor/ci/werdelesmarcio/BullSniffer">  [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=werdelesmarcio_BullSniffer&metric=alert_status)](https://sonarcloud.io/dashboard?id=werdelesmarcio_BullSniffer)  <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/werdelesmarcio/BullSniffer">  <img alt="GitHub" src="https://img.shields.io/github/license/werdelesmarcio/BullSniffer">  <img alt="Twitter URL" src="https://img.shields.io/twitter/url/https/twitter.com/ScorpionInc?style=social">

Repository for the BullSniffer application.

## What is a sniffer?
A sniffer is not necessarily a malicious application. In fact, this software is often used to monitor and analyze network traffic to detect potential problems and maintain more efficient data flow.

However, a sniffer can also be used for dubious purposes as it captures everything that passes through the analyzed network, including passwords and unencrypted usernames (plain text).

This way hackers who use a sniffer and have access to a network will have access to any information that travels through it. Also, some sniffers do not need to be installed on a computer connected to a local area network and can even be run via flash drives.

## BullSniffer
BullSniffer is a sniffer-type tool under development that focuses on network flow analysis. It is developed for GNU/Linux systems. It listens in _promiscuous mode_ and captures information that is traveling across the target network.

_Note: To use as executable, remember to give execute permission._
**sudo chmod +x bullsniffer.py**

---

## Execution
To run the application, you only need to enter the name _(or path if it has not been sent to the PATH)_ when connected to the network you want to sniff. Just remembering that to run the app you must be **root**

**sudo ./bullsniffer**

_Exemple:_

```  ___________                               
    / ========= \                              
   /_____________\                             
  | _____________ |                            
  | | -         | |                            
  | |           | |                            
  | |___________| |________________________________  
  |_=_____________|          BULLSNIFFER           ) 
  / ::::::::::::: \          VERSION 1.0          /  
 / ::::::::::::::: \      BY: Werdeles Soares =D-'   
(___________________)    Vault Cyber Security                        

------------------------------
Destination MAC: 00:1a:dd:ba:3d:a1
Source MAC: b4:74:9f:86:8e:7e
Protocol: 8
Version: 4
IP Header Length: 5 TTL: 64
Protocol: 6
Source Address: 192.168.1.114
Destination Adress: 149.154.175.205
Source Port: 49828 Dest. Port: 443
Sequence Number: 168534950
Acknowledgement: 2729051853
TCP Header Length: 8
Data: 53�*�����e�ÚZ)����<i�x�T���鳇`�c�X�	�ײ���K���Ky/�=�H�����dޢ�ʔo�F6����������mLeZ��P�$��B��Wε�^[L���o�h��:9
                                                                                                                     Jt�֨��=┦:��f�'��o ,���:<�\(j��Yǭ�j?��ѳk`_�>��)�E�z�*� |ʽM�V"U\� Hy7���o����������i7����B8�����PW��"�euX`@���
���HB�$(�rE�h��т3ضwiq�.AI&��n�.aR׮��/�ս��fTݒ<�
      ��6��ێ�e+d�@|Z�/u�#{wL�����ZUG�Di�r
  /QS~]=�/�lk�;��	�Y��&4ҳ��j�4Xt	6�4�Ck��{��(_��=1IUp�_x�R�;@+8�z"�Zg�%��#f9�m�I

------------------------------
------------------------------
Destination MAC: b4:74:9f:86:8e:7e
Source MAC: 00:1a:dd:ba:3d:a1
Protocol: 8
Version: 4
IP Header Length: 5 TTL: 54
Protocol: 6
Source Address: 149.154.175.205
Destination Adress: 192.168.1.114
Source Port: 443 Dest. Port: 49828
Sequence Number: 2729051853
Acknowledgement: 168535520
TCP Header Length: 8
Data: 

------------------------------

<omitted>

```

***The source code is under GPL License and is free to accept contributions..***


<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/werdelesmarcio/BullSniffer?style=for-the-badge">   <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/werdelesmarcio/BullSniffer?style=for-the-badge">


<img src = "https://github.com/werdelesmarcio/Imagens/blob/master/Selos/PoweredByLinux.png?raw=true" width =80 align="right">
