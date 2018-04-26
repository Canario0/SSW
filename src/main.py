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
    usuario = {i: usuario[i] if usuario[i] != None else '' for i in usuario}
    if request.method == 'GET':
        nombre = usuario['nombre']
        ap1 = usuario['apellido1']
        ap2 = usuario['apellido2']
        dir = usuario['direccion']
        nac = usuario['nacimiento']
        emp = usuario['empresa']
        tel = usuario['telefono']
        mail = usuario['email']
        return render_template('configuracion_perfil.html', user=user, nombreUser=nombre, apellido1User=ap1, apellido2User=ap2, direccionUser=dir, empresaUser=emp, tfnoUser=tel, emailUser=mail)

    elif request.method == 'POST':
        if 'nombre' in request.form:
            usuario['nombre'] = request.form['nombre']
        if 'ap1' in request.form:
            usuario['apellido1'] = request.form['ap1']
        if 'ap2' in request.form:
            usuario['apellido2'] = request.form['ap2']
        if 'user' in request.form:
            usuario['nickname'] = request.form['user']
        if 'direccion' in request.form:
            usuario['direccion'] = request.form['direccion']
        if 'empresa' in request.form:
            usuario['empresa'] = request.form['empresa']
        if 'tfno' in request.form:
            usuario['telefono'] = request.form['tfno']
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
