# SSW
Práctica SSW para el curso 2017/2018

## Requisitos
Python3: en sistemas ubuntu se puede instalar así.
```bash
$ sudo apt install python3
```

MySQL: en sistemas ubuntu se puede instalar así.
```bash
$ sudo apt install mysql-client mysql-server
```

Virtualenv: en sistemas ubuntu se puede instalar así.
```bash
$ sudo apt install virtualenv
```

## Creación de la base de datos
Para crear la base de datos e inicializarla ejecutar los siguientes
comandos. Posterior mente el nombre que decida para su tabal deberá se añadido al archivo config.conf.
```bash
$ mysql -u root -p
mysql > create database database-name ;
mysql > exit;
$ mysql -u root -p ssw < bbdd/scritBD . sql

```

## Instalación de las dependencias de flask y primer arranque
Una vez que hemos descargado los anteriores programas tenemos que ejecutar el fichero install.sh de
nuestra práctica, es necesario darle permisos de ejcución si no los tiene. Comando:
```
$ cd src/
$ ./install.sh
```
En el caso de que no exista nos crea un entorno virtual en la carpeta en la que estamos ejecutando el
fichero install.sh, después inicializa dicho entorno virtual e instala en él todo lo necesario para que nuestra
práctica funcione. Las dependencias y programas se encuentran en un fichero llamado requirments.txt.

**Antes de arrancar** por primera vez nuestro proyecto tenemos que añadir los datos sobre la configuración de la base de datos en el archivo config.conf.

Para arrancar el sistema simplemente tenemos que ejecutar el fichero run.sh, que nos ejecutará el flask,
nos montará el servidor web y se encargará de devolvernos una url y un puerto local en la que mirar nuestra
página web.
