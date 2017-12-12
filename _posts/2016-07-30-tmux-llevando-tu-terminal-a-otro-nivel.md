---
layout: post
title: tmux - Llevando tu terminal a otro nivel
date: 2016-07-30 13:37
author: Andoni A.
categories: [Software Libre]
tags: [Software Libre]
---
En ocasiones necesitamos trabajar con varias terminales a la vez, redimensionando para encajar todo y tener el máximo de información en pantalla, con cuidado de no cerrar la conexión ssh y cortar a mitad algún proceso... ¿Y por qué? Porque no conocíais (o mejor dicho "conocíamos") <strong>tmux</strong>.

¿Y que es tmux? Es una terminal multiplexora, que aunque suene a batidora traducido al <em>castellano simple</em> significa que es una terminal que permite tener diferentes sesiones donde se ejecutan aplicaciones en una shell. Permitiéndonos dividir la pantalla de manera horizontal o vertical para el uso de estas sesiones.

tmux utiliza un modelo cliente-servidor, el servidor tiene varias sesiones y cada ventana es una entidad independiente que puede ser libremente vinculada a otras sesiones. En cada sesión se podrán visualizar y aceptar la entrada de teclado de varios clientes.

Se puede instalar desde nuestro gestor de paquetes favorito:
<blockquote><code>apt-get install tmux</code></blockquote>
Funciona principalmente a base de comandos y atajos de teclado, pero podemos habilitar acciones con el ratón desde su archivo de configuración, <strong>~/.tmux.conf</strong>, desde este mismo archivo podremos configurar los atajos de teclado a nuestro gusto, este es mio personal actualmente:
```
# Tmux should be pretty, we need 256 color for that
set -g default-terminal "screen-256color"

# Dividir tmux con una combinación de teclas más "visual"
# split panes using | and -
bind | split-window -h
bind - split-window -v

# Movernos de panel con Alt-flecha sin necesidad de usar Ctrl+b
bind -n M-Left select-pane -L
bind -n M-Right select-pane -R
bind -n M-Up select-pane -U
bind -n M-Down select-pane -D

# Activa el cambio de panel con el ratón
set -g mouse-select-pane on

# Configuración del reloj (Se muestra con Ctrl+b,t)
set-window-option -g clock-mode-colour green
set-window-option -g clock-mode-style 24

# Personalización de la barra de estado
set -g status-interval 30
set -g status-justify right
set -g status-left-length 120
set -g status-right-length 140

set -g status-bg default
set -g status-fg white

set-option -g status-right ''
setw -g window-status-format '#[fg=black,bg=brightblack] #I #[fg=brightblack,bg=black] #W '
setw -g window-status-current-format '#[fg=white,nobold,bg=black] #I #[fg=black,bg=green] #W '

set-option -g status-right ''
set-option -g status-left " #[fg=green,bold]#S:#P#[fg=white,nobold]|#[fg=cyan,nobold]%d/%m/%Y#[fg=white]|#[fg=red,bold][#(whoami)@#H]"

# Activa F5 para recargar la configuración de tmux
bind-key -n F5 source-file ~/.tmux.conf; display "reloaded!"

# Aumenta el tiempo que aparecen los mensaje a 2s
set-option -g display-time 2000
```

Como podéis ver es muy personalizable, hay mucha documentación por Internet para dejarlo a vuestro gusto. También encontrareis muchas "<a href="https://tmuxcheatsheet.com/">chuletas</a>" para recordar los atajos hasta que los aprendáis.

A parte de su utilidad a la hora de trabajar con servidores, ya que puedes dejar la sesión de tmux, desconectarte sin cortar los comandos que se están ejecutando, volver más tarde y unirte de nuevo a dicha sesión; me gustaría destacar la capacidad de que puedan trabajar dos personas en una misma ventana.

Como veis en las imágenes, desde ambos dispositivos estaba conectado a la misma sesión, mientras escribía un comando en el ordenador podía ver como se escribía desde el móvil y viceversa.

Las posibilidades con tmux son prácticamente infinitas, pero como siempre eso dependerá de vuestra imaginación y sobretodo de vuestra curiosidad.

&nbsp;

<em>Saludos y que la fuerza os acompañe!</em>

&nbsp;

Referencias:
<a href="https://wiki.archlinux.org/index.php/Tmux_(Espa%C3%B1ol)" target="_blank">Wiki Arch Linux</a>
<a href="https://tmuxcheatsheet.com/">Tmux Cheat Sheet</a>
