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


-- ----------------------------------------------------
-- BBDD inizialiation
-- ----------------------------------------------------
insert into usuario values ('popi', 'pipo@dog.com', 'opipopi', 'Pipo', 'Canino', null, null, str_to_date('24-04-2018', '%d-%m-%Y'), null, null);
insert into usuario values ('El Retrasito', 'el@retrasito.com', 'retrasito1', 'El', 'Retrasito',  null, null, str_to_date('21-09-2017', '%d-%m-%Y'), null, null);
insert into usuario values ('Antimateria', 'sergio.esteban@alumnos.uva.es', '1234567890', 'Sergio', 'Esteban', null,'Calle Ciudad de la Habana 23', str_to_date('01-01-1997', '%d-%m-%Y'), null, 719537216);
insert into usuario values ('Canario', 'pablo.renero@alumnos.uva.es', 'c4n4r10', 'Pablo', 'Renero', null, 'Calle Ciudad de la Habana 24', str_to_date('31-12-1997', '%d-%m-%Y'), null, 689340123);
insert into usuario values ('Smokt', 'alejandro.martinez@alumnos.uva.es', 'contraseña', 'Alejandro', 'Martinez', null, 'Plaza de España 9', str_to_date('01-02-1997', '%d-%m-%Y'), null, 681234517);
insert into usuario values ('0ravla', 'alvaro.berruezo@alumnos.uva.es', '1234', 'Alvaro', 'Berruezo', null, 'Calle Me Falta un Tornillo 21', str_to_date('19-09-1997', '%d-%m-%Y'), null, 684932185);
insert into usuario values ('PeterGriffin', 'peter.griffin@alumnos.uva.es', 'grifffffin', 'Peter', 'Griffin', null, 'Calle Spooner 31', str_to_date('12-08-1975', '%d-%m-%Y'), 'Padre de Familia', 693728612);
insert into usuario values ('HomerJSimpson', 'homer.j@simpson.com', 'homero', 'Homer', 'Simpson', null, 'Evergreen Terrace 742', str_to_date('22-02-1980', '%d-%m-%Y'), 'Los Simpson', 649334821);
insert into usuario values ('JVegas', 'vegas@apple.com', 'aloha', 'J', 'Vegas', null, null, str_to_date('11-02-1973', '%d-%m-%Y'), 'UVa', 983123456);
insert into usuario values ('CVaca', 'cesar@infor.uva.es', 'n00b', 'Cesar', 'Vaca', null, null, str_to_date('01-07-1979', '%d-%m-%Y'), 'UVa', 983123456);
insert into usuario values ('Benja', 'ben@ja.min', 'minjaben', 'Benjamin', 'Sahelices', null, 'Campus Universitario Miguel Delibes', str_to_date('24-06-1971', '%d-%m-%Y'), 'UVa', 983123123);

insert into sensor values (1, "HC05", "sesor de temperatura", 2, true, 236.25, 2547.36);
insert into medicion values (1, Date_format(now(),'%Y-%m-%d %h:%i:%s'), Date_format(now(), '%Y-%m-%d'), 20.15); 
insert into medicion values (1, Date_format(now()+1,'%Y-%m-%d %h:%i:%s'), Date_format(now(), '%Y-%m-%d'), 20.11); 
insert into medicion values (1, Date_format(now()+2,'%Y-%m-%d %h:%i:%s'), Date_format(now(), '%Y-%m-%d'), 20.12); 
insert into medicion values (1, Date_format(now()+3,'%Y-%m-%d %h:%i:%s'), Date_format(now(), '%Y-%m-%d'), 20.13); 
insert into medicion values (1, Date_format(now()+4,'%Y-%m-%d %h:%i:%s'), Date_format(now(), '%Y-%m-%d'), 20.14); 
insert into medicion values (1, Date_format(now()+5,'%Y-%m-%d %h:%i:%s'), Date_format(now(), '%Y-%m-%d'), 20.16); 
insert into medicion values (1, Date_format(now()+6,'%Y-%m-%d %h:%i:%s'), Date_format(now(), '%Y-%m-%d'), 20.17); 
insert into medicion values (1, Date_format(now()+7,'%Y-%m-%d %h:%i:%s'), Date_format(now(), '%Y-%m-%d'), 20.18); 
