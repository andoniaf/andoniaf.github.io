---
layout: post
title: Nextcloud - Añadiendo almacenamiento externo I (SMB/CIFS)
date: 2016-12-17 13:37
author: Andoni A.
categories: Linux
tags: [cloud, linux, nextcloud, selfhosted]
---
Complementando la ultima entrada, en la que instalaba Nextcloud, ahora vamos a ver como añadir espacio usando la función de almacenamiento externo.

Nextcloud soporta varios tipos de almacenamiento externo. Yo he escogido <strong>Samba</strong> y <strong>Dropbox</strong> pero <a href="https://docs.nextcloud.com/server/9/admin_manual/configuration_files/external_storage_configuration_gui.html#available-storage-backends">aquí</a> podéis consultar todos los que están disponibles actualmente.

En esta entrada configuraremos <strong>Samba </strong>como almacenamiento externo. ¿Recordáis que <strong>SELinux</strong> podía dar problemas con los permisos a la hora de escribir en los archivos de configuración de Nextcloud?
Pues también da problemas a la hora de activar el almacenamiento externo... Así que lo primero que debemos hacer es ejecutar el comando siguiente para permitir al <strong>servicio httpd</strong> conectarse a una red remota:
<pre class="code">setsebool -P httpd_can_network_connect on</pre>
(<em>Estuve un rato buscando y buscando porque no funcionaba hasta que recordé al Sr. SELinux... ahora al lio</em>)

<strong>1. Primero hay que activar el plugin de Almacenamiento externo:</strong> <img class="aligncenter size-full wp-image-192" src="http://blogdeandoniaf.files.wordpress.com/2016/11/seleccic3b3n_645.png" alt="Nextcloud - Externo" width="587" height="187" />

<strong>2. Seleccionar los almacenamientos externos que queremos usar:
</strong>

En el <strong>panel de administración de Nextcloud</strong> aparecerá una nueva opción (External storages) donde podemos configurar:
<ul>
 	<li>Almacenamientos externos activos</li>
 	<li>Usuarios pueden/no pueden montar almacenamientos externos</li>
 	<li>Almacenamientos externos comunes para varios usuarios montados automáticamente<img class="wp-image-191 aligncenter" src="http://blogdeandoniaf.files.wordpress.com/2016/11/seleccic3b3n_646.png" alt="Nextcloud - Externo" width="619" height="360" />Yo he marcado Dropbox y SMB, ademas de permitir a los usuarios montar sus propios almacenamientos externos. <em>(¡OJO! Los usuarios solo podran montar los servicios que este activos.)</em></li>
</ul>
<strong>3. Seleccionamos el almacenamiento externo a configurar:
</strong>

<img class="aligncenter size-full wp-image-189" src="http://blogdeandoniaf.files.wordpress.com/2016/11/seleccic3b3n_649.png" alt="Nextcloud - Externo" width="405" height="119" />

<strong>4. Permitimos Samba/CIFS con SELinux:
</strong>
<p class="code"><code>setsebool -P httpd_use_cifs on</code></p>
Con este comando permitimos al <strong>servicio httpd</strong> usar CIFS.

<strong>5. Rellenamos los datos:</strong>

![Alm Ext]({{ "/assets/images/2016/nextcloud_02.png" | absolute_url }})

Con esto ya tendemos configurada la conexión, que nos aparecerá como una carpeta más dentro de Nextcloud:

<img class="aligncenter size-full wp-image-194" src="http://blogdeandoniaf.files.wordpress.com/2016/11/seleccic3b3n_654.png" alt="Nextcloud - Externo" width="129" height="56" />

En la próxima entrada configuraremos <strong>Dropbox </strong>como almacenamiento externo.

<em>Saludos y que la fuerza os acompañe!</em>
