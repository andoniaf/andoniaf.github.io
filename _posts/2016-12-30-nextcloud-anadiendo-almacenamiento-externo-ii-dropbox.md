---
layout: post
title: Nextcloud – Añadiendo almacenamiento externo II (Dropbox)
date: 2016-12-30 13:37
author: Andoni A.
categories: Linux
tags: [cloud, linux, nextcloud, selfhosted]
---
En la entrada anterior configurábamos Samba como <strong>almacenamiento externo</strong> para Nextcloud, hoy toca <strong>Dropbox</strong>. Vamos directos al grano:

<strong>1. Para poder conectar Dropbox dentro de Nextcloud debemos crear nuestra propia App desde <a href="http://www.dropbox.com/developers">aqui</a>:</strong>

<img class="aligncenter size-full wp-image-187" src="http://blogdeandoniaf.files.wordpress.com/2016/11/dropbox1.png" alt="Nextcloud - Externo" width="302" height="317" />

<strong>2. Seleccionamos "Dropbox API", escogemos el tipo de acceso y el nombre de la app:</strong>

<img class="aligncenter size-full wp-image-186" src="http://blogdeandoniaf.files.wordpress.com/2016/11/seleccic3b3n_651.png" alt="Nextcloud - Externo" width="826" height="792" />

<strong>3. Una vez se cree la App en el apartado de configuración encontraremos los datos necesarios para conectar Dropbox con Nextcloud:</strong>

<img class="aligncenter wp-image-185" src="http://blogdeandoniaf.files.wordpress.com/2016/11/seleccic3b3n_652.png" alt="Nextcloud - Externo" width="404" height="91" />

<strong>4. Vamos al panel de administración de Nextcloud, apartado de External storages y seleccionamos Dropbox:
</strong>

<img class="aligncenter size-full wp-image-189" src="http://blogdeandoniaf.files.wordpress.com/2016/11/seleccic3b3n_649.png" alt="Nextcloud - Externo" width="405" height="119" />

<strong>5. Rellenamos los datos:</strong>

<a href="http://blogdeandoniaf.files.wordpress.com/2016/11/seleccic3b3n_653.png"><img class="aligncenter wp-image-184" src="https://blogde-andoniaf.rhcloud.com/wp-content/uploads/2016/11/Selección_653-1024x34.png" alt="Nextcloud - Externo" width="1126" height="37" /></a>

&nbsp;

Y al igual que con Samba nos aparecerá una nueva carpeta que accederá a nuestros archivos de Dropbox:

<img class="aligncenter size-full wp-image-210" src="http://blogdeandoniaf.files.wordpress.com/2016/11/seleccic3b3n_655.png" alt="Nextcloud - Externo" width="159" height="156" />

Esto facilitará el intercambio de archivos entre ambas plataformas, en caso de que sigamos queriendo usar Dropbox después de configurar nuestra propia "Nube".

Porque recordar que...

<img class="alignright" src="https://images.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.bradnash.com%2Fwp-content%2Fuploads%2F2016%2F02%2Fno-cloud.png&amp;f=1" alt="" width="306" height="247" />

&nbsp;

&nbsp;

&nbsp;

&nbsp;

<em>Saludos y que la fuerza os acompañe!</em>
