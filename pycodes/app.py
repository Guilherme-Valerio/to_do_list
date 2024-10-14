from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError
from sqlalchemy import Column, Integer, String
from flask_migrate import Migrate


# Inicializa a aplicação Flask
app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

# Configurações do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://list_db_owner:ozwquikc1pr6@ep-plain-block-a5flllmm.us-east-2.aws.neon.tech:5432/list_db?sslmode=require'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco de dados
db = SQLAlchemy(app)

# Inicializa o Migrate
migrate = Migrate(app, db)

# Modelos
class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(128), nullable=False, unique=True)
    password = Column(String(512), nullable=False)

class Task(db.Model):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    user_id = Column(Integer, db.ForeignKey('user.id'), nullable=False)

# Rotas
@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('tasks'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('tasks'))
        flash('Credenciais inválidas', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        new_user = User(username=username, password=password)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registro realizado com sucesso', 'success')
            return redirect(url_for('login'))
        except IntegrityError:
            db.session.rollback()
            flash('Nome de usuário já existe', 'danger')
    return render_template('register.html')

@app.route('/tasks')
def tasks():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    tasks = Task.query.filter_by(user_id=user_id).all()
    return render_template('tasks.html', tasks=tasks)

@app.route('/tasks/add', methods=['POST'])
def add_task():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    title = request.form['title']
    new_task = Task(title=title, user_id=session['user_id'])
    db.session.add(new_task)
    db.session.commit()
    return '', 204

@app.route('/tasks/update/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    task = Task.query.get_or_404(task_id)
    task.title = request.json.get('title')
    db.session.commit()
    return '', 204

@app.route('/tasks/delete/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return '', 204

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

# Executa a criação das tabelas no banco de dados
with app.app_context():
    db.create_all()  # Cria as tabelas no banco de dados

if __name__ == '__main__':
    app.run(debug=True)
