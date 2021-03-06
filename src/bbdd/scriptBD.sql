
-- -----------------------------------------------------
-- This script creates the tables and initializate them
-- -----------------------------------------------------

-- -----------------------------------------------------
-- If tables already exists, delete them             
-- -----------------------------------------------------
DROP TABLE IF EXISTS liked;
DROP TABLE IF EXISTS favorito;
DROP TABLE IF EXISTS medicion;
DROP TABLE IF EXISTS sensor;
DROP TABLE IF EXISTS usuario;

-- -----------------------------------------------------
-- Table "ssw"."usuario"
-- -----------------------------------------------------
CREATE TABLE usuario(
  nickname VARCHAR(20) NOT NULL,
  email VARCHAR(45),
  password VARCHAR(20) NOT NULL,
  nombre VARCHAR(10),
  apellido1 VARCHAR(20),
  apellido2 VARCHAR(20),
  direccion VARCHAR(100),
  nacimiento DATE,
  empresa VARCHAR(30),
  telefono INTEGER,
  PRIMARY KEY (nickname));
  
-- -----------------------------------------------------
-- Table "ssw"."sensor"
-- -----------------------------------------------------
CREATE TABLE sensor (
  id INTEGER NOT NULL AUTO_INCREMENT,
  nickname VARCHAR(20) NOT NULL,
  nombre VARCHAR(10) NOT NULL,
  descripcion VARCHAR(255),
  tipo INTEGER NOT NULL,
  visible BOOLEAN NOT NULL,
  x DOUBLE PRECISION NOT NULL,
  y DOUBLE PRECISION NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (nickname) REFERENCES usuario(nickname) ON DELETE CASCADE);

-- -----------------------------------------------------
-- Table "ssw"."favorito"
-- -----------------------------------------------------
CREATE TABLE favorito (
  nickname VARCHAR(20),
  id INTEGER NOT NULL,
  PRIMARY KEY (nickname, id),
  FOREIGN KEY (nickname) REFERENCES usuario(nickname) ON DELETE CASCADE,
  FOREIGN KEY (id) REFERENCES sensor(id) ON DELETE CASCADE);

-- -----------------------------------------------------
-- Table "ssw"."liked"
-- -----------------------------------------------------
CREATE TABLE liked (
  nickname VARCHAR(20),
  id INTEGER NOT NULL,
  PRIMARY KEY (nickname, id),
  FOREIGN KEY (nickname) REFERENCES usuario(nickname) ON DELETE CASCADE,
  FOREIGN KEY (id) REFERENCES sensor(id) ON DELETE CASCADE);

-- -----------------------------------------------------
-- Table "ssw"."medicion"
-- -----------------------------------------------------
CREATE TABLE medicion (
  id INTEGER NOT NULL AUTO_INCREMENT,
  fechaSubida DATETIME,
  fechaMedicion VARCHAR(30),
  valor DOUBLE PRECISION,
  PRIMARY KEY (fechaSubida),
  FOREIGN KEY (id) REFERENCES sensor(id) ON DELETE CASCADE);


-- ----------------------------------------------------
-- BBDD inizialiation
-- ----------------------------------------------------
-- ----------------------------------------------------
-- Values for some users
-- ----------------------------------------------------
insert into usuario values (
    'sergio',
    'sergio.esteban@alumnos.uva.es',
    'sergio',
    'Sergio',
    'Esteban',
    'Pellejero',
    'Valladolid - Parquesol',
    str_to_date('23-02-2018', '%d-%m-%Y'), 
    'UVa',
    365412879);

insert into usuario values (
    'pablo',
    'pablo.renero@alumnos.uva.es',
    'pablo',
    'Pablo',
    'Renero',
    'Balganon',
    'Valladolid - Parquesol',
    str_to_date('24-02-2018', '%d-%m-%Y'), 
    'UVa',
    965874123);

insert into usuario values (
    'alvaro',
    'alvaro.berruezo@alumnos.uva.es',
    'alvaro',
    'Alvaro',
    'Berruezo',
    'Franco',
    'Valladolid - Centro',
    str_to_date('25-02-2018', '%d-%m-%Y'), 
    'UVa',
    548632158);

insert into usuario values (
    'alejandro',
    'alejandro.martinez@alumnos.uva.es',
    'alejandro',
    'Alejandro',
    'Martinez',
    'Andres',
    'Valladolid - Parquesol',
    str_to_date('26-02-2018', '%d-%m-%Y'), 
    'UVa',
    231254687);

-- ----------------------------------------------------
-- Values for some sensors
-- ----------------------------------------------------
insert into sensor values (1, 
    'sergio',
    'HFC05', 
    'sensor humedad',
    2,
    true,
    40.0,
    -1.0);

insert into sensor values (2, 
    'sergio',
    'HFC05', 
    'sensor humedad',
    2,
    true,
    40.417,
    -3.703);

insert into sensor values (3, 
    'alejandro',
    'JUI87', 
    'sensor iluminación',
    3,
    true,
    43.36,
    -8.41);

insert into sensor values (4, 
    'alvaro',
    'AFJ56', 
    'sensor contaminación',
    4,
    true,
    36.15,
    47.26);


-- ----------------------------------------------------
-- Values for some meditions
-- ----------------------------------------------------
insert into medicion values (1,
    Date_format(now(), '%Y-%m-%d %h:%i:%s'),
    '25-89-2035',
    20.11); 

insert into medicion values (1,
    Date_format(now()+1, '%Y-%m-%d %h:%i:%s'),
    '25-89-2035',
    20.12); 

insert into medicion values (1,
    Date_format(now()+2, '%Y-%m-%d %h:%i:%s'),
    '25-89-2035',
    20.13); 

insert into medicion values (1,
    Date_format(now()+3, '%Y-%m-%d %h:%i:%s'),
    '25-89-2035',
    20.14); 

insert into medicion values (1,
    Date_format(now()+4, '%Y-%m-%d %h:%i:%s'),
    '25-89-2035',
    20.15); 

insert into medicion values (1,
    Date_format(now()+5, '%Y-%m-%d %h:%i:%s'),
    '25-89-2035',
    20.16); 

insert into medicion values (1,
    Date_format(now()+6, '%Y-%m-%d %h:%i:%s'),
    '25-89-2035',
    20.17); 

insert into medicion values (1,
    Date_format(now()+7, '%Y-%m-%d %h:%i:%s'),
    '25-89-2035',
    20.18); 

insert into favorito values('pablo',
    3);

insert into favorito values('pablo',
    4);
