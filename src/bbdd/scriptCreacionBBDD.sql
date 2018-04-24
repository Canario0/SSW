DROP TABLE IF EXISTS LIKED;
DROP TABLE IF EXISTS FAVORITO;
DROP TABLE IF EXISTS MEDICION;
DROP TABLE IF EXISTS SENSOR;
DROP TABLE IF EXISTS USUARIO;
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
  password VARCHAR(10) NOT NULL,
  nombre VARCHAR(10),
  apellidos VARCHAR(20),
  direccion VARCHAR(100),
  nacimiento DATE,
  empresa VARCHAR(30),
  telefono INTEGER,
  PRIMARY KEY (nickname));
  
-- -----------------------------------------------------
-- Table "ssw"."sensor"
-- -----------------------------------------------------
CREATE TABLE sensor (
  id INTEGER NOT NULL,
  nombre VARCHAR(10) NOT NULL,
  descripcion VARCHAR(255),
  tipo INTEGER NOT NULL,
  visible BOOLEAN NOT NULL,
  x DOUBLE PRECISION NOT NULL,
  y DOUBLE PRECISION NOT NULL,
  PRIMARY KEY (id));

-- -----------------------------------------------------
-- Table "ssw"."favorito"
-- -----------------------------------------------------
CREATE TABLE favorito (
  nickname VARCHAR(20),
  id INTEGER NOT NULL,
  PRIMARY KEY (nickname, id),
  FOREIGN KEY (nickname) REFERENCES usuario(nickname),
  FOREIGN KEY (id) REFERENCES sensor(id));

-- -----------------------------------------------------
-- Table "ssw"."favorito"
-- -----------------------------------------------------
CREATE TABLE liked (
  nickname VARCHAR(20),
  id INTEGER NOT NULL,
  PRIMARY KEY (nickname, id),
  FOREIGN KEY (nickname) REFERENCES usuario(nickname),
  FOREIGN KEY (id) REFERENCES sensor(id));

-- -----------------------------------------------------
-- Table "ssw"."medicion"
-- -----------------------------------------------------
CREATE TABLE medicion (
  id INTEGER NOT NULL,
  fechaSubida DATETIME,
  fechaMedicion DATE NOT NULL,
  valor DOUBLE PRECISION,
  PRIMARY KEY (fechaSubida),
  FOREIGN KEY (id) REFERENCES sensor(id));
