from peewee import Model, MySQLDatabase,BooleanField, CharField, IntegerField, DateField, DateTimeField, ForeignKeyField, CompositeKey, DoubleField
from playhouse.shortcuts import model_to_dict
from flask_login import UserMixin
import configparser
import datetime

conf = configparser.ConfigParser()
conf.read('config.conf')

db = MySQLDatabase(conf['DataBase']['name'], user=conf['DataBase']['user'], password=conf['DataBase']
                   ['password'], host=conf['DataBase']['host'], port=int(conf['DataBase']['port']))


class Usuario(Model, UserMixin):
    nickname = CharField(max_length=20, primary_key=True, db_column='nickname')
    email = CharField(max_length=45,null=True)
    password = CharField(max_length=10, null=False)
    nombre = CharField(max_length=10, null=True)
    apellido1 = CharField(max_length=20, null=True)
    apellido2 = CharField(max_length=20, null=True)
    direccion = CharField(max_length=100, null=True)
    nacimiento = DateField(null=True)
    empresa = CharField(max_length=30, null=True)
    telefono = IntegerField(null=True)

    def get_id(self):
        return self.nickname
    class Meta:
        database = db


class Sensor(Model):
    id = IntegerField(primary_key=True,  db_column='id')
    nickname = ForeignKeyField(Usuario, backref='sensores', db_column='nickname', on_delete='CASCADE')
    nombre = CharField(max_length=10, null=False)
    descripcion = CharField(null=True)
    tipo = IntegerField(null=False)
    visible = BooleanField(null=False, default=True)
    x = DoubleField(null=False)
    y = DoubleField(null=False)

    class Meta:
        database = db


class Favorito(Model):
    nickname = ForeignKeyField(Usuario, db_column='nickname', on_delete='CASCADE')
    id = ForeignKeyField(Sensor,db_column='id', on_delete='CASCADE')

    class Meta:
        database = db
        primary_key = CompositeKey('nickname', 'id')


class Liked(Model):
    nickname = ForeignKeyField(Usuario, db_column='nickname', on_delete='CASCADE')
    id = ForeignKeyField(Sensor, db_column='id', on_delete='CASCADE')

    class Meta:
        database = db
        primary_key = CompositeKey('nickname', 'id')

 
class Medicion(Model):
    id = ForeignKeyField(Sensor, backref='mediciones', db_column='id', on_delete='CASCADE')
    # este valor se autogenera
    fechaSubida = DateTimeField(
        default=datetime.datetime.now, primary_key=True)
    fechaMedicion = CharField(max_length=20, null=False)
    valor = DoubleField(null=False)

    class Meta:
        database = db

#-----------------------------------------------------------------------------
#           Creación de las tuplas
#-----------------------------------------------------------------------------
def create_Usuario(nickname, password):
    with db.atomic():
        Usuario.create(nickname=nickname, password=password)

def create_Sensor(nickname, nombre, descripcion, tipo, visible, x, y):
    with db.atomic():
        Sensor.create(nickname = nickname, nombre = nombre, descripcion = descripcion, tipo = tipo, visible = visible, x = x, y = y)

def create_Favorito(nickname, id):
    with db.atomic():
        Favorito.create(nickname=nickname, id=id)

def create_Liked(nickname, id):
    with db.atomic():
        Liked.create(nickname=nickname, id=id)

def create_Medicion(id, fechaMedicion, valor):
    with db.atomic():
        Medicion.create(id = id, fechaMedicion = fechaMedicion, valor = valor)
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
#       Actualizaciones
#----------------------------------------------------------------------------
def update_Usuario(user):
     with db.atomic():
        Usuario.update(**user).where(Usuario.nickname == user['nickname']).execute()

def update_Sensor(sensor):
     with db.atomic():
        Sensor.update(**sensor).where(Sensor.id == sensor['id']).execute()

def delete_Sensor(id):
    with db.atomic():
        Sensor.delete().where(Sensor.id == id).execute()

def delete_Favorito(user,id):
    with db.atomic():
        Favorito.delete().where(Favorito.id == id, Favorito.nickname == user).execute()

def delete_Like(user, id):
    with db.atomic():
        Liked.delete().where(Liked.id == id, Liked.nickname == user).execute()

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
#       Consultas
#----------------------------------------------------------------------------
def get_Usuario(nickname):
    return list (Usuario.select().where(Usuario.nickname == nickname).dicts())

def get_Sensor_ById(id):
    return model_to_dict(Sensor.get(Sensor.id == id))

def get_Sensors(visible = 1):
    return list(Sensor.select().where(Sensor.visible == visible).dicts())

def get_Sensor_ByUser(nickname):
    user = Usuario.get(Usuario.nickname == nickname)
    return list(user.sensores.dicts())

def get_Last_Mediciones(id):
    sensor= Sensor.get(Sensor.id == id)
    return list(sensor.mediciones.order_by(Medicion.fechaSubida.desc()).limit(5).dicts())

def get_Mediciones(id):
    sensor= Sensor.get(Sensor.id == id)
    return list(sensor.mediciones.order_by(Medicion.fechaSubida.asc()).dicts())

def get_Favoritos(nickname):
    return list(Sensor.select().join(Favorito).where(Favorito.nickname == nickname).dicts())
  
def get_InfoLikes(id):
    return Liked.select().where(Liked.id == id).count()

def get_alreadyLiked(nickname, id):
    aux = list(Liked.select().where(Liked.nickname == nickname, Liked.id == id)) 
    return True if len(aux) != 0 else False
  
def get_Busqueda(campo, parametro, user):
    if(campo == "nombre"):
        return list(Sensor.select().where(Sensor.nombre == parametro, Sensor.nickname == user).dicts())
    elif(campo == "tipo"):
        return list(Sensor.select().where(Sensor.tipo == parametro, Sensor.nickname == user).dicts())
    else:
        return list(Sensor.select().where(Sensor.id == parametro, Sensor.nickname == user).dicts())

def get_BusquedaFav(campo, parametro):
    if(campo == "nombre"):
        return list(Sensor.select().where(Sensor.nombre == parametro).dicts())
    elif(campo == "tipo"):
        return list(Sensor.select().where(Sensor.tipo == parametro).dicts())
    else:
        return list(Sensor.select().where(Sensor.id == parametro).dicts())
#----------------------------------------------------------------------------


def ini():
    db.connect()

def fin():
    db.close()


