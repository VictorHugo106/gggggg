from database import db

class Doadores(db.Model):
    __tablename__ = 'tb_Doadores'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    telefone = db.Column(db.String(15))


    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


    def __repr__(self):
        return f"<Doadores {self.nome}>"
    

class Doacoes(db.Model):
    __tablename__ = 'tb_Doacoes'
    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.DECIMAL(10, 2))
    data = db.Column(db.DATE)
    id_Doadores = db.Column(db.Integer, db.ForeignKey('tb_Doadores.id'))

    Doadores = db.relationship('Doadores', foreign_keys=id_Doadores)


    def __init__(self, valor, data, id_Doadores):
        self.valor = valor
        self.data = data
        self.id_Doadores = id_Doadores

    
    def __repr__(self):
        return f"<Doacoes {self.valor} - {self.Doadores.nome}>"