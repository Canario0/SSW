
-- -----------------------------------------------------
-- Table "mydb"."USUARIO"
-- -----------------------------------------------------
CREATE TABLE "USUARIO" (
  "nickname" VARCHAR(50) NOT NULL,
  "email" VARCHAR(45 ),
  "password" VARCHAR(45 ),
  "nombre" VARCHAR(45 ),
  "apellidos" VARCHAR(45 ),
  "direccion" VARCHAR(100 ),
  "fechaNacimiento" DATE,
  "empresa" VARCHAR(45 ),
  "telefono" INTEGER,
  "sensorFav" INTEGER NOT NULL,
  "sensorLike" INTEGER NOT NULL,
  PRIMARY KEY ("nickname"));
  
-- -----------------------------------------------------
-- Table "mydb"."SENSOR"
-- -----------------------------------------------------
CREATE TABLE "SENSOR" (
  "id" INTEGER NOT NULL,
  "nicknameUser" VARCHAR(50 ),
  "nombre" VARCHAR(45 ),
  "descripcion" VARCHAR(500 ),
  "tipo" VARCHAR(45 ),
  "visible" VARCHAR(45 ),
  "latitud" VARCHAR(45 ),
  "longitud" VARCHAR(45 ),
  "numeroLikes" INTEGER,
  PRIMARY KEY ("id"),
  FOREIGN KEY ("nicknameUser")
  REFERENCES "USUARIO" ("nickname"));

-- -----------------------------------------------------
-- Table "mydb"."MEDICION"
-- -----------------------------------------------------
CREATE TABLE "MEDICION" (
  "fechaSubida" DATE,
  "fechaMedicion" DATE NOT NULL,
  "valor" VARCHAR(45 ),
  PRIMARY KEY ("fechaMedicion"));


-- -----------------------------------------------------
-- Table "mydb"."MEDICIONES"
-- -----------------------------------------------------
CREATE TABLE "MEDICIONES" (
  "id" INTEGER NOT NULL,
  "fecha" VARCHAR(45) NOT NULL,
  PRIMARY KEY ("id", "fecha"),
  FOREIGN KEY ("id")
  REFERENCES "SENSOR" ("id"));



ALTER TABLE "USUARIO" ADD FOREIGN KEY ("sensorFav")  REFERENCES "SENSOR" ("id");
ALTER TABLE "USUARIO" ADD FOREIGN KEY ("sensorLike") REFERENCES "SENSOR" ("id");

 



