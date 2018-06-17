---
layout: post
title: "Build automatizado de imágenes Docker"
date: 2018-06-17 09:13:13
author: Andoni A.
categories: Docker
tags: docker dockerhub github
cover: "/assets/docker_header.jpg"
---

Buenas, continuando con la [entrada anterior](https://andoniaf.github.io/docker/2018/06/10/dockerize-python-app.html) y con la idea de no perder el ritmo, aunque sea con entradas *rápidas, sencillas y para toda la familia*.

Después de crear una imagen de Docker que desplegase el bot, el siguiente paso era poder compartirla.

[Docker Hub](https://docs.docker.com/docker-hub/) es un registro proporcionado por [Docker Inc](https://www.docker.com/company) donde podemos alojar nuestras imágenes, tanto públicas como privadas.

Uno de los métodos de los que disponemos para subir nuestras imágenes es la configuración de **builds automatizados**. Esto nos permite que cuando hagamos un cambio en el código de nuestro repositorio de Github o Bitbucket se construya automáticamente una nueva imagen de Docker con dichos cambios.  

Para este ejemplo voy a usar un repositorio en [Github](https://github.com/andoniaf/pyEMTbot-docker) <i class="fa fa-github"></i>, lo primero es enlazar nuestra cuenta de Docker Hub con la de Github:

<a href="/assets/images/2018/06/01_linkedAccount.png" data-lightbox="falcon9-large" data-title="Ejemplo automated build">
  <img src="/assets/images/2018/06/01_linkedAccount.png" title="Ejemplo automated build"  width="700" >
</a>

Después, dentro de las opciones de creación, seleccionamos crear *automated build* y marcamos Github:

<a href="/assets/images/2018/06/02_createAutoBuild.png" data-lightbox="falcon9-large" data-title="Ejemplo automated build">
  <img src="/assets/images/2018/06/02_createAutoBuild.png" title="Ejemplo automated build"  height="190" >
</a><a href="/assets/images/2018/06/03_createAutoBuild.png" data-lightbox="falcon9-large" data-title="Ejemplo automated build">
  <img src="/assets/images/2018/06/03_createAutoBuild.png" title="Ejemplo automated build"  height="220" >
</a>

Nos listará los repositorios que tenemos en nuestra cuenta, seleccionamos el que queremos, en mi caso `pyEMTbot-docker` y aparecerá el siguiente formulario:

<a href="/assets/images/2018/06/04_createAutoBuild.png" data-lightbox="falcon9-large" data-title="Ejemplo automated build">
  <img src="/assets/images/2018/06/04_createAutoBuild.png" title="Ejemplo automated build"  width="600" >
</a>

La mayoría de estos datos podemos cambiarlos más tarde, al igual que activar/desactivar la opción de que la build se active con cada push o la nomenclatura de los tags. (*Por ejemplo, yo creé el repo privado inicialmente y lo cambié a público una vez finalizadas las pruebas.*)

<a href="/assets/images/2018/06/05_createAutoBuild.png" data-lightbox="falcon9-large" data-title="Ejemplo automated build">
  <img src="/assets/images/2018/06/05_createAutoBuild.png" title="Ejemplo automated build"  width="600" >
</a>


Cuando creamos la *build automática* nos crea una primera imagen en el repositorio de Docker Hub, podemos ver las diferentes fases por las que pasa la construcción desde "Build Details":


<a href="/assets/images/2018/06/06_createAutoBuild.png" data-lightbox="falcon9-large" data-title="Ejemplo automated build">
  <img src="/assets/images/2018/06/06_createAutoBuild.png" title="Ejemplo automated build"  width="600" >
</a>

<a href="/assets/images/2018/06/07_createAutoBuild.png" data-lightbox="falcon9-large" data-title="Ejemplo automated build">
  <img src="/assets/images/2018/06/07_createAutoBuild.png" title="Ejemplo automated build"  width="600" >
</a>

<a href="/assets/images/2018/06/08_createAutoBuild.png" data-lightbox="falcon9-large" data-title="Ejemplo automated build">
  <img src="/assets/images/2018/06/08_createAutoBuild.png" title="Ejemplo automated build"  width="600" >
</a>

Cuando termina podemos acceder y ver los logs de la construcción:

<a href="/assets/images/2018/06/09_createAutoBuild.png" data-lightbox="falcon9-large" data-title="Ejemplo automated build">
  <img src="/assets/images/2018/06/09_createAutoBuild.png" title="Ejemplo automated build"  width="600" >
</a>
<a href="/assets/images/2018/06/10_createAutoBuild.png" data-lightbox="falcon9-large" data-title="Ejemplo automated build">
  <img src="/assets/images/2018/06/10_createAutoBuild.png" title="Ejemplo automated build"  width="600" >
</a>

Con cada *push* al repositorio se inicia el proceso de construcción automática:

<a href="/assets/images/2018/06/11_createAutoBuild.png" data-lightbox="falcon9-large" data-title="Ejemplo automated build">
  <img src="/assets/images/2018/06/11_createAutoBuild.png" title="Ejemplo automated build"  width="600" >
</a>

Si en algún *push*, "rompemos" la imagen de Docker y no puede construirse nos aparecerá el "Error" en el histórico y podremos analizar en los detalles cual ha sido el fallo y corregirlo.

<a href="/assets/images/2018/06/03_errorBuild.png" data-lightbox="falcon9-large" data-title="Ejemplo automated build">
  <img src="/assets/images/2018/06/03_errorBuild.png" title="Ejemplo automated build"  width="600" >
</a>

<a href="/assets/images/2018/06/02_errorBuild.png" data-lightbox="falcon9-large" data-title="Ejemplo automated build">
  <img src="/assets/images/2018/06/02_errorBuild.png" title="Ejemplo automated build"  width="600" >
</a>

<a href="/assets/images/2018/06/01_errorBuild.png" data-lightbox="falcon9-large" data-title="Ejemplo automated build">
  <img src="/assets/images/2018/06/01_errorBuild.png" title="Ejemplo automated build"  width="600" >
</a>

Una vez corregido el fallo, y la construcción ha finalizado correctamente, la imagen esta disponible para que cualquiera que use Docker pueda buscarla y usarla:
```
$ docker search pyEMT
NAME                       DESCRIPTION                                     STARS               OFFICIAL            AUTOMATED
andoniaf/pyemtbot-docker   Imagen de Docker que contiene un bot de tele…   0                                       [OK]

$ docker run -d -v ${PWD}/settings.py:/pyemtbot/settings.py andoniaf/pyemtbot-docker:latest
e08c755b2ab90c336933b6e6c81913b7177bd320bae42b5a40654373e686698f

$ docker ps
CONTAINER ID        IMAGE                             COMMAND                  CREATED             STATUS              PORTS          NAMES
e08c755b2ab9        andoniaf/pyemtbot-docker:latest   "python ./bot.py"        7 seconds ago       Up 4 seconds                       serene_johnson

```


Espero poder ir sacando más hueco para trastear con Docker y escribir alguna cosilla más.







*~ Saludos y que la fuerza os acompañe!*

----
- [https://docs.docker.com/docker-hub/builds](https://docs.docker.com/docker-hub/builds)
- [https://github.com/andoniaf/pyEMTbot-docker](https://github.com/andoniaf/pyEMTbot-docker)
- [https://hub.docker.com/r/andoniaf/pyemtbot-docker
-docker](https://hub.docker.com/r/andoniaf/pyemtbot-docker
-docker)
