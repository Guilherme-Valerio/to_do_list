import os

# Carregar a chave secreta do JWT das variáveis de ambiente
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'default_secret')  # valor padrão se não estiver definido
