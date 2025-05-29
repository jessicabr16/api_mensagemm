from flask import Blueprint
from app.controllers import message_controller

messages_bp = Blueprint('messages', __name__)

messages_bp.route('/mensagens', methods=['GET'])(message_controller.listar_mensagens)
messages_bp.route('/mensagens/<int:id>', methods=['GET'])(message_controller.obter_mensagem)
messages_bp.route('/mensagens', methods=['POST'])(message_controller.criar_mensagem)
messages_bp.route('/mensagens/<int:id>', methods=['PUT'])(message_controller.atualizar_mensagem)
messages_bp.route('/mensagens/<int:id>', methods=['DELETE'])(message_controller.deletar_mensagem)