from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('principalSinRegistrar.html')

@app.route("/registrar")
def register():
    return render_template('Registrar.html')

@app.route("/login")
def login():
    return render_template('Login.html')

@app.route("/<user>/index")
def logged_index(user):
    return render_template('principalRegistrado.html', user = user)

@app.route("/<user>/profile")
def profile(user):
    return render_template('usuario.html', user = user)


@app.route("/HolaMundo")
def hello():
    return "Hello World3!"

# Es llamado anstes de terminar la petición
# @app.teardown_appcontext
# def close_db(error):
#     """Closes the database again at the end of the request."""
#     if hasattr(g, 'sqlite_db'):
#         g.sqlite_db.close()
