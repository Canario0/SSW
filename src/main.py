#coding: utf-8
from flask import Flask, render_template, request, redirect, url_for

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

@app.route("/<user>/configuracion")
def config(user):
    return render_template('configuracion_perfil.html', user = user)




@app.route("/HolaMundo")
def hello():
    return "Hello World3!"

# Es llamado anstes de terminar la petición
# @app.teardown_appcontext
# def close_db(error):
#     """Closes the database again at the end of the request."""
#     if hasattr(g, 'sqlite_db'):
#         g.sqlite_db.close()
