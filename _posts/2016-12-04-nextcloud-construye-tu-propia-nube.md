---
layout: post
title: Nextcloud - Construye tu propia nube
date: 2016-12-04 13:37
author: Andoni A.
categories: [Software Libre]
tags: [cloud, linux, nextcloud, selfhosted]
---
Una de las principales razones por las que decidí comprarme mi propio servidor fue para poder montar mi propio Dropbox, porque "<em>la Nube no es más que el ordenador de <img class="wp-image-230 alignright" src="http://blogdeandoniaf.files.wordpress.com/2017/11/no-cloud.png" alt="There is no cloud" width="160" height="129" />otra persona</em>", y prefiero que esa persona, sea yo.

Como sistema operativo me he decantado por CentOS 7 Minimal porque quería una distribución que viniese solo con lo necesario y ademas quería probar algo de "<em>la familia Red Hat</em>".

Dicho esto os dejo con los pasos a seguir:
<div class="level1">

<strong>1. Lo primero actualizar el sistema e instalar un par de herramientas básicas:</strong>
<pre class="code">sudo yum -y update &amp;&amp; yum -y upgrade
sudo yum install wget net-tools vim</pre>
<strong>2. Después instalaremos PHP:</strong>
<pre class="code">sudo yum install -y httpd php php-mysql sqlite php-dom php-mbstring php-gd php-pdo php-json php-xml php-zip php-gd curl php-curl php55-php-mysqlnd php55 php55-php php55-php-gd php55-php-mbstring php-mcrypt php-pear wget bizp2</pre>
</div>
<strong>3. Copiamos los módulos de PHP 5.5 en la carpeta de Apache y reiniciamos:</strong>
<div class="level1">
<pre class="code">cp /opt/rh/httpd24/root/etc/httpd/conf.d/php55-php.conf /etc/httpd/conf.d/
cp /opt/rh/httpd24/root/etc/httpd/conf.modules.d/10-php55-php.conf /etc/httpd/conf.modules.d/
cp /opt/rh/httpd24/root/etc/httpd/modules/libphp55-php5.so /etc/httpd/modules/

service httpd restart</pre>
<strong>4. Como BBDD vamos a usar MariaDB:</strong>
<pre class="code">sudo yum install mariadb mariadb-server -y</pre>
<strong>5. Iniciamos el servicio de MariaDB y lo añadimos al arranque:</strong>
<pre class="code">sudo systemctl start mariadb.service
sudo systemctl enable mariadb.service</pre>
<strong>6. Mejoramos la seguridad de la instalación de MariaDB:</strong>
<pre class="code">sudo /usr/bin/mysql_secure_installation
 
Enter current password for root (enter for none): Enter
Set root password? [Y/n]: Y
New password: &lt;your-password&gt;
Re-enter new password: &lt;your-password&gt;
Remove anonymous users? [Y/n]: Y
Disallow root login remotely? [Y/n]: Y
Remove test database and access to it? [Y/n]: Y
Reload privilege tables now? [Y/n]: Y</pre>
<strong>7. Creamos la base de datos para NextCloud:</strong>
<pre class="code">mysql -u root -p</pre>
<strong>Una vez dentro ejecutamos:</strong>
<pre class="code">CREATE DATABASE nextcloud;   
CREATE USER 'nextclouduser'@'localhost' IDENTIFIED BY 'yourpassword';   
GRANT ALL PRIVILEGES ON nextcloud.* TO 'nextclouduser'@'localhost' IDENTIFIED BY 'yourpassword' WITH GRANT OPTION;   
FLUSH PRIVILEGES;   
EXIT;</pre>
<strong>8. Ahora debemos buscar la ultima versión de Nextcloud y descargarla:</strong>
<pre class="code">cd /tmp   
wget https://download.nextcloud.com/server/releases/nextcloud-10.0.0.zip   
unzip nextcloud-10.0.0.zip   
sudo mv nextcloud /var/www/html/
sudo chown -R apache:apache /var/www/html/nextcloud/</pre>
<strong>9. Permitimos el acceso a Nextcloud en el firewall:
</strong>
<pre class="code">sudo firewall-cmd --permanent --zone=public --add-service=http   
sudo firewall-cmd --permanent --zone=public --add-service=https   
sudo firewall-cmd --reload</pre>
<strong>10. Configurar SELinux:</strong>

Si tenemos SELinux activo puede darnos problemas con los permisos. Pero obviamente desactivarlo no es una buena opción.

Usando los siguientes comandos deberíamos evitar cualquier problema a la hora de escribir en los archivos de Nextcloud:
<pre class="code">semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/html/nextcloud/data'

