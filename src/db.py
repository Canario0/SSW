from peewee import Model, MySQLDatabase,BooleanField, CharField, IntegerField, DateField, DateTimeField, ForeignKeyField, CompositeKey, DoubleField
from flask_login import UserMixin
from app import loginmn
import configparser
import datetime

conf = configparser.ConfigParser()
conf.read('config.conf')

db = MySQLDatabase(conf['DataBase']['name'], user=conf['DataBase']['user'], password=conf['DataBase']
                   ['password'], host=conf['DataBase']['host'], port=int(conf['DataBase']['port']))


class Usuario(Model, UserMixin):
    nickname = CharField(max_length=20, primary_key=True)
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
    id = IntegerField(primary_key=True)
    nickname = ForeignKeyField(Usuario, backref='sensores', db_column='nickname')
    nombre = CharField(max_length=10, null=False)
    descripcion = CharField(null=True)
    tipo = IntegerField(null=False)
    visible = BooleanField(null=False, default=True)
    x = DoubleField(null=False)
    y = DoubleField(null=False)

    class Meta:
        database = db


class Favorito(Model):
    nickname = ForeignKeyField(Usuario, db_column='nickname')
    id = ForeignKeyField(Sensor,db_column='id')

    class Meta:
        database = db
        primary_key = CompositeKey('nickname', 'id')


class Liked(Model):
    nickname = ForeignKeyField(Usuario, db_column='nickname')
    id = ForeignKeyField(Sensor, db_column='id')

    class Meta:
        database = db
        primary_key = CompositeKey('nickname', 'id')


class Medicion(Model):
    id = ForeignKeyField(Sensor, backref='mediciones', db_column='id')
    # este valor se autogenera
    fechaSubida = DateTimeField(
        default=datetime.datetime.now, primary_key=True)
    fechaMedicion = DateField(null=False)
    valor = DoubleField(null=False)

    class Meta:
        database = db

#-----------------------------------------------------------------------------
#           Creación de las tuplas
#-----------------------------------------------------------------------------
def create_Usuario(nickname, password):
    with db.atomic():
        Usuario.create(nickname=nickname, password=password)

def create_Sensor(id, nombre, descripcion, tipo, visible, x, y):
    with db.atomic():
        Sensor.create(id = id, nombre = nombre, descripcion = descripcion, tipo = tipo, visible = visible, x = x, y = y)

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


#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
#       Consultas
#----------------------------------------------------------------------------
@loginmn.user_loader
def loader_Usuario(nickname):
    return Usuario.get(Usuario.nickname == nickname)

def get_Usuario(nickname):
    return list (Usuario.select().where(Usuario.nickname == nickname).dicts())

def get_Sensor_ById(id):
    return list (Sensor.select().where(Sensor.id == id).dicts())

def get_Sensor_ByUser(nickname):
    user = Usuario.get(Usuario.nickname == nickname)
    return list(user.sensores.dicts())
#return  user.sensores


def get_Mediciones(id):
    sensor= Sensor.select().where(Sensor.id == id)
    return list(sensor.mediciones.dicts()) if len(list(sensor))>0 else []
#----------------------------------------------------------------------------


def ini():
    db.connect()

def fin():
    db.close()


