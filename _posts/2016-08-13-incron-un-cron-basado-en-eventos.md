---
layout: post
title: Incron - Un cron basado en eventos
date: 2016-08-13 13:37
author: Andoni A.
categories: Linux
---
Para el proyecto final del ciclo necesitaba automatizar la ejecución de un script cada vez que se modificase un archivo de configuración en concreto. Consultando con mi tutor me recomendó <strong>Incron</strong>, un cron guiado por eventos <a href="http://inotify.aiken.cz/?section=inotify&amp;page=about&amp;lang=en">inotify.</a>

Incron, que viene de juntar las palabras "inotify" y  "cron", es un demonio que monitoriza lo que ocurre en el sistema de ficheros y ejecuta acciones en respuesta a determinados eventos. Estas acciones están definidas, como en el caso del "cron", por una serie de reglas.

Podemos instalarlo con nuestro gestor de paquetes preferido:
<blockquote><code>sudo apt-get install incron</code></blockquote>
Una vez instalado crearemos el archivo <strong>/etc/incron.allow </strong>para incluir a los usuarios que podrán declarar reglas de incron, si solo queremos que sea <em>root</em> lo incluiremos en dicho archivo.

La sintaxis de la reglas, muy similar a la de cron, es:
<blockquote><code class="plain plain">Directorio_o_fichero   Evento   Acción</code></blockquote>
<ul>
 	<li><strong>Directorio o fichero</strong> que se va a monitorizar.</li>
 	<li><strong>Evento </strong>que activará la acción, los más usados son:
<ul>
 	<li>IN_ACCESS: el fichero ha sido leído.</li>
 	<li>IN_MODIFY: el fichero fue modificado.</li>
 	<li>IN_MOVED_FROM: fichero movido desde el directorio observado.</li>
 	<li>IN_MOVED_TO: fichero movido al directorio observado.</li>
 	<li>IN_OPEN: el fichero fue abierto.</li>
 	<li>IN_CREATE: un fichero/directorio fue creado en el directorio.</li>
 	<li>IN_DELETE: un fichero/directorio fue eliminado en el directorio.</li>
 	<li>ALL_EVENTS: se lanzará en todos los casos.</li>
</ul>
</li>
 	<li><strong>Acción</strong>, es el comando o script que se ejecutará cuando se cumpla el evento. Se pueden usar las siguientes variables:
<ul>
 	<li>$$: signo del dolar.</li>
 	<li>$@: ruta al directorio contenedor</li>
 	<li>$#: fichero o directorio observado sin su ruta</li>
 	<li>$%: evento que provoca la notificación</li>
 	<li>$&amp;: número del evento que se ejecutó</li>
</ul>
</li>
</ul>
Para crear y manipular la reglas usaremos el comando <strong>incrontab</strong>:
<ul>
 	<li><code>incrontab -l</code> : Muestra las reglas que tenemos definidas.</li>
 	<li><code>incrontab -r</code> : Borra la tabla de reglas por completo. (Cuidado, que no pide confirmación.)</li>
 	<li><code>incrontab -d</code> : Recarga la tabla de reglas. Esto será necesario para que los cambios que hagamos en la lista de reglas sean efectivos.</li>
 	<li><code>incrontab -e</code>: Abrirá nuestro editor predeterminado para crear las nueva reglas.</li>
</ul>
&nbsp;

Lo usos que se le pueden dar a esta aplicación dependerán de la imaginación de cada uno: reiniciar un servicio después de una modificación en su configuración, copias de seguridad de una carpeta o archivo importante, monitorización de eventos del sistema, incluso <a href="https://makuro.wordpress.com/2009/10/16/less-and-incron/">autocompiladores</a>...
<blockquote><code>/var/www/html/php/SnortRulez/test.rules IN_MODIFY restart-IDS</code></blockquote>
Esta es la regla usada en mi proyecto, que reiniciaba el sensor del IDS cada vez que se modificaba el archivo de reglas de Snort.

Hay una limitación a tener en cuenta con Incron (y inotify)  y es que no soporta la monitorización de directorios recursivamente, habría que crear una regla separada para cada uno de los subdirectorios.

&nbsp;

Espero que os sea útil y le encontréis un hueco en vuestro sistema.

&nbsp;

<em>Saludos y que la fuerza os acompañe!</em>

&nbsp;

&nbsp;

&nbsp;
