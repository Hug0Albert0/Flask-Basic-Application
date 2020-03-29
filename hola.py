from flask import Flask, request, make_response, redirect, abort, render_template, url_for, session, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config["SECRET_KEY"] = "13301053"

class FormularioNombreIndex(FlaskForm):
   nombre = StringField("¿Cuál es tu nombre?", validators=[DataRequired()])
   registrar = SubmitField("Registrar")

@app.route("/", methods = ["GET", "POST"])
@app.route("/index/", methods = ["GET", "POST"])
def index():
   formulario_nombre = FormularioNombreIndex()
   if formulario_nombre.validate_on_submit():
      viejo_nombre = session.get("nombre_usuario")
      if viejo_nombre is not None and viejo_nombre != formulario_nombre.nombre.data:
         flash("Has cambiado tu nombre")
      session["nombre_usuario"] = formulario_nombre.nombre.data
      return redirect(url_for("index"))
   return render_template(
      "index.html",
      formulario_nombre = formulario_nombre,
      nombre_usuario = session.get("nombre_usuario"),
      ahora = datetime.utcnow()
   )

@app.route("/mascota/")
@app.route("/mascota/<nombre_animal>")
def user(nombre_animal = None):
   return render_template(
      "mascota.html",
      nombre_animal = nombre_animal
   )

@app.errorhandler(404)
def page_not_found(e):
   return render_template("404.html"), 404


#@app.route("/agent/")
#def agent():
#   print(request.headers)
#   user_agent = request.headers.get("User-Agent")
#   """
#      request.headers => Host,User-Agent,Accept,Accept-Language,Accept-Encoding,
#      Connection,Upgrade-Insecure-Requests
#   """
#   return "<p>Tu navegador es {user_agent}</p>".format(user_agent = user_agent)
##Error 404
#@app.route("/error/")
#def error():
#   return "<h1>No soy mesero, soy el taquero...y abro a las 9</h1>", 400
#@app.route("/response/")
#def response():
#   response = make_response("<h1>Este documento tiene una cookie!</h1>")
#   response.set_cookie("answer", "42")
#   return response
#@app.route('/user/<id>')
#def get_user(id):
#user = load_user(id)
#if not user:
#abort(404)
#return '<h1>Hello, {}</h1>'.format(user.name)
#@app.route('/')
#def index():
#return redirect('http://www.example.com')