semanage fcontext -a -t httpd_sys_rw_content_t    '/var/www/html/nextcloud/config'  

semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/html/nextcloud/apps'   

</pre>
<strong>11. Ahora tenemos Nextcloud descargado, pero falta instalarlo:</strong>

Estos son los datos que puede variar a la hora de ejecutar la instalación:
<ul>
 	<li class="level1">
<div class="li">database-name: <em>nextcloud</em></div></li>
 	<li class="level1">
<div class="li">database-user: <em>nextclouduser</em></div></li>
 	<li class="level1">
<div class="li">database-pass: <em>yourpassword</em></div></li>
 	<li class="level1">
<div class="li">admin-user: <em>admin</em></div></li>
 	<li class="level1">
<div class="li">admin-pass <em>nextcloudadminpassword</em></div></li>
</ul>
<pre class="code">cd /var/www/html/nextcloud
sudo -u apache php occ maintenance:install --database "mysql" --database-name "nextcloud"  --database-user "nextclouduser" --database-pass "yourpassword" --admin-user "admin" --admin-pass "nextcloudadminpassword"</pre>
Si se instala correctamente aparecerá el siguiente mensaje:
<pre class="code">Nextcloud is not installed - only a limited number of commands are available
ownCloud was successfully installed</pre>
<strong>12. Debemos añadir la IP del servidor (p.e. 80.7.113.11) y el nombre de dominio (p.e. <a class="urlextern" title="http://www.example.com" href="http://www.example.com" rel="nofollow">example.com</a>) en la lista de confianza de NextCloud:</strong>
<pre class="code">sudo vi /var/www/html/config/config.php

0 =&gt; 'localhost',
1 =&gt; '80.7.113.11', # Añadimos estas lineas.
2 =&gt; 'example.com',</pre>
<strong>13. Por seguridad, podemos ejecutar este script que establecerá los permisos correctamente en las carpetas de Nextcloud:</strong>
<pre class="code">#!/bin/bash
ocpath='/var/www/html/nextcloud'
htuser='apache'
htgroup='apache'
rootuser='root'

printf "Creating possible missing Directoriesn"
mkdir -p $ocpath/data
mkdir -p $ocpath/assets
mkdir -p $ocpath/updater

printf "chmod Files and Directoriesn"
find ${ocpath}/ -type f -print0 | xargs -0 chmod 0640
find ${ocpath}/ -type d -print0 | xargs -0 chmod 0750

printf "chown Directoriesn"
chown -R ${rootuser}:${htgroup} ${ocpath}/
chown -R ${htuser}:${htgroup} ${ocpath}/apps/
chown -R ${htuser}:${htgroup} ${ocpath}/assets/
chown -R ${htuser}:${htgroup} ${ocpath}/config/
chown -R ${htuser}:${htgroup} ${ocpath}/data/
chown -R ${htuser}:${htgroup} ${ocpath}/themes/
chown -R ${htuser}:${htgroup} ${ocpath}/updater/

chmod +x ${ocpath}/occ

printf "chmod/chown .htaccessn"
if [ -f ${ocpath}/.htaccess ]
 then
  chmod 0644 ${ocpath}/.htaccess
  chown ${rootuser}:${htgroup} ${ocpath}/.htaccess
fi
if [ -f ${ocpath}/data/.htaccess ]
 then
  chmod 0644 ${ocpath}/data/.htaccess
  chown ${rootuser}:${htgroup} ${ocpath}/data/.htaccess
fi</pre>
Si se necesitasemos actualizar Nexcloud en un futuro se podemos:
<pre class="code">#!/bin/bash
# Sets permissions of the Nextcloud instance for updating

ocpath='/var/www/html/nextcloud'
htuser='apache'
htgroup='apache'

chown -R ${htuser}:${htgroup} ${ocpath}</pre>
Y después volver a utilizar el script anterior.

<strong>15. Reiniciamos Apache para que cargue con todos lo cambios:
</strong>
<pre class="code">sudo systemctl restart httpd.service</pre>
<strong>16. Y probamos a acceder a <a class="urlextern" title="http://80.7.113.11" href="http://80.7.113.11" rel="nofollow">http://80.7.113.11</a>
</strong>

</div>
Dentro de la interfaz de Nexcloud encontrareis muchas opciones de configuración. Podéis consultar la documentación acerca de Nextcloud en su <a href="https://docs.nextcloud.com/">web</a>

Aquí os dejo la ventana de login del mio:

![Login Nube 13]({{ "/assets/images/2016/nextcloud_01.png" | absolute_url }})

Como siempre, espero que os sea útil y que os animéis a construir vuestra propia <em>nube</em>.

<em>Saludos y que la fuerza os acompañe!</em>
