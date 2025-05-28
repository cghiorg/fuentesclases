# ------------------------------
# 1. Ejecutable simple (modo consola)
# ------------------------------
# Empaqueta el script y deja la consola visible (útil si usás print())
# Comando:
# pyinstaller app.py

# ------------------------------
# 2. Ejecutable sin consola (modo ventana)
# ------------------------------
# Ideal para aplicaciones gráficas como Flask o Tkinter.
# No aparece la ventana negra de la consola.
# Comando:
# pyinstaller --noconsole app.py

# ------------------------------
# 3. Ejecutable como archivo único
# ------------------------------
# Genera un solo archivo .exe (más portable).
# Puede tardar más en iniciar porque descomprime al ejecutar.
# Comando:
# pyinstaller --onefile app.py

# ------------------------------
# 4. Incluir carpetas (como templates y static en Flask)
# ------------------------------
# Flask necesita estas carpetas para funcionar correctamente.
# En Windows se usa el símbolo ; y en Linux/Mac se usa :
# Comando en Windows:
# pyinstaller --add-data "templates;templates" --add-data "static;static" app.py
# Comando en Linux/Mac:
# pyinstaller --add-data "templates:templates" --add-data "static:static" app.py

# ------------------------------
# 5. Comando combinado: todo junto
# ------------------------------
# Un solo archivo, sin consola, incluyendo carpetas esenciales para Flask
# Comando:
# pyinstaller --onefile --noconsole --add-data "templates;templates" --add-data "static;static" app.py

# ------------------------------
# 6. Usar archivo .spec (configuración personalizada)
# ------------------------------
# 1. Generá el archivo de especificaciones:
#    pyinstaller app.py
# 2. Editá el archivo generado: app.spec (para agregar icono, datos, ocultar consola, etc.)
# 3. Ejecutá PyInstaller usando:
#    pyinstaller app.spec

# ------------------------------
# 7. Cambiar el icono del ejecutable (solo Windows)
# ------------------------------
# Necesitás un archivo .ico
# Comando:
# pyinstaller --onefile --noconsole --icon=icono.ico app.py

# ------------------------------
# 8. Agregar archivos adicionales (como una base de datos SQLite)
# ------------------------------
# Comando:
# pyinstaller --add-data "data.db;." app.py
# Esto guarda "data.db" en el mismo directorio del ejecutable.