from flask import Blueprint, render_template, request, redirect, flash
from models import Doacoes, Doadores
from database import db

bp_Doacoes = Blueprint('Doacoes', __name__, template_folder="templates")

@bp_Doacoes.route("/")
def index():
    t = Doacoes.query.all()
    return render_template("Doacoes.html", dados=t)


@bp_Doacoes.route("/add")
def add():
    p = Doadores.query.all()
    return render_template("Doacoes_add.html", Doadores=p)


@bp_Doacoes.route("/save", methods=['POST'])
def save():
    valor = request.form.get("valor")
    data = request.form.get("data")
    id_Doadores = request.form.get("id_Doadores")
    if valor and data and id_Doadores:
        db_Doacoes = Doacoes(valor, data, id_Doadores)
        db.session.add(db_Doacoes)
        db.session.commit()
        flash("Doacoes cadastrada!")
        return redirect("/Doacoes")
    else:
        flash("Preencha todos os campos!")
        return redirect("/Doacoes/add")
    

@bp_Doacoes.route("/remove/<int:id>")
def remove(id):
    t = Doacoes.query.get(id)
    try:
        db.session.delete(t)
        db.session.commit()
        flash("Doacoes removida!")
        return redirect("/Doacoes")
    except:
        flash("Doacoes Inválida!")
        return redirect("/Doacoes")
    


@bp_Doacoes.route("/edit/<int:id>")
def edit(id):
    t = Doacoes.query.get(id)
    return render_template("Doacoes_edit.html", dados=t)


@bp_Doacoes.route("/edit-save", methods=['POST'])
def edit_save():
    valor = request.form.get("valor")
    data = request.form.get("data")
    id_Doadores = request.form.get("id_Doadores")
    id = request.form.get("id")
    if valor and data and id_Doadores and id:
        t = Doacoes.query.get(id)
        t.valor = valor
        t.data = data
        t.id_Doadores = id_Doadores
        db.session.commit()
        flash("Dados atualizados!")
        return redirect("/Doacoes")
    else:
        flash("Preencha todos os campos!")
        return redirect("/Doacoes")