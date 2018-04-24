DROP TABLE IF EXISTS SENSOR;
DROP TABLE IF EXISTS LIKED;
DROP TABLE IF EXISTS FAVORITO;
DROP TABLE IF EXISTS MEDICION;
DROP TABLE IF EXISTS USUARIO;

-- -----------------------------------------------------
-- Table "mydb"."USUARIO"
-- -----------------------------------------------------
CREATE TABLE USUARIO(
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
-- Table "mydb"."SENSOR"
-- -----------------------------------------------------
CREATE TABLE SENSOR (
  id INTEGER NOT NULL,
  nombre VARCHAR(10) NOT NULL,
  descripcion VARCHAR(255),
  tipo INTEGER NOT NULL,
  visible BOOLEAN NOT NULL,
  x DOUBLE PRECISION NOT NULL,
  y DOUBLE PRECISION NOT NULL,
  PRIMARY KEY (id));

-- -----------------------------------------------------
-- Table "mydb"."FAVORITO"
-- -----------------------------------------------------
CREATE TABLE FAVORITO (
  nickname VARCHAR(20),
  id INTEGER NOT NULL,
  PRIMARY KEY (nickname, id),
  FOREIGN KEY (nickname) REFERENCES USUARIO(nickname),
  FOREIGN KEY (id) REFERENCES SENSOR(id));

-- -----------------------------------------------------
-- Table "mydb"."FAVORITO"
-- -----------------------------------------------------
CREATE TABLE LIKED (
  nickname VARCHAR(20),
  id INTEGER NOT NULL,
  PRIMARY KEY (nickname, id),
  FOREIGN KEY (nickname) REFERENCES USUARIO(nickname),
  FOREIGN KEY (id) REFERENCES SENSOR(id));

-- -----------------------------------------------------
-- Table "mydb"."MEDICION"
-- -----------------------------------------------------
CREATE TABLE MEDICION (
  id INTEGER NOT NULL,
  fechaSubida DATETIME,
  fechaMedicion DATE NOT NULL,
  valor DOUBLE PRECISION,
  PRIMARY KEY (fechaSubida),
  FOREIGN KEY (id) REFERENCES SENSOR(id));
