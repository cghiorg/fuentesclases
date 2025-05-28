from werkzeug.security import generate_password_hash, check_password_hash

# Registro del usuario
password_original = input("Elegí una contraseña: ")
hash_generado = generate_password_hash(password_original)
print("Contraseña encriptada:", hash_generado)

# Simulamos un login
password_login = input("Ingresá tu contraseña: ")

if check_password_hash(hash_generado, password_login):
    print("✅ Acceso concedido.")
else:
    print("❌ Contraseña incorrecta.")
