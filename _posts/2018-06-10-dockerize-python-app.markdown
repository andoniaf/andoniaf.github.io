---
layout: post
title: "Dockerizando Python App"
date: 2018-06-10 12:13:14
author: Andoni A.
categories: Docker
tags: docker python bot
cover: "/assets/docker_header.jpg"
---

Buenas, después de una temporada con poco tiempo libre he podido sacar un hueco y me apetecía trastear con **Docker**. Como también tengo abandonado mi bot para [consultar la EMT](https://andoniaf.github.io/linux/2017/10/10/conky-emt.html), he decidido antes de retomarlo *dockerizarlo*.

Por si alguien no lo conoce, Docker es una herramienta permite crear, desplegar y ejecutar aplicaciones sobre "contenedores", [aquí](https://www.docker.com/what-docker) tenéis más info.

Podemos crear nuestra propia imagen de Docker mediante un **Dockerfile**. Yo voy a crear una imagen que ejecute mi telegram-bot de consulta para la EMT.

Para empezar tengo el código del bot en un directorio `/pyEMTbot-docker`:
```
~/git/pyEMTbot-docker> ls
bot.py  logs  modules  requirements.txt  settings.py  settings-template.py
```

Dentro de ese mismo directorio, creamos el `Dockerfile`:
```
FROM python:3

RUN mkdir /pyemtbot

WORKDIR /pyemtbot

COPY requirements.txt /pyemtbot

RUN pip install -r requirements.txt

COPY . /pyemtbot

CMD [ "python", "./bot.py" ]
```

Cada instrucción crea una "capa", así que como dijo [Jack](https://es.wikipedia.org/wiki/Jack_el_Destripador), vamos por partes.:

  - Esta primera linea establece la "capa base" de nuestra imagen:
```
FROM python:3
```
  En este caso es una imagen básica con Python 3.


  - `RUN` ejecuta la orden dentro de la imagen:
```
RUN mkdir /pyemtbot
WORKDIR /pyemtbot
```
  Creando por tanto el directorio `/pyemtbot` que marcamos como "directorio de trabajo" con `WORKDIR`.

  Esto nos ahorra tener que estar cambiando de directorio o escribiendo rutas absolutas como `RUN cd /to/path && do-X`.

  - Con `COPY` copiamos contenido del host a la imagen:
```
COPY requirements.txt /pyemtbot
```

  - Como la aplicación tiene varias dependencias las instalamos:
```
RUN pip install -r requirements.txt
```

  - Y por último, copiamos el resto del código a la imagen y añadimos el comando que se lanzará cuando arranquemos el contenedor:
```
COPY . /pyemtbot
CMD [ "python", "./bot.py" ]
```

  *¿Por qué no hemos copiado todo el contenido y luego instalado las dependencias?¿No nos ahorramos así un paso?*

  Como he mencionado antes, cada instrucción crea una capa en la imagen. A la hora de construir la imagen, estas capas se guardan en caché, por lo que si solo modificamos las últimas capas, no será necesario "regenerar" las anteriores.

  En este caso, primero se instalan las dependencias, ya que si solo cambiamos el código, solo tendrán que generarse las últimas dos capas.

  En este ejemplo se puede ver como nos indica que esta usando el caché:
```
/pyEMTbot-docker> docker build -t pyemtbot .
Sending build context to Docker daemon  20.99kB
Step 1/7 : FROM python:3
 ---> a5b7afcfdcc8
Step 2/7 : RUN mkdir /pyemtbot
 ---> Using cache
 ---> ad4b8ae9ad94
Step 3/7 : WORKDIR /pyemtbot
 ---> Using cache
 ---> d11177ff034e
Step 4/7 : COPY requirements.txt /pyemtbot
 ---> Using cache
 ---> 089d916a911a
Step 5/7 : RUN pip install -r requirements.txt
 ---> Using cache
 ---> e6937249c745
Step 6/7 : COPY . /pyemtbot
 ---> a644b39a83a3
Step 7/7 : CMD [ "python", "./bot.py" ]
 ---> Running in 2e69f9bdf693
Removing intermediate container 2e69f9bdf693
 ---> 4bba79e10fd2
Successfully built 4bba79e10fd2
Successfully tagged pyemtbot:latest
```

Como se ve en el ejemplo, una vez preparado el `Dockerfile`, ejecutamos `docker build -t <nombreDeLaImagen> .` para crear la imagen.

Una vez creada podemos usarla como cualquier otra:
```
/pyEMTbot-docker> docker run -d --name pyemtbot pyemtbot:latest
58e4b7386c5811b7c6ee1fca7f95712c002c2619730db6123ad645f6d1a4ba89
/pyEMTbot-docker> docker ps |grep emt
58e4b7386c58        pyemtbot:latest         "python ./bot.py"        9 seconds ago       Up 7 seconds                                                                                     pyemtbot
/pyEMTbot-docker> docker exec  pyemtbot tail /pyemtbot/logs/bot.log
[2018-06-10 10:30]: Andoni: /start
[2018-06-10 10:30]: Andoni: /uptime
[2018-06-10 10:30]: Andoni: /emt 636
```

<a href="/assets/images/2018/06/pyemtbot_tg_example.jpg" data-lightbox="falcon9-large" data-title="Ejemplo Telegram">
  <img src="/assets/images/2018/06/pyemtbot_tg_example.jpg" title="Ejemplo Telegram"  height="450" >
</a>

Espero poder ir sacando hueco para trastear más con Docker y escribir alguna cosilla más.







*~ Saludos y que la fuerza os acompañe!*
