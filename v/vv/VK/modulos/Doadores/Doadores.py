from flask import Blueprint, render_template, request, redirect, flash
from models import Doadores
from database import db

bp_Doadores = Blueprint('Doadores', __name__, template_folder="templates")

@bp_Doadores.route("/")
def index():
    p = Doadores.query.all()
    return render_template("Doadores.html", dados=p)


@bp_Doadores.route("/add")
def add():
    return render_template("Doadores_add.html")


@bp_Doadores.route("/save", methods=['POST'])
def save():
    nome = request.form.get("nome")
    telefone = request.form.get("telefone")
    if nome and telefone:
        db_Doadores = Doadores(nome, telefone)
        db.session.add(db_Doadores)
        db.session.commit()
        flash("Doadores cadastrado!")
        return redirect("/Doadores")
    else:
        flash("Preencha todos os campos!")
        return redirect("/Doadores/add")
    

@bp_Doadores.route("/remove/<int:id>")
def remove():
    p = Doadores.query.get(id)
    try:
        db.session.delete(p)
        db.session.commit()
        flash("Doadores removido!")
        return redirect("/Doadores")
    except:
        flash("Doadores Inválido!")
        return redirect("/Doadores")


@bp_Doadores.route("/edit/<int:id>")
def edit():
    p = Doadores.query.get(id)
    return render_template("Doadores_edit.html", dados=p)


@bp_Doadores.route("/editsave", methods=['POST'])
def edit_save():
    nome = request.form.get("nome")
    telefone = request.form.get("telefone")
    id = request.form.get("id")
    if nome and telefone and id:
        p = Doadores.query.get(id)
        p.nome = nome
        p.telefone = telefone
        db.session.commit()
        flash("Dados atualizados!")
        return redirect("/Doadores")
    else:
        flash("Preencha todos os campos!")
        return redirect("/Doadores")