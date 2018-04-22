from peewee import *
import configparser

conf = configparser.ConfigParser()
conf.read('config.txt')

db = MySQLDatabase(conf['DataBase']['name'], user=conf['DataBase']['user'], password=conf['DataBase']
                   ['password'], host=conf['DataBase']['host'], port=conf['DataBase']['port'])

class Usuario(Model):
    nickname = CharField(max_length=20, primary_key= True)
    email = CharField(null=False)
    password = CharField(max_length=10,null= False, unique = True)
    nombre = CharField(max_length=10, null= True)
    apellidos = CharField(max_length=20, null= True)
    direccion = CharField(max_length=30, null= True)
    nacimiento = DateField(null= True)
    empresa = CharField(max_length=30, null= True)
    telefono = IntegerField(null= True)
    class Meta:
        database = db

class Sensor(Model):
    id = IntegerField(primary_key=True)
    nombre = CharField(max_length=10, null= False)
    descripcion = CharField(null = True)
    tipo = IntegerField(null=False)
    visible = BooleanField(null=False, default=True)
    x = IntegerField(null=False)
    y = IntegerField(null=False)
    class Meta:
        database = db

class Favorito(Model):
    nickname=ForeignKeyField(Usuario)
    id = ForeignKeyField(Sensor)
    class Meta:
        database = db
        primary_key = CompositeKey('nickname', 'tag')

class Like(Model):
    nickname=ForeignKeyField(Usuario)
    id = ForeignKeyField(Sensor)
    class Meta:
        database = db
        primary_key = CompositeKey('nickname', 'tag')




