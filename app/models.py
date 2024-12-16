from app import db

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True)
    cpf = db.Column(db.String(14), unique=True)
    sexo = db.Column(db.String(1))
    telefone = db.Column(db.String(20))
    cep = db.Column(db.String(10))
    cidade = db.Column(db.String(120))
    bairro = db.Column(db.String(120))
    logradouro = db.Column(db.String(120))
    numero = db.Column(db.String(10))
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    senha = db.Column(db.String(50), nullable=False)
    data_cadastro = db.Column(db.DateTime, nullable=False)
    ultimo_acesso = db.Column(db.DateTime)

    def __repr__(self):
        return f"<Usuario {self.nome}>"
    

class Publicacao(db.Model):
    __tablename__ = 'publicacao'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(300))
    data = db.Column(db.DateTime, nullable=False)
    ativo = db.Column(db.Integer, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    usuario = db.relationship('Usuario', backref=db.backref('publicacoes', lazy=True))
    planta_id = db.Column(db.Integer, db.ForeignKey('planta.id'), nullable=False)
    planta = db.relationship('Planta', backref=db.backref('publicacoes', lazy=True))

    def __repr__(self):
        return f"<Publicacao {self.id}>"


class Contactar(db.Model):
    __tablename__ = 'contactar'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.DateTime, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    usuario = db.relationship('Usuario', backref=db.backref('contactados', lazy=True))
    publicacao_id = db.Column(db.Integer, db.ForeignKey('publicacao.id'), nullable=False)
    publicacao = db.relationship('Publicacao', backref=db.backref('contactados', lazy=True))

    def __repr__(self):
        return f"<Contactar Usuario: {self.usuario_id}, Publicacao: {self.publicacao_id}>"
    

class Favorito(db.Model):
    __tablename__ = 'favorito'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    publicacao_id = db.Column(db.Integer, db.ForeignKey('publicacao.id'), nullable=False)
    data_favorito = db.Column(db.DateTime, nullable=False)

    usuario = db.relationship('Usuario', backref=db.backref('favoritos', lazy=True))
    publicacao = db.relationship('Publicacao', backref=db.backref('favoritos', lazy=True))

    def __repr__(self):
        return f"<Favorito Usuario: {self.usuario_id}, Publicacao: {self.publicacao_id}>"


class Interesse(db.Model):
    __tablename__ = 'interesse'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.DateTime, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    usuario = db.relationship('Usuario', backref=db.backref('interessados', lazy=True))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    categoria = db.relationship('Categoria', backref=db.backref('interessados', lazy=True))

    def __repr__(self):
        return f"<Interesse {self.id}>"
    

class Planta(db.Model):
    __tablename__ = 'planta'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_popular = db.Column(db.String(255))
    nome_cientifico = db.Column(db.String(255))
    familia = db.Column(db.String(255))
    origem = db.Column(db.String(255))
    descricao = db.Column(db.String(1000))
    ciclo_vida = db.Column(db.String(400))
    crescimento = db.Column(db.String(500))
    quando_fruto = db.Column(db.String(255))
    quando_flores = db.Column(db.String(255))
    flores = db.Column(db.String(700))
    clima_nativo = db.Column(db.String(200))
    clima_permitido = db.Column(db.String(200))
    adubacao = db.Column(db.String(1200))
    como_regar = db.Column(db.String(1000))
    aceita_poda = db.Column(db.Integer)
    sombra = db.Column(db.String(255))
    altura_muda = db.Column(db.String(100))

    def __repr__(self):
        return f"<Planta {self.nome_popular}>"
    

class Categoria(db.Model):
    __tablename__ = 'categoria'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"<Categoria {self.nome}>"
    

class CategoriaPlanta(db.Model):
    __tablename__ = 'categoria_planta'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    categoria = db.relationship('Categoria', backref=db.backref('categoria_planta', lazy=True))
    planta_id = db.Column(db.Integer, db.ForeignKey('planta.id'), nullable=False)
    planta = db.relationship('Planta', backref=db.backref('categoria_planta', lazy=True))

    def __repr__(self):
        return f"<CategoriaPlanta Categoria: {self.categoria_id}, Planta: {self.planta_id}>"
        

class Notificacao(db.Model):
    __tablename__ = 'notificacao'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(300), nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    publicacao_id = db.Column(db.Integer, db.ForeignKey('publicacao.id'), nullable=False)
    publicacao = db.relationship('Publicacao', backref=db.backref('notificacoes', lazy=True))
    interesse_id = db.Column(db.Integer, db.ForeignKey('interesse.id'), nullable=False)
    interesse = db.relationship('Interesse', backref=db.backref('notificacoes', lazy=True))

    def __repr__(self):
        return f"<Notificacao {self.descricao}>"
    

class Foto(db.Model):
    __tablename__ = 'foto'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(120), nullable=False)
    caminho = db.Column(db.String(120), nullable=False)
    data_cadastro = db.Column(db.DateTime, nullable=False)
    publicacao_id = db.Column(db.Integer, db.ForeignKey('publicacao.id'), nullable=False)
    publicacao = db.relationship('Publicacao', backref=db.backref('fotos', lazy=True))

    def __repr__(self):
        return f"<Foto {self.nome}>"