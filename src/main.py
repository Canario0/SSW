#coding: utf-8
from flask import Flask, render_template, request, redirect, url_for
from peewee import Model, MySQLDatabase,BooleanField, CharField, IntegerField, DateField, DateTimeField, ForeignKeyField, CompositeKey, DoubleField
import configparser
import datetime


app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('principalSinRegistrar.html')

@app.route("/registrar", methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('Registrar.html')
    elif request.method == 'POST':
        user = request.form['nick-name']
        password = request.form['contraseña']
        repassword = request.form['recontraseña']
        #if password == repassword:
            #if no existe user:
        return redirect(url_for('logged_index', user=user))
            #else:
            #usuario ya existe
        #else:
            #No coinciden las contraseñas

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('Login.html')
    elif request.method == 'POST':
        user = request.form['nick-name']
        password = request.form['contraseña']
        #if existe user y passwd
        return redirect(url_for('logged_index', user=user))
        #else:
            #Usuario y contraseña incorrectos

@app.route("/<user>/configuracion", methods=['POST', 'GET'])
def config(user):
    if request.method == 'GET':
        return render_template('configuracion_perfil.html', user = user)
    elif request.method == 'POST':
        if 'nombre' in request.form:
            nombre = request.form['nombre']
            #Guardar nombre en la base de datos
        if 'ap1' in request.form:
            ap1 = request.form['ap1']
            #Lo mismo con ap1
        if 'ap2' in request.form:
            ap2 = request.form['ap2']
        if 'user' in request.form:
            newuser = request.form['user']
        if 'direccion' in request.form:
            direccion = request.form['direccion']
        if 'empresa' in request.form:
            empresa = request.form['empresa']
        if 'tfno' in request.form:
            tfno = request.form['tfno']
        if 'imagen' in request.files:
            imagen = request.files['imagen']
            if imagen.filename != '':
                imagen.save('static/img/users/' + user)
        
        return redirect(url_for('config', user=user))

@app.route("/<user>/")
@app.route("/<user>/index")
def logged_index(user):
    return render_template('principalRegistrado.html', user = user)

@app.route("/<user>/profile")
def profile(user):
    return render_template('usuario.html', user = user)

@app.route("/<user>/sensores_favoritos")
def fav(user):
    return render_template('sensores_fav.html', user = user)

@app.route("/<user>/registrar_sensor")
def registrar_sensor(user):
    return render_template('registrar_sensor.html', user = user)

@app.route("/HolaMundo")
def hello():
    return "Hello World3!"

#----------------------------------------------------------------------

conf = configparser.ConfigParser()
conf.read('config.txt')

db = MySQLDatabase(conf['DataBase']['name'], user=conf['DataBase']['user'], password=conf['DataBase']['password'], host=conf['DataBase']['host'], port=int(conf['DataBase']['port']))


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


#db.connect()
@app.before_request
def before_request():
    db.connect()

@app.after_request
def after_request(response):
    db.close()
    return response

create_Usuario('pipo', '1235aaaa')
user = list(Usuario.select().where(Usuario.nickname=='pipo').dicts())
print(user)

