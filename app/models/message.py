from app import db

class Mensagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    conteudo = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {"id": self.id, "conteudo": self.conteudo}