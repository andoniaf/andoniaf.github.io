---
layout: post
title: "AIOps, ¿que es y por que nada más descubrirlo ya no me gusta?"
date: 2020-05-30 13:13:37
author: Andoni A.
categories: Opinion
tags: ml ai review aiops opinion
cover: "/assets/images/2020/gear.jpg"
---

Buenas <i class="fa fa-hand-spock-o" aria-hidden="true"></i>, no había escuchado el término **AIOps** hasta leer este post ["Observability and the misleading promise of AIOps"](https://thenewstack.io/observability-and-the-misleading-promise-of-aiops/) , según el Glosario de Gartner:

> *AIOps (artificial Intelligence For It Operations) combines big data and machine learning to automate IT operations processes, including event correlation, anomaly detection and causality determination.*

Wow, suena bien ¿verdad? Eso es lo primero que he pensado, porque todo lo que tenga como prefijo `AI` o `ML` rezuma  molonidad. Pero bueno, bajándonos del tren del hype, cualquiera que haya tocado lo suficientemente cerca algo de AI sabe que no es tan mágico como parece.

> <i class="fa fa-exclamation-triangle" aria-hidden="true"></i> NOTA <i class="fa fa-exclamation-triangle" aria-hidden="true"></i> Os invito a leer el post original, porque esta entrada es básicamente un resumen/notas personales que he decido adaptar un poco para publicar y en la que voy a estar muy de acuerdo con el autor, Danyel Fisher.

Sobre el papel suena genial la idea de utilizar AI para detectar, incluso prevenir, fallos en nuestros sistemas, pero la AI necesita ser entrenada con datos. Y en estos datos necesitamos diferenciar los "buenos" y los "malos" ejemplos, pero eso no es  tan sencillo con los sistemas actuales, que son demasiado complejos e impredecibles.

¿Y a qué me refiero con impredecibles? Pues como dice en el post, por un lado desplegar una nueva funcionalidad puede hacer que cambie el comportamiento de forma que todo el entrenamiento previo no sea válido y por ejemplo los propios despliegues en sí son anomalías (*y la tendencia actual es a tener despliegues cada vez más frecuentes*).

<a href="/assets/images/2020/sistemas_impredecibles_change_my_mind.png" data-lightbox="falcon9-large" data-title="Change my mind">
  <img src="/assets/images/2020/sistemas_impredecibles_change_my_mind.png" title="Change my mind..."  witdh="820" >
</a>

> *Si alguien me puede rebatir esto estaría encantado de tener el punto de vista contrario, pero me cuesta imaginar como entrenar un modelo para predecir lo que, desde mi punto de vista actual, es impredecible.*

El otro punto "en contra" de AIOps, y que me ha impulsado bastante a publicar estas notas, es que fomenta una de las cosas con las que más en desacuerdo he estado desde que llevo en esto: tener alertas porque sí, muchas alertas, sin tener claro ni de que sirven. **C**iertamente al**G**uno sabe a lo que me **R**efiero.

<a href="/assets/images/2020/rajoy_muchas_alertas.png" data-lightbox="falcon9-large" data-title="Muy muchas alertas">
  <img src="/assets/images/2020/rajoy_muchas_alertas.png" title="" height="200" witdh="220" >
</a>

Cuando tienes un sistema lleno de alertas, y ademas la mayoría ni siquiera son accionables, lo que tienes es mi...ucho ruido, y lo único que te va a causar probablemente es pérdidas de tiempo.

Con **AIOps** fomentamos ese mal hábito, ya se encargará él de filtrar las alertas de verdad, ¿no? Puede que sea mejor idea tener una serie de [SLOs](https://landing.google.com/sre/workbook/chapters/implementing-slos/) que nos informen cuando la experiencia de usuario no está siendo la adecuada y entonces alertar.

> *Sí, esto lo ha escrito un SRE, si no menciono los SLOs por lo menos una vez exploto.*
> <video src="/assets/images/2020/noslonosre.mov" height="300" controls preload></video>

Al final, la única forma de no acabar ahogado entre alarmas es alertar solo lo importante. Claro que quizá, como dice el autor del post, no tengamos forma de relacionar nuestros datos con la experiencia del cliente, pero entonces el problemas es que no tenemos las herramientas adecuadas.

La comparación que usa me parece perfecta, así que la voy a copiar tal cual: Imagina que vas al médico pensando que te has roto un hueso, y el médico te hace un <abbr title="Electroencefalograma">EEG</abbr> y un <abbr title="Electrocardiograma">ECG</abbr> antes que ver como caminas por la consulta. Se pone a leer los resultado y se da cuenta de que cuando apoyas la pierna izquierda tu pulso se acelera, lo cual concuerda con que tengas un hueso de la pierna roto. Pero... ¿no habría sido más sencillo hacer una placa de rayos X?

Coincido, como ya había dicho antes, en que no estamos listos (aún) para mezclar AI con Ops, creo que primero a la mayoría nos falta invertir mucho más en observabilidad y en mejorar la monitorización de nuestros sistemas.

Y ahora llega la parte a la que estaba deseando llegar, ¿y vosotros qué opináis del tema? Me parece un tema interesante y bastante abierto a debate, así que espero vuestras opiniones por [<i class="fa fa-twitter-square fa-lg"></i>](https://twitter.com/andoni013/status/1266760676472733701?s=20) o [<i class="fa fa-linkedin-square fa-lg"></i>](https://www.linkedin.com/posts/andoniaf_el-otro-d%C3%ADa-descubr%C3%AD-que-era-aiops-y-me-activity-6672526392497860608-5oPv)!

*~ Saludos y que la fuerza os acompañe!* <i class="fa fa-ra"></i>

----
