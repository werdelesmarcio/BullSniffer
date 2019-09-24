# BullSniffer <img src="https://github.com/werdelesmarcio/PyTCPScan/blob/master/icon.png" width=25> 

<img src="http://img.shields.io/liberapay/receives/scorpion.svg?logo=liberapay">  <img alt="AppVeyor" src="https://img.shields.io/appveyor/ci/werdelesmarcio/PyTCPScan">  [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=werdelesmarcio_PyTCPScan&metric=alert_status)](https://sonarcloud.io/dashboard?id=werdelesmarcio_PyTCPScan)  <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/werdelesmarcio/PyTCPScan">  <img alt="GitHub" src="https://img.shields.io/github/license/werdelesmarcio/PyTCPScan">  <img alt="Twitter URL" src="https://img.shields.io/twitter/url/https/twitter.com/ScorpionInc?style=social">

Repositório para a aplicação BullSniffer.

PyTCPScan é uma ferramenta em fase de desnenvolvimento, voltada para estudo de redes e
é direcionada para sistemas GNU/Linux. Faz uma escuta em Promiscuous Mode e captura info
da rede onde é executado.

---

OBS.: Para usar como executável, lembrar de dar permissão de execução
**sudo chmod +x bullsniffer.py**

## Execução 
Para executar a aplicação deve passar o argumento com o host do alvo que terá
o fluxo de dados que entra e que sai dele enviados para o atacante.

**./bullsniffer [target]**

```
             ""8"" 8""""8 8""""8 8""""8                   
  eeeee e    e 8   8    " 8    8 8      eeee eeeee eeeee 
  8   8 8    8 8e  8e     8eeee8 8eeeee 8  8 8   8 8   8 
  8eee8 8eeee8 88  88     88         88 8e   8eee8 8e  8 
  88      88   88  88   e 88     e   88 88   88  8 88  8 
  88      88   88  88eee8 88     8eee88 88e8 88  8 88  8 
----------------------------------------------------------
                                       PyTCPScan ver 1.0 
                                               By: GH05T 
                                    VAULT CYBER SECURITY 
----------------------------------------------------------
 [*]Connecting to Target: xxxxxxxxxxxx.com.br
 [*]Scanning ports between 21 and 110 ...
 
 [!]Please wait, scanning remote host XXX.XX.XXX.XXX
 [*]This may take a while, be patient.
 
 [+]POSITIVE TO Port 21:	Status: OPEN
 [+]POSITIVE TO Port 22:	Status: OPEN
 [+]POSITIVE TO Port 80:	Status: OPEN
--------------------------------------------------
 [!]Scanning Completed in:  0:00:44.584693
--------------------------------------------------

 ---Finished---

```

***O código-fonte está sob Licença GLP e é livre para aceita contribuição.***


<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/werdelesmarcio/PyTCPScan?style=for-the-badge">   <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/werdelesmarcio/PyTCPScan?style=for-the-badge">


<img src = "https://github.com/werdelesmarcio/Imagens/blob/master/Selos/OpenSource.png?raw=true" width=50 align="left"><img src = "https://github.com/werdelesmarcio/Imagens/blob/master/Selos/PoweredByLinux.png?raw=true" width =50 align="center"><img src = "https://github.com/werdelesmarcio/Imagens/blob/master/Selos/SoftwareLivre.png?raw=true" width=50 align="right">
