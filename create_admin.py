from app import app, db  # Asegúrate de importar la instancia `app` de `app.py`
from models import User
from werkzeug.security import generate_password_hash

# Datos del administrador
username = 'alejandrojmf'
email = 'alejandrojmf96@gmail.com'
password = '123456'

# Establecer el contexto de la aplicación
with app.app_context():
    # Verificar si el administrador ya existe
    existing_admin = User.query.filter_by(username=username).first()
    if existing_admin:
        print("El usuario administrador ya existe.")
    else:
        # Crear el usuario administrador
        admin_user = User(
            username=username,
            email=email,
            password=generate_password_hash(password),
            is_admin=True  # Establece este usuario como administrador
        )
        db.session.add(admin_user)
        db.session.commit()
        print("Administrador creado con éxito.")
