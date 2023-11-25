FROM ubuntu:20.10

# Configurar fuentes de paquetes
RUN sed -i 's/archive/old-releases/g' /etc/apt/sources.list \
    && sed -i 's|http://security.ubuntu.com/ubuntu|http://old-releases.ubuntu.com/ubuntu|g' /etc/apt/sources.list

# Actualizar el índice de paquetes e instalar openssh-server y apt-utils
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends openssh-server\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Crear el usuario test y configurar la contraseña
RUN useradd -m -d /home/test -s /bin/bash test \
    && echo 'test:test' | chpasswd

# Crear el directorio para el proceso sshd
RUN mkdir /var/run/sshd

# Exponer el puerto 22
EXPOSE 22

# Iniciar el servicio sshd en modo daemon
CMD ["/usr/sbin/sshd", "-D"]

