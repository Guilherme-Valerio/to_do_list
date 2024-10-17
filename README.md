**To-Do List Application** 


**--Visão Geral--**

Esta é uma aplicação de gerenciamento de tarefas (To-Do List) desenvolvida em Python utilizando o framework FastAPI/Flask no back-end, Redis para cache e um banco de dados relacional para armazenamento persistente. A aplicação permite criar, listar, atualizar e excluir tarefas, e é protegida com autenticação JWT.



**--Funcionalidades--**
- Autenticação de Usuário: O usuário pode criar uma conta, fazer login e gerenciar suas tarefas pessoais. Senhas são protegidas utilizando hash;
- Gerenciamento de Tarefas: A aplicação permite adicionar, editar e deletar tarefas;
- Prevenção de Duplicação: Não é possível adicionar tarefas com o mesmo título para o mesmo usuário;
- CRUD Completo: Todas as operações (Create, Read, Update, Delete) estão implementadas.



**--Tecnologias Utilizadas--**
- Back-end: Python (Flask)
-	Banco de Dados: Neon(PostgreSQL)
-	Autenticação: JWT
-	Front-end: HTML, CSS, JavaScript (AJAX)
-	Versionamento: Git/GitHub



**--Estrutura do Código--**
- Back-end: As principais rotas e funcionalidades do servidor estão no arquivo app.py, incluindo o registro de usuário, login, gerenciamento de tarefas e autenticação de sessões;
- Front-end: As interações com o usuário ocorrem por meio de formulários HTML e requisições AJAX utilizando fetch no JavaScript, para comunicação assíncrona com o servidor;
- Banco de Dados: A integração com o banco de dados Neon foi feita via SQLAlchemy, onde os modelos de usuário e tarefa são definidos.



**--Desafios--**
 - Um dos maiores desafios foi implementar a segurança, garantindo que as senhas dos usuários fossem armazenadas de forma segura e implementando autenticação via JWT para proteger as sessões.



**--Próximos Passos--**
- Adicionar filtros para organizar as tarefas por categorias;
- Melhorar a interface do usuário e torná-la mais responsiva.


________________________________________

**---Como Rodar o Projeto Localmente--**

**Pré-requisitos**
-	Python 3.8+: Certifique-se de ter o Python instalado.
-	Crie um ambiente virtual (opcional, mas recomendado).
- Instale as dependências do projeto com pip
- Acesse a aplicação em http://localhost:5000.
