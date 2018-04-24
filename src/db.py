from peewee import Model, MySQLDatabase,BooleanField, CharField, IntegerField, DateField, DateTimeField, ForeignKeyField, CompositeKey, DoubleField
import configparser
import datetime

conf = configparser.ConfigParser()
conf.read('config.txt')

db = MySQLDatabase(conf['DataBase']['name'], user=conf['DataBase']['user'], password=conf['DataBase']
                   ['password'], host=conf['DataBase']['host'], port=int(conf['DataBase']['port']))


class Usuario(Model):
    nickname = CharField(max_length=20, primary_key=True)
    email = CharField(max_length=45,null=True)
    password = CharField(max_length=10, null=False)
    nombre = CharField(max_length=10, null=True)
    apellidos = CharField(max_length=20, null=True)
    direccion = CharField(max_length=100, null=True)
    nacimiento = DateField(null=True)
    empresa = CharField(max_length=30, null=True)
    telefono = IntegerField(null=True)

    class Meta:
        database = db


class Sensor(Model):
    id = IntegerField(primary_key=True)
    nombre = CharField(max_length=10, null=False)
    descripcion = CharField(null=True)
    tipo = IntegerField(null=False)
    visible = BooleanField(null=False, default=True)
    x = DoubleField(null=False)
    y = DoubleField(null=False)

    class Meta:
        database = db


class Favorito(Model):
    nickname = ForeignKeyField(Usuario)
    id = ForeignKeyField(Sensor)

    class Meta:
        database = db
        primary_key = CompositeKey('nickname', 'tag')


class Like(Model):
    nickname = ForeignKeyField(Usuario)
    id = ForeignKeyField(Sensor)

    class Meta:
        database = db
        primary_key = CompositeKey('nickname', 'tag')


class Medicion(Model):
    id = ForeignKeyField(Sensor, backref='mediciones')
    # este valor se autogenera
    fechaSubida = DateTimeField(
        default=datetime.datetime.now, primary_key=True)
    fechaMedicion = DateField(null=False)
    valor = DoubleField(null=False)

    class Meta:
        database = db


def create_Usuario(nickname, password):
    with db.atomic():
        Usuario.create(nickname=nickname, password=password)

def get_Usuario(nickname):
    list (Usuario.select().where(Usuario.nickname == nickname).dicts)


def ini():
    db.connect()

def fin():
    db.close()


