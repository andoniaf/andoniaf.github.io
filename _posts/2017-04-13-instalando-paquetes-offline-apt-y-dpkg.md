---
layout: post
title: Instalando paquetes Offline - apt y dpkg
date: 2017-04-13 13:13
author: Andoni A.
categories: [Linux]
---
En ocasiones podemos encontrarnos, como me ha ocurrido a mi hace poco, con la necesidad de instalar algún paquete en una máquina que no tenga acceso a Internet. En estos casos el típico <code>apt-get install $pkg</code> no va a funcionar, ¿entonces como podemos instalar lo que necesitamos?
<h4 id="1-localizar-informaci-n-del-paquete-">1. Localizar información del paquete:</h4>
En mi caso tenía que instalar el servicio SNMP en un servidor Ubuntu para poder monitorizarlo, asi que lo primero que hice fue localizar la información del paquete:
<pre class="code">root@antman:~# apt-cache show snmpd
Package: snmpd
Priority: optional
Section: net
Installed-Size: 227
Maintainer: Ubuntu Developers &lt;ubuntu-devel-discuss@lists.ubuntu.com&gt;
Original-Maintainer: Net-SNMP Packaging Team &lt;pkg-net-snmp-devel@lists.alioth.debian.org&gt;
Architecture: amd64
Source: net-snmp
Version: 5.7.2~dfsg-8.1ubuntu3.2
Depends: libc6 (&gt;= 2.4), libmysqlclient18 (&gt;= 5.5.24+dfsg-1), libsnmp30 (&gt;= 5.7.2~dfsg), libwrap0 (&gt;= 7.6-4~), debconf (&gt;= 0.5) | debconf-2.0, adduser, debconf, lsb-base (&gt;= 3.2-13), libsnmp-base
Filename: pool/main/n/net-snmp/snmpd_5.7.2~dfsg-8.1ubuntu3.2_amd64.deb
Size: 73254
MD5sum: eb442d99cb4d1fdec4461a60efe3392d
SHA1: 8e5af0cab031bff9b7290add006ab239a96424e3
SHA256: 2e88e59dac645685f33d49195c6c2b3757641bed248501ef5dcc9a86d70c1bfb
Description-es: SNMP (Simple Network Management Protocol) agents
El protocolo de gestión sencilla de redes (SNMP) proporciona un entorno
para intercambiar información de gestión entre agentes (servidores) y
clientes.
.
The Net-SNMP agent is a daemon which listens for incoming SNMP requests
from clients and provides responses.
Description-md5: 9dc6ec703377042ed23b16c47ed5cb6c
Homepage: http://net-snmp.sourceforge.net/
Bugs: https://bugs.launchpad.net/ubuntu/+filebug
Origin: Ubuntu
Supported: 5y</pre>
<div class="line">De toda esa información lo que más nos interesa es:</div>
<pre class="code">Version: 5.7.2~dfsg-8.1ubuntu3.2
Filename: pool/main/n/net-snmp/snmpd_5.7.2~dfsg-8.1ubuntu3.2_amd64.deb
MD5sum: eb442d99cb4d1fdec4461a60efe3392d</pre>
<div class="line"></div>
<h4 id="2-descargar-el-paquete-">2. Descargar el paquete:</h4>
Una vez tenemos esa información, desde otro equipo podemos descargarnos el paquete desde un repo como: <a href="http://es.archive.ubuntu.com/ubuntu">http://es.archive.ubuntu.com/ubuntu/$rutaPaquete</a> , por ejemplo:

<a href="http://es.archive.ubuntu.com/ubuntu/pool/main/n/net-snmp/libsnmp-base_5.4.3~dfsg-2.4ubuntu1.3_all.deb">http://es.archive.ubuntu.com/ubuntu/pool/main/n/net-snmp/libsnmp-base_5.4.3~dfsg-2.4ubuntu1.3_all.deb</a>

Si no conocemos ninguno podemos consultar el fichero <code>/etc/apt/sources.list </code>de la máquina donde se va a instalar.

La $rutaPaquete la sacamos del paso anterior, es el "Filename"; cuando este descargado el fichero podemos comprobar que el MD5sum coincide:
<pre class="code">[root@centos-test:/var/sftp]# md5sum snmpd_5.7.2~dfsg-8.1ubuntu3_amd64.deb
1339b13be467d99af97c784b001dc655  snmpd_5.7.2~dfsg-8.1ubuntu3_amd64.deb</pre>
Hay que comprobar si coincide con el obtenido en el primer paso, así nos aseguramos que sea el paquete correcto, después lo pasamos a la máquina ( por ssh, sftp, etc) .
<h4 id="3-instalaci-n-del-paquete-">3. Instalación del paquete:</h4>
Ahora que tenemos el paquete en la máquina accedemos a la ruta donde lo hayamos y lo instalamos con:
<pre class="code">dpkg -i $PKG.deb</pre>
En este punto hay dos opciones: que el paquete puede instalarse sin problemas, o lo que es más normal, nos de un error de dependencias como este:
<pre class="code">root@venom:/home/admindef# dpkg -i snmpd_5.7.2~dfsg-8.1ubuntu3_amd64.deb
Seleccionando el paquete snmpd previamente no seleccionado.
(Leyendo la base de datos ... 56075 ficheros o directorios instalados actualmente.)
Preparing to unpack snmpd_5.7.2~dfsg-8.1ubuntu3_amd64.deb ...
Unpacking snmpd (5.7.2~dfsg-8.1ubuntu3) ...
dpkg: problemas de dependencias impiden la configuración de snmpd:
snmpd depende de libmysqlclient18 (&gt;= 5.5.24+dfsg-1); sin embargo:
El paquete `libmysqlclient18' no está instalado.
snmpd depende de libsnmp30 (&gt;= 5.7.2~dfsg); sin embargo:
El paquete `libsnmp30' no está instalado.
snmpd depende de libsnmp-base; sin embargo:
El paquete `libsnmp-base' no está instalado.dpkg: error processing package snmpd (--install):
problemas de dependencias - se deja sin configurar
Processing triggers for ureadahead (0.100.0-16) ...
Processing triggers for man-db (2.6.7.1-1ubuntu1) ...
Se encontraron errores al procesar:
snmpd</pre>
Si ocurre esto tendremos que realizar los pasos anteriores con todas las dependencias antes de volver a intentar instalar el paquete que necesitábamos.

Y claro, estas dependencias pueden tener a sus vez  más dependencias... En mi caso acabé instalando todos estos paquetes:
```
[root@centos-test:/var/sftp/jail_operaciones/datos]# md5sum *.deb
1e6091db1981386e55898d787b831eda  libmysqlclient18_5.5.35+dfsg-1ubuntu1_amd64.deb
1bbe27c70dbf9d4bce15d57cc317ca3f  libperl5.18_5.18.2-2ubuntu1.1_amd64.deb
042d478dd8c2f8d47fe197b2bbf2e8a1  libsensors4_3.3.4-2ubuntu1_amd64.deb
c4359a72ce136c2538b27df9f1584f47  libsnmp30_5.7.2~dfsg-8.1ubuntu3_amd64.deb
bf7e5ff1d27d12703fb37b82f2e13bac  libsnmp-base_5.7.2~dfsg-8.1ubuntu3_all.deb
073fc2420db6acb4ec3b00264d84d03a  mysql-common_5.5.35+dfsg-1ubuntu1_all.deb<
1339b13be467d99af97c784b001dc655  snmpd_5.7.2~dfsg-8.1ubuntu3_amd64.deb
```
Como siempre, espero que os sea útil.

<em>Saludos y que la fuerza os acompañe!</em>
