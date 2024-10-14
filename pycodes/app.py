from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
# Importando e registrando rotas
from routes import task_routes
from auth import auth_routes

app = Flask(__name__)
app.register_blueprint(task_routes)
app.register_blueprint(auth_routes)
# Configurações do banco de dados (conectando ao PostgreSQL no Neon)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://list_db_owner:your_password@ep-plain-block-a5flllmm.us-east-2.aws.neon.tech/list_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuração JWT
app.config['JWT_SECRET_KEY'] = 'sua_chave_secreta'

# Inicializando a extensão SQLAlchemy e outras
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

if __name__ == '__main__':
    app.run(debug=True)
