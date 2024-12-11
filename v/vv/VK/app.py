from flask import Flask, render_template, request, flash, redirect, Blueprint
app = Flask(__name__)
app.config['SECRET_KEY'] = 'f77a90697fc48d53e3b05a15bd8c214697f139351362b3febaa190ccd4a3d4e2'

conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/Doacoes_db"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from database import db
from flask_migrate import Migrate
from models import Doadores, Doacoes

db.init_app(app)
migrate = Migrate(app, db)

from modulos.Doadores.Doadores import bp_Doadores
app.register_blueprint(bp_Doadores, url_prefix='/Doadores')

from modulos.Doacoes.Doacoes import bp_Doacoes
app.register_blueprint(bp_Doacoes, url_prefix='/Doacoes')

@app.route("/")
def index():
    return render_template("index.html")