from app.models import Usuario
from app import db

def criar_usuario(nome, email):
    novo_usuario = Usuario(nome=nome, email=email)
    db.session.add(novo_usuario)
    db.session.commit()

def listar_usuarios():
    return Usuario.query.all()
