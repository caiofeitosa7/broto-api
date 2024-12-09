from flask import Blueprint, jsonify, request
from app.controllers.user_controller import criar_usuario, listar_usuarios

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return jsonify({"mensagem": "Bem-vindo à API Flask!"})

@main.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = listar_usuarios()
    return jsonify([{"id": u.id, "nome": u.nome, "email": u.email} for u in usuarios])

@main.route('/usuarios', methods=['POST'])
def add_usuario():
    dados = request.json
    criar_usuario(nome=dados['nome'], email=dados['email'])
    return jsonify({"mensagem": "Usuário criado com sucesso!"}), 201
