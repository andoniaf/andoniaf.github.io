---
layout: post
title: Guacamole - Remote Desktop desde el navegador
date: 2017-01-27 08:37
author: Andoni A.
tags: [guacamole, remote desktop, Selfhosted]
---
Buenas, hoy os voy a explicar mi receta secreta para un buen guacamole, necesitamos: una maquina CentOS, un poco de tiempo, algo de ganas, y por último ir al supermercado a comprar un tarro de Guacamole.

<em>Silencio total... un arbusto pasa rodando... más silencio.</em>

Ahora en serio, si es que no habeis cerrado esta ventana ya, vamos a instalar <strong>Guacamole</strong>, un <strong>Remote Desktop Gateway</strong> con el que poder conectar a todas nuestras máquinas, ya sea por VNC, RDP o SSH; todo desde un mismo sitio, el navegador. Guacamole esta basado en <strong>HTML5</strong> por lo que no necesita ningún tipo de cliente especial y puede usarse incluso desde el móvil o la tablet.

Vamos con los pasos:
<ol>
 	<li>Instalar dependencias y otros paquetes necesarios:
<pre class="code bash"><span class="kw2">yum install</span> <span class="re5">-y</span> <span class="kw2">wget</span> <span class="kw2">vim</span> pv <span class="kw2">dialog</span> <span class="kw2">gcc</span> cairo-devel libpng-devel uuid-devel freerdp-devel freerdp-plugins pango-devel libssh2-devel libvncserver-devel pulseaudio-libs-devel openssl-devel libvorbis-devel libwebp-devel tomcat gnu-free-mono-fonts</pre>
Es recomendable consultar el <a class="urlextern" title="http://guacamole.incubator.apache.org/doc/gug/installing-guacamole.html" href="http://guacamole.incubator.apache.org/doc/gug/installing-guacamole.html" rel="nofollow">manual</a> donde se indica la función de cada dependencia, ya que es posible que alguna no nos interese y podamos obviarla.</li>
 	<li>Descargar el código de Guacamole Server desde su <a class="urlextern" title="http://guacamole.incubator.apache.org/releases/" href="http://guacamole.incubator.apache.org/releases/" rel="nofollow">web</a> o desde <a class="urlextern" title="http://github.com/apache/incubator-guacamole-server" href="http://github.com/apache/incubator-guacamole-server" rel="nofollow">Github.
</a>
Una vez descargado lo descomprimimos:
<pre class="code bash"><span class="kw2">tar</span> <span class="re5">-xzf</span> guacamole-server-0.9.10-incubating.tar.gz
<span class="kw3">cd</span> guacamole-server-0.9.10-incubating<span class="sy0">/

</span></pre>
</li>
 	<li>Compilamos e instalamos:
<pre class="code bash">.<span class="sy0">/</span>configure <span class="re5">--with-init-dir</span>=<span class="sy0">/</span>etc<span class="sy0">/</span>init.d
<span class="kw2">make</span>            <span class="co0"># to compile guacamole-server</span>
<span class="kw2">make</span> <span class="kw2">install</span>    <span class="co0"># to install the components that were built</span>
ldconfig        <span class="co0"># to update your system's cache of installed libraries</span></pre>
</li>
 	<li>Ahora descargamos el Guacamole client, podemos construirlo nosotros mismos o descargarnos el archivo ya preparado desde su <a class="urlextern" title="http://guacamole.incubator.apache.org/releases/" href="http://guacamole.incubator.apache.org/releases/" rel="nofollow">web</a>.Una vez descargado/creado el archivo .war lo desplegamos en el tomcat:
<pre class="code bash"><span class="kw2">cp</span> guacamole<span class="sy0">/</span>target<span class="sy0">/</span>guacamole-0.9.10-incubating.war <span class="sy0">/</span>var<span class="sy0">/</span>lib<span class="sy0">/</span>tomcat<span class="sy0">/</span>webapps<span class="sy0">/</span>guacamole.war

