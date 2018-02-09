---
layout: post
title: Entendiendo la carga (load) en Linux
date: 2017-03-20 21:02
author: Andoni A.
categories: Linux
tags: linux load
---
La <strong>carga del sistema </strong>mide el consumo de los recursos de un equipo, y por tanto es importante para conocer el rendimiento del mismo.

<img class="aligncenter size-full wp-image-358" src="http://blogdeandoniaf.files.wordpress.com/2018/03/seleccic3b3n_001.png" alt="" width="719" height="45" />

A pesar de ser algo muy simple, mucha gente desconoce como interpretarlo y diferenciar entre valores "buenos" o "malos".

Lo primero que hay que saber es que los valores corresponden a la <strong>carga media</strong> de los <strong>últimos 1, 5 y 15 minutos</strong>.

Lo segundo, es que <strong>no es lo mismo</strong> la carga de un servidor <strong>mononúcleo</strong> que la de uno <strong>multinúcleo</strong> (o multiprocesador), y aquí es donde entra la típica <em>analogía del tráfico</em>.

Cada núcleo equivaldría a un carril, si tenemos el carril vacío la carga sería 0.
<ul>
 	<li>Si tenemos un carril, y esta lleno de coches, la carga es es de 1.00:</li>
</ul>
<img class="aligncenter size-full wp-image-359" src="http://blogdeandoniaf.files.wordpress.com/2018/03/seleccic3b3n_002.png" alt="" width="624" height="99" />
<ul>
 	<li>Si tenemos un carril que va un poco más vacío, la carga (en este ejemplo) sería de 0.60:</li>
</ul>
<img class="aligncenter size-full wp-image-360" src="http://blogdeandoniaf.files.wordpress.com/2018/03/seleccic3b3n_004.png" alt="" width="624" height="99" />
<ul>
 	<li>En cambio si el carril esta lleno, y ademas hay coches esperando, la carga sería de mayor de 1, en este caso de 1.60:</li>
</ul>
<img class="aligncenter size-full wp-image-361" src="http://blogdeandoniaf.files.wordpress.com/2018/03/seleccic3b3n_005.png" alt="" width="738" height="224" />
<ul>
 	<li>Por otro lado, en caso de tener dos carriles (dos núcleos) y estar llenos, la carga sería de 2.00:<img class="aligncenter size-full wp-image-362" src="http://blogdeandoniaf.files.wordpress.com/2018/03/seleccic3b3n_003.png" alt="" width="626" height="190" /></li>
</ul>
Como he mencionado es importante, ya que no es lo mismo tener 2.00 de carga en un equipo mononúcleo que en un multinúcleo, el primero estaría doblando su capacidad mientras que el segundo puede estar funcionando sin problemas.

¿Y como se cuantos núcleos tiene mi equipo? Fácil, sacando esa información de /proc/cpuinfo:

<code>grep 'model name' /proc/cpuinfo | wc -l</code>

También hay que tener en cuenta en cual de los tres números de la carga nos fijamos. Lo recomendable es fijarse en el último, el de los <strong>15 minutos</strong>, porque es normal ver picos de carga en los dos primeros.

Para terminar añadir que ademas de con el comando '<strong>uptime</strong>' podemos conocer la carga del sistema usando '<strong>top</strong>,' '<strong>htop</strong>', '<strong>w</strong>' o directamente consultando el archivo <strong>/proc/loadavg</strong>

<em>Saludos y que la fuerza os acompañe!</em>
