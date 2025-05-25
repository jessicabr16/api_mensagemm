from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False  # não ordenar o JSON automaticamente

# Lista de mensagens 
Mensagens = [
    {'id': 1, 'conteudo': 'Olá, mundo!'},
    {'id': 2, 'conteudo': 'Outra mensagem.'}
]

# GET para todas as mensagens
@app.route('/mensagens', methods=['GET'])
def get_mensagem():
    return jsonify(Mensagens)

# GET por id
@app.route('/mensagens/<int:id>', methods=['GET'])
def get_mensagem_por_id(id):
    for mensagem in Mensagens:
        if mensagem['id'] == id:
            return jsonify(mensagem)
    return jsonify({'erro': 'Mensagem não encontrada'}), 404

# POST para criar nova mensagem
@app.route('/mensagens', methods=['POST'])
def create_mensagem():
    conteudo = request.get_json().get('conteudo')
    nova_mensagem = {
        'id': len(Mensagens) + 1,
        'conteudo': conteudo
    }
    Mensagens.append(nova_mensagem)
    return jsonify(nova_mensagem), 201

# PUT para atualizar mensagem
@app.route('/mensagens/<int:id>', methods=['PUT'])
def atualizar_mensagem(id):
    novo_conteudo = request.get_json().get('conteudo')
    for mensagem in Mensagens:
        if mensagem['id'] == id:
            mensagem['conteudo'] = novo_conteudo
            return jsonify(mensagem)
    return jsonify({'erro': "Mensagem não encontrada"}), 404

# DELETE para apagar mensagem
@app.route('/mensagens/<int:id>', methods=['DELETE'])
def delete_mensagem(id):
    for i, mensagem in enumerate(Mensagens):
        if mensagem['id'] == id:
            del Mensagens[i]
            return jsonify({"mensagem": "Mensagem deletada com sucesso"})
    return jsonify({"erro": "Mensagem não encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True)
