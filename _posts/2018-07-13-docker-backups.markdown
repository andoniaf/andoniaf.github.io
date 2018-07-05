---
layout: post
title: "Backup de contenedores Docker"
date: 2018-07-04 13:13:13
author: Andoni A.
categories: Docker
tags: docker backup script
cover: "/assets/docker_header.jpg"
---

Buenas, siguiendo con **Docker**, hoy voy a hablar de como hacer backups de los contenedores. *¿Backup de contenedores?¿Pero no se supone que deberían ser stateless?¿Por qué queremos hacer un backup?* Si, probablemente hacer backups de los contenedores no sea una prioridad por la forma en la que se usan, pero en algunos casos puede sernos útil. (*Por ejemplo, para crear una imagen a partir de otra o para mover el contenedor de máquina.*)

Lo que sí considero más interesante es hacer backups de los volúmenes montados en un contenedor, porque en muchos casos usaremos esos volúmenes para mantener la persistencia de dichos datos, ¿y si son persistentes es porque nos importa mantenerlos no?

Pero primero empecemos por como hacer el backup de un contenedor, recordemos que un **contenedor** al final es una **instancia en ejecución** de una **imagen**.

Con el comando [`docker commit`](https://docs.docker.com/engine/reference/commandline/commit/#extended-description) creamos una nueva imagen a partir de un contenedor. Hay que tener en cuenta que **no se incluyen los datos que estén en los volúmenes** montados (más adelante veremos como hacer backup de estos datos):

```
% docker ps                                                                                                                                           
CONTAINER ID        IMAGE                             COMMAND             CREATED             STATUS              PORTS      NAMES
fbaa87dc95ef        andoniaf/pyemtbot-docker:latest   "python ./bot.py"   8 seconds ago       Up 3 seconds                   cranky_shtern

% docker commit fbaa87dc95ef pyemtbot-docker:nuevotag                                                                                                 
sha256:95fc2296e8ae9cea618f53a1703ef3aad0a30d75dc771ed5029752d27b7e7fc3

% docker images | grep pyemt
pyemtbot-docker                nuevotag            95fc2296e8ae        12 seconds ago      1.18GB
andoniaf/pyemtbot-docker       latest              d662f5182109        2 weeks ago         1.18GB
```

Ahora podríamos crear nuevos contenedores a partir de esta imagen o simplemente utilizar este comando a modo de "snapshot".

Esta imagen podemos exportarla a un fichero con el comando [`docker save`](https://docs.docker.com/engine/reference/commandline/save/#extended-description), o bien para guardarla como respaldo en otra ubicación o para importarla en otra máquina:

```
% docker save --output /tmp/pyemtbot_backup20180704.tar pyemtbot-docker:nuevotag                        

% ls -lh /tmp/pyemtbot_backup20180704.tar       
-rw------- 1 aalonsof aalonsof 1,2G jul  4 19:02 /tmp/pyemtbot_backup20180704.tar
```

También podríamos exportar directamente un contenedor a un fichero con [`docker export`](https://docs.docker.com/engine/reference/commandline/export/).

Ambos comandos generan un tarball, la diferencia es que `docker save` mantiene todas las capas y tags mientras que `docker export` no mantiene ningún tipo de "histórico", *aplanando* (flattening) la imagen como se suele decir.

Después podemos cargar la imagen con [`docker load`](https://docs.docker.com/engine/reference/commandline/load) (o con [`docker import`](https://docs.docker.com/engine/reference/commandline/import) si hemos usado `docker export`):
```
% docker rmi pyemtbot-docker:nuevotag                                                                                                                 !5310
Untagged: pyemtbot-docker:nuevotag
Deleted: sha256:95fc2296e8ae9cea618f53a1703ef3aad0a30d75dc771ed5029752d27b7e7fc3
Deleted: sha256:1204c7af28f3e4958612a0fd14d6cc5197b699519344fa7ab47f4fe4767498cb

% docker images | grep nuevotag               

% docker load < /tmp/pyemtbot_backup20180704.tar                                                                                                      !5312
34a54e8343e4: Loading layer [==================================================>]   5.12kB/5.12kB
Loaded image: pyemtbot-docker:nuevotag

% docker images | grep nuevotag                                                                                                          
pyemtbot-docker                nuevotag            95fc2296e8ae        22 minutes ago      1.18GB
```

Con estos comandos ya podemos realizar backups o mover de máquina nuestros contenedores, pero... ¡aun faltan los datos de los volúmenes!

La [documentación de Docker nos sugiere una solución](https://docs.docker.com/storage/volumes/#backup-a-container) para hacer estos backups que a mi parecer es demasiado manual. Como fan de lo automático quería algo que simplemente indicándole el nombre del contenedor hiciera un backup de todos sus volúmenes montados, pero también con la opción de hacer solo el backup de algunos.

Para esto preparé [containerBck.sh](https://github.com/andoniaf/containersBck) <i class="fa fa-github"></i>. En el README ya esta explicado como usar el script por lo que unicamente voy a explicar un poco como gestiona el backup de los volúmenes.

Si le indicamos la ruta de uno o varios volúmenes, fácil, simplemente crea un tar.gz de esos directorios. Por otro lado, si le indicamos que haga un backup de todos los volúmenes del contenedor, los busca primero usando el comando [`docker inspect`](https://docs.docker.com/engine/reference/commandline/inspect/) y luego crea un tar.gz por cada uno de ellos:

<a href="/assets/images/2018/07/docker_bck01.jpg" data-lightbox="falcon9-large" data-title="Ejemplo docker inspect">
  <img src="/assets/images/2018/07/docker_bck01.jpg" title="Ejemplo docker inspect"  witdh="736" >

El script incluye un periodo de retención ajustable que se encarga de eliminar los backups de los volúmenes e imágenes que queden fuera de ese rango.

Cualquier sugerencia o mejora del script se agradece <i class="fa fa-smile-o"></i>, animaros a hacer algún <i class="fa fa-hand-o-right"></i> [PullRequest](https://github.com/andoniaf/containersBck/pulls) .


*~ Saludos y que la fuerza os acompañe!* <i class="fa fa-ra"></i>

----
