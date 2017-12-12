---
layout: post
title: Nextcloud - Añadiendo un segundo factor de autenticación
date: 2017-01-13 14:37
author: Andoni A.
categories: Linux
tags: [cloud, Linux, nextcloud, Selfhosted]
---
Continuando con Nextcloud, he encontrado un plugin muy interesante que permite habilitar un segundo factor de autenticación en nuestra Nube.

Se llama "<a href="https://github.com/nextcloud/twofactor_totp">Two Factor TOTP Provider</a>" y podéis descargarlo desde el <a href="https://apps.nextcloud.com/apps/twofactor_totp/releases?platform=11#11">aqui.</a>


La <strong>instalación</strong> es muy sencilla:

Descargamos todos los archivos y los copiamos a nuestro servidor, dentro de la carpeta "apps" de <strong>Nextcloud</strong>, junto con el resto de plugins.

Una vez hecho esto, no hace falta ni reiniciar, accedemos con el usuario Administrador a <strong>Aplicaciones</strong>":

<img class="aligncenter size-full wp-image-274" src="http://blogdeandoniaf.files.wordpress.com/2016/12/seleccic3b3n_682.png" alt="" width="276" height="226" />

Y dentro del apartado de "<strong>No habilitado</strong>" encontraremos el plugin para activarlo:

<img class="aligncenter size-full wp-image-275" src="http://blogdeandoniaf.files.wordpress.com/2016/12/seleccic3b3n_683.png" alt="" width="393" height="179" />

Ahora cualquier usuario desde su panel personal puede acceder y <strong>activar</strong> la autenticación de dos factores:

<img src="http://blogdeandoniaf.files.wordpress.com/2016/12/seleccic3b3n_685.png" alt="" width="344" height="304" /><img src="http://blogdeandoniaf.files.wordpress.com/2016/12/seleccic3b3n_684.png" alt="" width="152" height="201" />


Este es el código que debemos escanear con <a href="https://github.com/0xbb/otp-authenticator">OTP Authenticator</a> (Open Source) o <a href="https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2">Google Authenticator  </a>(Propietario) para obtener nuestros códigos de acceso.

A partir de ahora cuando accedamos a nuestra cuenta, nos <strong>solicitara un segundo código</strong>:

<img class="wp-image-280 alignright" src="http://blogdeandoniaf.files.wordpress.com/2017/12/seleccic3b3n_687-e1481197991937.png" width="234" height="295" />
<h1></h1>


En caso de querer <strong>desactivarlo</strong> es tan simple como desmarcar la casilla de "Habilitar TOTP".

&nbsp;

<em>Saludos y que la fuerza os acompañe!</em>