</pre>
</li>
 	<li>Configurar la base de datos. En este punto Guacamole esta instalado, pero hasta que no este terminado de configurar no podremos conectarnos a el.
<div class="li">

Instalamos la BBDD y preparamos los archivos necesarios para que Guacamole funcione con autenticación desde BBDD:
<pre class="code bash"><span class="kw2">yum</span> <span class="re5">-y</span> <span class="kw2">install</span> mariadb mariadb-server
<span class="kw2">mkdir</span> <span class="re5">-p</span> ~<span class="sy0">/</span>guacamole<span class="sy0">/</span>sqlauth <span class="sy0">&amp;&amp;</span> <span class="kw3">cd</span> ~<span class="sy0">/</span>guacamole<span class="sy0">/</span>sqlauth
<span class="kw2">wget</span> https:<span class="sy0">//</span>sourceforge.net<span class="sy0">/</span>projects<span class="sy0">/</span>guacamole<span class="sy0">/</span>files<span class="sy0">/</span>current<span class="sy0">/</span>extensions<span class="sy0">/</span>guacamole-auth-jdbc-0.9.10-incubating.tar.gz
<span class="kw2">tar</span> <span class="re5">-xzf</span> guacamole-auth-jdbc-0.9.10-incubating.tar.gz
<span class="kw2">wget</span> http:<span class="sy0">//</span>dev.mysql.com<span class="sy0">/</span>get<span class="sy0">/</span>Downloads<span class="sy0">/</span>Connector<span class="sy0">/</span>j<span class="sy0">/</span>mysql-connector-java-5.1.38.tar.gz
<span class="kw2">tar</span> <span class="re5">-xzf</span> mysql-connector-java-5.1.38.tar.gz
<span class="kw2">mkdir</span> <span class="re5">-p</span> <span class="sy0">/</span>usr<span class="sy0">/</span>share<span class="sy0">/</span>tomcat<span class="sy0">/</span>.guacamole<span class="sy0">/</span><span class="br0">{</span>extensions,lib<span class="br0">}</span>
<span class="kw2">mv</span> guacamole-auth-jdbc-0.9.10-incubating<span class="sy0">/</span>mysql<span class="sy0">/</span>guacamole-auth-jdbc-mysql-0.9.10-incubating.jar <span class="sy0">/</span>usr<span class="sy0">/</span>share<span class="sy0">/</span>tomcat<span class="sy0">/</span>.guacamole<span class="sy0">/</span>extensions<span class="sy0">/</span>
<span class="kw2">mv</span> mysql-connector-java-5.1.38<span class="sy0">/</span>mysql-connector-java-5.1.38-bin.jar <span class="sy0">/</span>usr<span class="sy0">/</span>share<span class="sy0">/</span>tomcat<span class="sy0">/</span>.guacamole<span class="sy0">/</span>lib<span class="sy0">/</span>
systemctl restart mariadb.service</pre>
</div>
<div class="li">

