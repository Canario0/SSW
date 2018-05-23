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
app.config['SECRET_KEY'] = os.urandom(24)

tipos_sensor = {"Temperatura": 1, "Humedad": 2,
                "Iluminación": 3, "Contaminación": 4, "Ruido": 5}
tipos_sensor2 = ['Temperatura', 'Humedad',
                 'Iluminación', 'Contaminación', 'Ruido']


@app.route("/default_img")
def default_img():
    return redirect(url_for('static', filename='img/users/default.png'))


def convertir_tipos(sensores):
    for x in sensores:
        x['tipo'] = tipos_sensor2[x['tipo']-1]


@app.route("/")
@app.route("/index")
def index():
    sensores = get_Sensors(1)
    convertir_tipos(sensores)
    return render_template('principalSinRegistrar.html', sensores=sensores)


@app.route("/<user>/sensor/<id>/registrar_medida", methods=['POST', 'GET'])
@login_required
def addMedition(user, id):
    if comprobar_Usuario(user):
        if request.method == 'GET':
            rows = get_Mediciones(id)
            return render_template('registrar_medida.html', user=user, id=id, rows=rows)
        elif request.method == 'POST':
            fechaMedicion = request.form['fecha-medicion']
            medida = round(float(request.form['medida']), 4)
            create_Medicion(id, fechaMedicion, medida)
            return redirect(url_for('informacion_sensor', user=user, id=id))
    else:
        if current_user.is_authenticated:
            return redirect(url_for('registrar_medicion.html', user=current_user.nickname))
        else:
            return redirect(url_for('index'))


@app.route("/registrar", methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for('logged_index', user=current_user.nickname))
        return render_template('Registrar.html')
    elif request.method == 'POST':
        user = request.form['nick-name']
        password = request.form['contraseña']
        repassword = request.form['recontraseña']
        # if len(get_Usuario(user)) == 0:
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
            return redirect(url_for('logged_index', user=current_user.nickname))
        return render_template('Login.html')
    elif request.method == 'POST':
        user = request.form['nick-name']
        password = request.form['contraseña']
        if get_Usuario(user) != []:
            if get_Usuario(user)[0]['password'] == password:
                login_user(loader_Usuario(user))
                next_page = request.args.get('next')
                if not next_page or urlparse(next_page).netloc != '':
                    return redirect(url_for('logged_index', user=user))
                else:
                    return redirect(next_page)
            else:
                flash('Contraseña incorrecta')
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
            usuario = {i: usuario[i] if usuario[i]
                       != None else '' for i in usuario}
            return render_template('configuracion_perfil.html',
                                   user=user,
                                   email=usuario['email'],
                                   fecha=usuario['nacimiento'],
                                   nombre=usuario['nombre'],
                                   apellido1=usuario['apellido1'],
                                   apellido2=usuario['apellido2'],
                                   direccion=usuario['direccion'],
                                   empresa=usuario['empresa'],
                                   telefono=usuario['telefono'])

        elif request.method == 'POST':
            form = request.form
            usuario['email'] = form.get('email') if(
                form.get('email') != '') else usuario['email']
            usuario['nombre'] = form.get('nombre') if(
                form.get('nombre') != '') else usuario['nombre']
            usuario['apellido1'] = form.get('apellido1') if(
                form.get('apellido1') != '') else usuario['apellido1']
            usuario['apellido2'] = form.get('apellido2') if(
                form.get('apellido2') != '') else usuario['apellido2']
            usuario['direccion'] = form.get('direccion') if(
                form.get('direccion') != '') else usuario['direccion']
            usuario['empresa'] = form.get('empresa') if(
                form.get('empresa') != '') else usuario['empresa']
            usuario['telefono'] = form.get('telefono') if(
                request.form.get('telefono') != '') else usuario['telefono']
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
    sensores = get_Sensors() + get_Sensors(0)
    sensores = [i for i in sensores if (
        i['visible'] == 0 and i['nickname'] == current_user.nickname) or i['visible'] == 1]
    convertir_tipos(sensores)
    if comprobar_Usuario(user):
        return render_template('principalRegistrado.html', user=user, sensores=sensores)
    else:
        if current_user.is_authenticated:
            return redirect(url_for('logged_index', user=current_user.nickname))
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
        convertir_tipos(rows)
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
        rows = get_Favoritos(user)
        convertir_tipos(rows)
        return render_template('sensores_fav.html', user=user, rows=rows)
    else:
        if current_user.is_authenticated:
            return redirect(url_for('logged_index', user=current_user.nickname))
        else:
            return redirect(url_for('index'))


@app.route("/<user>/registrar_sensor", methods=['POST', 'GET'])
@login_required
def registrar_sensor(user):
    if request.method == 'GET':
        if comprobar_Usuario(user):
            return render_template('registrar_sensor.html', user=user)
        else:
            if current_user.is_authenticated:
                return redirect(url_for('logged_index', user=current_user.nickname))
            else:
                return redirect(url_for('index'))
    elif request.method == 'POST':
        nombre = request.form['nombre']
        desc = request.form['descripcion']
        tipo = request.form['rating']
        visible = int(request.form['visibilidad'])
        x = request.form['lat']
        y = request.form['long']
        create_Sensor(user, nombre, desc,
                      tipos_sensor[tipo], visible, float(x), float(y))
        return redirect(url_for('profile', user=current_user.nickname))


@app.route("/<user>/sensor/<id>")
@login_required
def informacion_sensor(user, id):
    if comprobar_Usuario(user):
        sensor = get_Sensor_ById(id)
        rows = get_Mediciones(id)
        if user == sensor['nickname']['nickname']:
            return render_template('info_sensor.html', id=id, user=user, sensor=sensor, rows=rows, logeado=1, tipo = tipos_sensor2)
        else:
            return render_template('info_sensor.html', id=id, user=user, sensor=sensor, rows=rows, logeado=0, tipo = tipos_sensor2)
    else:
        if current_user.is_authenticated:
            return redirect(url_for('logged_index', user=current_user.nickname))
        else:
            return (redirect(url_for('index')))

@app.route("/sensor/<id>")
def informacion_sensor_sin_user(id):
    sensor = get_Sensor_ById(id)
    rows = get_Mediciones(id)
    return render_template('info_sensor.html', id=id, user=str(sensor['nickname']['nickname']), sensor=sensor, rows=rows, logeado=0, tipo = tipos_sensor2)


@app.route("/<user>/delete/<id>")
@login_required
def eliminar(user, id):
    if comprobar_Usuario(user):
        delete_Sensor(id)
        return redirect(url_for('profile', user=user))
    else:
        if current_user.is_authenticated:
            return redirect(url_for('logged_index', user=current_user.nickname))
        else:
            return (redirect(url_for('index')))


@app.route("/<user>/deleteFav/<id>")
@login_required
def eliminarFav(user, id):
    if comprobar_Usuario(user):
        delete_Favorito(user, id)
        return redirect(url_for('fav', user=user))
    else:
        if current_user.is_authenticated:
            return redirect(url_for('logged_index', user=current_user.nickname))
        else:
            return (redirect(url_for('index')))


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
