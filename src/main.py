from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('principalSinRegistrar.html')

@app.route("/Registrar")
def register():
    return render_template('Registrar.html')


@app.route("/HolaMundo")
def hello():
    return "Hello World3!"

# Es llamado anstes de terminar la petición
# @app.teardown_appcontext
# def close_db(error):
#     """Closes the database again at the end of the request."""
#     if hasattr(g, 'sqlite_db'):
#         g.sqlite_db.close()
