#coding: utf-8
from flask import Flask, render_template, request, redirect, url_for
from peewee import Model, MySQLDatabase,BooleanField, CharField, IntegerField, DateField, DateTimeField, ForeignKeyField, CompositeKey, DoubleField
import configparser
import datetime
from db import * 


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

@app.before_request
def before_request():
    ini()

@app.after_request
def after_request(response):
    fin()
    return response
