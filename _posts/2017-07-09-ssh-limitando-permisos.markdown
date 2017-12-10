---
layout: post
title:  "SSH – Limitando permisos en claves RSA"
date:   2017-07-09 13:13:13
author: Andoni Alonso
categories: Linux Seguridad
---

<p style="text-align:left;">Hoy traigo una entrada <em>express</em> sobre una función muy interesante que desconocía de las conexiones mediante <strong>claves RSA</strong>, y es la posibilidad (entre otros) de restringir desde que equipos se usan dichas claves o los comandos que pueden ejecutar.</p>
Lo veo muy útil para, por ejemplo, tareas específicas como la realización de un <strong>backup</strong>.

Podemos limitar la clave para que solo funcione desde un único equipo de nuestra red y solo tenga permitido usar el script que se encarga de hacer las copias de seguridad:
<pre class="code">from="nas.marvel.lan", command="/usr/scripts/backup_semanal" ssh-rsa AAAA...V9S7 userbck@marvel.lan</pre>
Si intentamos usar esa clave para ejecutar cualquier otro comando comprobaremos que solo se ejecuta el <em>permitido</em> "backup-semanal":
<pre class="code">userbck@nas:~> ssh -i clave_bck webserver 'backup_semanal'
## BACKUP SEMANAL ##
¿Desea crear una nueva copia semanal? (s/n) n
Saliendo...
userbck@nas:~> ssh -i clave_bck webserver 'df'
## BACKUP SEMANAL ##
¿Desea crear una nueva copia semanal? (s/n) n
Saliendo...
userbck@nas:~> ssh -i clave_bck webserver 'w'
## BACKUP SEMANAL ##
¿Desea crear una nueva copia semanal? (s/n) n
Saliendo...</pre>
De esta forma aplicamos un par de conceptos básicos de la seguridad: el principio de <strong>menor exposición</strong> y el de <strong>mínimo privilegio</strong>.


<p style="text-align:left;">Tenéis más información acerca del fichero authorized_keys y sus opciones <a href="http://man.openbsd.org/OpenBSD-current/man8/sshd.8#AUTHORIZED_KEYS_FILE_FORMAT">aquí</a>.</p>
<p style="text-align:left;"><em>~ Saludos y que la fuerza os acompañe!</em></p>
