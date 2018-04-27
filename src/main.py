#coding: utf-8
from flask import Flask, render_template, request, redirect, url_for, flash
from peewee import Model, MySQLDatabase, BooleanField, CharField, IntegerField, DateField, DateTimeField, ForeignKeyField, CompositeKey, DoubleField
import configparser
import datetime
import os
from db import *

app = Flask(__name__)
app.config['SECRET_KEY']=os.urandom(24)

@app.route("/")
@app.route("/index")
def index():
    return render_template('principalSinRegistrar.html')


# esta interaccion no está probada, probarla por la mañana
@app.route("/sensor/<id>/anadirMedidas", methods=['POST', 'GET'])
def addMedition():
    if request.method == 'GET':
        return render_template('añadirMedidas.html')
    elif request.method == 'POST':
        fechaMedicion = request.form['fecha-medicion']
        medida = request.form['medida']
        createMedicion(id, fechaMedicion, medida)


@app.route("/registrar", methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('Registrar.html')
    elif request.method == 'POST':
        user = request.form['nick-name']
        password = request.form['contraseña']
        repassword = request.form['recontraseña']
        #if len(get_Usuario(user)) == 0:
        if get_Usuario(user) == []:
            if password == repassword:
                create_Usuario(user, password)
                return redirect(url_for('logged_index', user=user))
            else:
                flash('Las contraseñas no coinciden')
        else:
            flash('Nick-name en uso')
        return redirect(url_for('register'))

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('Login.html')
    elif request.method == 'POST':
        user = request.form['nick-name']
        password = request.form['contraseña']
        if get_Usuario(user) != []:
            if get_Usuario(user)[0]['password'] == password:
                return redirect(url_for('logged_index', user=user))
            else:
                flash('Contrasñea incorrecta')
        else:
            flash('El usuario no existe')
        return redirect(url_for('login'))

@app.route("/<user>/configuracion", methods=['POST', 'GET'])
def config(user):
    usuario = get_Usuario(user)[0]
    if request.method == 'GET':
        usuario = {i: usuario[i] if usuario[i] != None else '' for i in usuario}
        return render_template('configuracion_perfil.html',
            user=user,
            email=usuario['email'],
            nombre=usuario['nombre'],
            apellido1=usuario['apellido1'],
            apellido2=usuario['apellido2'],
            direccion=usuario['direccion'],
            empresa=usuario['empresa'],
            telefono=usuario['telefono'])

    elif request.method == 'POST':
        form = request.form
        usuario['email'] = form.get('email') if(form.get('email')!= '') else usuario['email']
        usuario['nombre'] = form.get('nombre') if(form.get('nombre')!= '') else usuario['nombre']
        usuario['apellido1'] = form.get('apellido1') if(form.get('apellido1')!= '') else usuario['apellido1']
        usuario['apellido2'] = form.get('apellido2') if(form.get('apellido2')!= '') else usuario['apellido2']
        usuario['direccion'] = form.get('direccion') if(form.get('direccion')!= '') else usuario['direccion']
        usuario['empresa'] = form.get('empresa') if(form.get('empresa')!= '') else usuario['empresa']
        usuario['telefono'] = form.get('telefono') if(request.form.get('telefono')!= '') else usuario['telefono']
        if 'imagen' in request.files:
            imagen = request.files['imagen']
            if imagen.filename != '':
                imagen.save('static/img/users/' + user)

        update_Usuario(usuario)
        return redirect(url_for('config', user=user))

@app.route("/<user>/")
@app.route("/<user>/index")
def logged_index(user):
    return render_template('principalRegistrado.html', user=user)


@app.route("/<user>/profile")
def profile(user):
#	sensoresUsuario = get_Usuario()
#	for messages in sensoresUsuario.sensores[0]:
#		print(messages)
    rows = get_Sensor_ByUser(user)
    return render_template('usuario.html', user=user, rows=rows)


@app.route("/<user>/sensores_favoritos")
def fav(user):
    return render_template('sensores_fav.html', user=user)


@app.route("/<user>/registrar_sensor")
def registrar_sensor(user):
    return render_template('registrar_sensor.html', user=user)


@app.route("/sensor/<id>")
def informacion_sensor(id):
    return render_template('info_sensor.html', id=id)


@app.before_request
def before_request():
    ini()


@app.after_request
def after_request(response):
    fin()
    return response
