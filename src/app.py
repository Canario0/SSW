#coding: utf-8
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from urllib.parse import urlparse
import configparser
import datetime
import os
import json
from db import *


app = Flask(__name__)
loginmn = LoginManager(app)
loginmn.login_view = 'login'
app.config['SECRET_KEY']=os.urandom(24)

@app.route("/")
@app.route("/index")
def index():
    sensores = get_Sensors()
    return render_template('principalSinRegistrar.html', sensores=sensores)


@app.route("/sensor/<id>/registrar_medida", methods=['POST', 'GET'])
@login_required
def addMedition():
    if request.method == 'GET':
        return render_template('registrar_medida.html')
    elif request.method == 'POST':
        fechaMedicion = request.form['fecha-medicion']
        medida = request.form['medida']
        create_Medicion(id, fechaMedicion, medida)


@app.route("/registrar", methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for('logged_index', user = current_user.nickname))
        return render_template('Registrar.html')
    elif request.method == 'POST':
        user = request.form['nick-name']
        password = request.form['contraseña']
        repassword = request.form['recontraseña']
        #if len(get_Usuario(user)) == 0:
        if get_Usuario(user) == []:
            if password == repassword:
                create_Usuario(user, password)
                login_user(loader_Usuario(user))
                return redirect(url_for('logged_index', user=user))
            else:
                flash('Las contraseñas no coinciden')
        else:
            flash('Nick-name en uso')
        return redirect(url_for('register'))

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for('logged_index', user = current_user.nickname))
        return render_template('Login.html')
    elif request.method == 'POST':
        user = request.form['nick-name']
        password = request.form['contraseña']
        if get_Usuario(user) != []:
            if get_Usuario(user)[0]['password'] == password:
                login_user(loader_Usuario(user))
                next_page = request.args.get('next')
                if not next_page or url_parse(next_page).netloc != '':
                    return redirect(url_for('logged_index', user=user))
                else:
                    return redirect(next_page)
            else:
                flash('Contrasñea incorrecta')
        else:
            flash('El usuario no existe')
        return redirect(url_for('login'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/<user>/configuracion", methods=['POST', 'GET'])
@login_required
def config(user):
    if comprobar_Usuario(user):
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
    else:
        if current_user.is_authenticated:
            return redirect(url_for('logged_index', user=current_user.nickname))
        else:
            return redirect(url_for('index'))


@app.route("/<user>/")
@app.route("/<user>/index")
@login_required
def logged_index(user):
    sensores = get_Sensors()
    if comprobar_Usuario(user):
        return render_template('principalRegistrado.html', user=user, sensores=sensores)
    else:
        if current_user.is_authenticated:
            return redirect(url_for('logged_index', user=current_user.nickname, sensores=sensores))
        else:
            return redirect(url_for('index', sensores=sensores))


@app.route("/<user>/profile")
@login_required
def profile(user):
#	sensoresUsuario = get_Usuario()
#	for messages in sensoresUsuario.sensores[0]:
#		print(messages)
    if comprobar_Usuario(user):
        rows = get_Sensor_ByUser(user)
        return render_template('usuario.html', user=user, rows=rows)
    else:
        if current_user.is_authenticated:
            return redirect(url_for('logged_index', user=current_user.nickname))
        else:
            return redirect(url_for('index'))


@app.route("/<user>/sensores_favoritos")
@login_required
def fav(user):
    if comprobar_Usuario(user):
        return render_template('sensores_fav.html', user=user)
    else:
        if current_user.is_authenticated:
            return redirect(url_for('logged_index', user=current_user.nickname))
        else:
            return redirect(url_for('index'))


@app.route("/<user>/registrar_sensor")
@login_required
def registrar_sensor(user):
    if comprobar_Usuario(user):
        return render_template('registrar_sensor.html', user=user)
    else:
        if current_user.is_authenticated:
            return redirect(url_for('logged_index', user=current_user.nickname))
        else:
            return redirect(url_for('index'))


@app.route("/sensor/<id>")
@login_required
def informacion_sensor(id):
    user = request.args.get('user')
    sensor = get_Sensor_ById(id)
    return render_template('info_sensor.html', id=id, user=user, sensor=sensor)


@app.before_request
def before_request():
    ini()


@app.after_request
def after_request(response):
    fin()
    return response


@loginmn.user_loader
def loader_Usuario(nickname):
    return Usuario.get(Usuario.nickname == nickname)


def comprobar_Usuario(user):
    if current_user.nickname == user:
        return True
    else:
        return False
