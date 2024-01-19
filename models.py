from app import db

class Usuario(db.Model):
    id = db.Column('id', db.Integer, primary_key = True, autoincrement=True)
    usuario = db.Column(db.String(255))
    senha = db.Column(db.String(255))
    tarefas = db.relationship('Tarefas', backref="usuario", lazy=True)

    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

class Tarefas(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    tarefa = db.Column(db.String(150))
    descricao = db.Column(db.String(250))
    data = db.Column(db.String(15))
    hora = db.Column(db.String(15))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    def __init__(self, tarefa, descricao, data, hora, usuario_id):
        self.tarefa = tarefa
        self.descricao = descricao
        self.data = data
        self.hora = hora
        self.usuario_id = usuario_id

