# BullSniffer <img src="https://github.com/werdelesmarcio/BullSniffer/blob/master/bullsniffericon.png" width=25> 

<img src="http://img.shields.io/liberapay/receives/scorpion.svg?logo=liberapay">  <img alt="AppVeyor" src="https://img.shields.io/appveyor/ci/werdelesmarcio/BullSniffer">  [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=werdelesmarcio_BullSniffer&metric=alert_status)](https://sonarcloud.io/dashboard?id=werdelesmarcio_BullSniffer)  <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/werdelesmarcio/BullSniffer">  <img alt="GitHub" src="https://img.shields.io/github/license/werdelesmarcio/BullSniffer">  <img alt="Twitter URL" src="https://img.shields.io/twitter/url/https/twitter.com/ScorpionInc?style=social">

Repositório para a aplicação BullSniffer.

## O que é um sniffer?
Um sniffer não é necessariamente malicioso. Na verdade, este tipo de software é usado com 
frequência para monitorar e analisar o tráfego de rede para detectar problemas e manter um 
fluxo eficiente. 

No entanto, um sniffer também pode ser usado com má fé. Eles capturam tudo o que passa por
eles, inclusive senhas e nomes de usuários não criptografados. Dessa forma, os hackers com
acesso a um sniffer terão acesso também a qualquer conta que passar por ele. Além disso, um 
sniffer pode ser instalado em qualquer computador conectado a uma rede local. 

Ele não precisa ser instalado no próprio aparelho que se deseja monitorar. Em outras palavras,
ele pode permanecer oculto durante a conexão.

## O BullSniffer
BullSniffer é uma ferramenta do tipo Sniffer que está em fase de desnenvolvimento e é voltada
para análises de fluxo de redes. É direcionada para sistemas GNU/Linux. Ela faz uma escuta em 
Modo Promíscuo _(Promiscuous Mode)_ e captura informações que estejam trafegando pela rede.

---

_OBS.: Para usar como executável, lembrar de dar permissão de execução_
**sudo chmod +x bullsniffer.py**

---

## Execução 
Para executar a aplicação, apenas deve-se digitar o nome ou o caminho, se não tiver sido enviada
para o PATH, quando estiver conectado a rede que se quer Sniffar. Só lembrando de que para executar
a aplicação você deve ser **root**

**sudo ./bullsniffer**

_Exemplo de Resposta:_

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

<omitido>

```

***O código-fonte está sob Licença GLP e é livre para aceita contribuição.***


<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/werdelesmarcio/BullSniffer?style=for-the-badge">   <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/werdelesmarcio/BullSniffer?style=for-the-badge">


<img src = "https://github.com/werdelesmarcio/Imagens/blob/master/Selos/PoweredByLinux.png?raw=true" width =80 align="right">
