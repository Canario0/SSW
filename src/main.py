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
        print (request.form)
        usuario['email'] = request.form['email'] if(request.form['email']!= '') else usuario['email']
        usuario['nombre'] = request.form['nombre'] if(request.form['nombre']!= '') else usuario['nombre']
        usuario['apellido1'] = request.form['apellido1'] if(request.form['appelido1']!= '') else usuario['apellido1']
        usuario['apellido2'] = request.form['apellido2'] if(request.form['apellido2']!= '') else usuario['apellido2']
        usuario['direccion'] = request.form['direccion'] if(request.form['direccion']!= '') else usuario['direccion']
        usuario['empresa'] = request.form['empresa'] if(request.form['empresa']!= '') else usuario['empresa']
        usuario['telefono'] = request.form['telefono'] if(request.form['telefono']!= '') else usuario['telefono']
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
		sensoresUsuario = get_Usuario()
		for messages in sensoresUsuario.sensores[0]:
			print(messages)
    return render_template('usuario.html', user=user)


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
