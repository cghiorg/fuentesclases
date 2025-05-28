from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Configuración de la base de datos SQLite
engine = create_engine('sqlite:///usuarios.db', echo=True)
Base = declarative_base()

# Modelo de datos
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    email = Column(String)

# Crear la tabla en la base de datos
Base.metadata.create_all(engine)

# Crear una sesión para interactuar con la base
Session = sessionmaker(bind=engine)
session = Session()

# Insertar usuarios
usuario1 = Usuario(nombre="Ana", email="ana@mail.com")
usuario2 = Usuario(nombre="Carlos", email="carlos@mail.com")

session.add(usuario1)
session.add(usuario2)
session.commit()

# Consultar usuarios
usuarios = session.query(Usuario).all()
for u in usuarios:
    print(f"{u.id} - {u.nombre} ({u.email})")

# Cerrar sesión
session.close()