Creamos la base de datos y al usuario que va a acceder a ella:
<pre class="code bash">mysqladmin <span class="re5">-u</span> root password <span class="re1">$rootDBPass</span>
mysql <span class="re5">-u</span> root <span class="re5">-p</span>   <span class="co0"># Enter password</span></pre>
<pre class="code sql"><span class="kw1">CREATE</span> <span class="kw1">DATABASE</span> guacdb;
<span class="kw1">CREATE</span> <span class="kw1">USER</span> <span class="st0">'guacuser'</span>@<span class="st0">'localhost'</span> <span class="kw1">IDENTIFIED</span> <span class="kw1">BY</span> <span class="st0">'$guacUserDBpass'</span>;
<span class="kw1">GRANT</span> <span class="kw1">SELECT</span><span class="sy0">,</span><span class="kw1">INSERT</span><span class="sy0">,</span><span class="kw1">UPDATE</span><span class="sy0">,</span><span class="kw1">DELETE</span> <span class="kw1">ON</span> guacdb<span class="sy0">.*</span> <span class="kw1">TO</span> <span class="st0">'guacuser'</span>@<span class="st0">'localhost'</span>;
<span class="kw1">FLUSH</span> privileges;
quit</pre>
Extendemos el esquema de la BBDD:
<pre class="code bash"><span class="kw3">cd</span> ~<span class="sy0">/</span>guacamole<span class="sy0">/</span>sqlauth<span class="sy0">/</span>guacamole-auth-jdbc-0.9.10-incubating<span class="sy0">/</span>mysql<span class="sy0">/</span>schema<span class="sy0">/</span>
<span class="kw2">cat</span> .<span class="sy0">/*</span>.sql <span class="sy0">|</span> mysql <span class="re5">-u</span> root <span class="re5">-p</span> guacdb</pre>
</div></li>
 	<li>Creamos los directorios y archivos de configuración para Guacamole:
<pre class="code bash"><span class="kw2">mkdir</span> <span class="re5">-p</span> <span class="sy0">/</span>etc<span class="sy0">/</span>guacamole<span class="sy0">/</span> <span class="sy0">&amp;&amp;</span> <span class="kw2">vim</span> <span class="sy0">/</span>etc<span class="sy0">/</span>guacamole<span class="sy0">/</span>guacamole.properties</pre>
<pre class="code bash"><span class="co0"># MySQL properties</span>
mysql-hostname: localhost
mysql-port: <span class="nu0">3306</span>
mysql-database: guacdb
mysql-username: guacuser
mysql-password: <span class="re1">$guacUserDBpass</span>
 
<span class="co0"># Additional settings</span>
mysql-default-max-connections-per-user: <span class="nu0">0</span>
mysql-default-max-group-connections-per-user: <span class="nu0">0

</span></pre>
Creamos un enlace para que Guacamole pueda encontrar esta configuración:
<pre class="code bash"><span class="kw2">ln</span> <span class="re5">-s</span> <span class="sy0">/</span>etc<span class="sy0">/</span>guacamole<span class="sy0">/</span>guacamole.properties <span class="sy0">/</span>usr<span class="sy0">/</span>share<span class="sy0">/</span>tomcat<span class="sy0">/</span>.guacamole<span class="sy0">/</span></pre>
</li>
 	<li>Abrimos el puerto 8080 puerto en el FW:
<pre class="code bash">firewall-cmd <span class="re5">--add-port</span>=<span class="nu0">8080</span><span class="sy0">/</span>tcp <span class="re5">--permanent</span></pre>
</li>
 	<li>Activamos los servicios para que arranquen en el inicio y reiniciamos para comprobar que todo funciona correctamente:
<pre class="code bash">systemctl <span class="kw3">enable</span> tomcat.service <span class="sy0">&amp;&amp;</span> systemctl <span class="kw3">enable</span> mariadb.service <span class="sy0">&amp;&amp;</span> chkconfig guacd on
systemctl reboot</pre>
</li>
 	<li>Ahora deberíamos poder acceder a "http://IPservidor:8080/guacamole” con las claves por defecto: guacadmin:guacadmin (No olvidéis cambiarlas!!)<img class="size-full wp-image-335 aligncenter" src="http://blogdeandoniaf.files.wordpress.com/2018/01/seleccic3b3n_025.jpg" alt="" width="323" height="362" />La interfaz es muy sencilla y en un momento podemos configurar y probar nuestras conexiones:</li>
</ol>

<img class="size-full wp-image-335 aligncenter" src="https://blogdeandoniaf.files.wordpress.com/2018/01/seleccic3b3n_026.jpg" alt="" width="700" />

<img class="size-full wp-image-335 aligncenter" src="https://blogdeandoniaf.files.wordpress.com/2018/01/seleccic3b3n_028.jpg
" alt="" height="550" />


<em>Saludos y que la fuerza os acompañe!</em>
