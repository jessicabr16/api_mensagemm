from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mensagens.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Modelo de Mensagem
class Mensagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    conteudo = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {"id": self.id, "conteudo": self.conteudo}

# GET para todas as mensagens
@app.route('/mensagens', methods=['GET'])
def get_mensagem():
    mensagens = Mensagem.query.all()
    return jsonify([m.to_dict() for m in mensagens])

# GET por id
@app.route('/mensagens/<int:id>', methods=['GET'])
def get_mensagem_por_id(id):
    mensagem = Mensagem.query.get(id)
    if mensagem:
        return jsonify(mensagem.to_dict())
    return jsonify({'erro': 'Mensagem não encontrada'}), 404

# POST para criar nova mensagem
@app.route('/mensagens', methods=['POST'])
def create_mensagem():
    conteudo = request.get_json().get('conteudo')
    nova_mensagem = Mensagem(conteudo=conteudo)
    db.session.add(nova_mensagem)
    db.session.commit()
    return jsonify(nova_mensagem.to_dict()), 201

# PUT para atualizar mensagem
@app.route('/mensagens/<int:id>', methods=['PUT'])
def atualizar_mensagem(id):
    mensagem = Mensagem.query.get(id)
    if mensagem:
        novo_conteudo = request.get_json().get('conteudo')
        mensagem.conteudo = novo_conteudo
        db.session.commit()
        return jsonify(mensagem.to_dict())
    return jsonify({'erro': 'Mensagem não encontrada'}), 404

# DELETE para apagar mensagem
@app.route('/mensagens/<int:id>', methods=['DELETE'])
def delete_mensagem(id):
    mensagem = Mensagem.query.get(id)
    if mensagem:
        db.session.delete(mensagem)
        db.session.commit()
        return jsonify({"mensagem": "Mensagem deletada com sucesso"})
    return jsonify({"erro": "Mensagem não encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True)
