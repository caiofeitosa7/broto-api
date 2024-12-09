import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:suc0_b0l4ch4@localhost/broto'
    SECRET_KEY = "3c312c6nqod71NPpcmjdhdgUinFEILidAUIDN123126bYFD4E24579hkdsfsdl"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SECRET_KEY = os.getenv("SECRET_KEY", "minha_chave_secreta")
