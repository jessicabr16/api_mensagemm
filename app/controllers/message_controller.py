from flask import request, jsonify
from app.models.message import Mensagem
from app import db

def listar_mensagens():
    mensagens = Mensagem.query.all()
    return jsonify([m.to_dict() for m in mensagens])

def obter_mensagem(id):
    mensagem = Mensagem.query.get(id)
    if mensagem:
        return jsonify(mensagem.to_dict())
    return jsonify({'erro': 'Mensagem não encontrada'}), 404

def criar_mensagem():
    conteudo = request.get_json().get('conteudo')
    if conteudo == "":
        return jsonify({'erro': 'Mensagem vazia'}), 400
    nova_mensagem = Mensagem(conteudo=conteudo)
    db.session.add(nova_mensagem)
    db.session.commit()
    return jsonify(nova_mensagem.to_dict()), 201

def atualizar_mensagem(id):
    mensagem = Mensagem.query.get(id)
    if mensagem:
        novo_conteudo = request.get_json().get('conteudo')
        if novo_conteudo == "":
            return jsonify({'erro': 'Mensagem vazia'}), 400
        mensagem.conteudo = novo_conteudo
        db.session.commit()
        return jsonify(mensagem.to_dict())
    return jsonify({'erro': 'Mensagem não encontrada'}), 404

def deletar_mensagem(id):
    mensagem = Mensagem.query.get(id)
    if mensagem:
        db.session.delete(mensagem)
        db.session.commit()
        return jsonify({"mensagem": "Mensagem deletada com sucesso"})
    return jsonify({"erro": "Mensagem não encontrada"}), 404
