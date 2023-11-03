import string
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox

# Importa la biblioteca cryptography después de la instalación
from cryptography.fernet import Fernet
import os
import pickle
import subprocess

# Comando para instalar la biblioteca cryptography
comando_instalacion = "pip install cryptography"

# Intenta instalar cryptography
try:
    subprocess.run(comando_instalacion, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print("Error al instalar cryptography:", e)
    exit(1)

directorio_actual = os.path.dirname(os.path.abspath(__file__))
archivo_contrasenas_bin = os.path.join(directorio_actual, "contrasenas.bin")
archivo_contrasenas_cifrado = os.path.join(directorio_actual, "contrasenas_cifrado.bin")
archivo_clave = os.path.join(directorio_actual, "clave_maestra.key")

# Contraseña maestra predeterminada
contrasena_descifrado = "4237alfonso"

# Crear un objeto Fernet con una clave generada o almacenada previamente
if os.path.exists(archivo_clave):
    with open(archivo_clave, "rb") as clave_file:
        clave_maestra = clave_file.read()
else:
    clave_maestra = Fernet.generate_key()
    with open(archivo_clave, "wb") as clave_file:
        clave_file.write(clave_maestra)

fernet = Fernet(clave_maestra)

def generar_contrasena(longitud, incluir_numeros, incluir_mayusculas, incluir_minusculas, incluir_especiales):
    caracteres = ""
    if incluir_numeros:
        caracteres += string.digits
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_especiales:
        caracteres += string.punctuation

    contrasena_generada = ''.join(random.choice(caracteres) for _ in range(longitud))
    contrasena_cifrada = fernet.encrypt(contrasena_generada.encode())
    return contrasena_cifrada

def guardar_contrasena(usuario, contrasena):
    contrasenas = leer_contrasenas()
    usuario_existente = False
    for i, (u, _) in enumerate(contrasenas):
        if u == usuario:
            contrasenas[i] = (usuario, contrasena)
            usuario_existente = True
            break
    if not usuario_existente:
        contrasenas.append((usuario, contrasena))

    escribir_contrasenas(contrasenas)
    print("Contraseña guardada con éxito.")

def leer_contrasenas():
    try:
        with open(archivo_contrasenas_cifrado, "rb") as archivo:
            contrasenas_cifradas = archivo.read()
            contrasenas = pickle.loads(fernet.decrypt(contrasenas_cifradas))
        return contrasenas
    except (FileNotFoundError, EOFError):
        return []

def escribir_contrasenas(contrasenas):
    contrasenas_cifradas = fernet.encrypt(pickle.dumps(contrasenas))
    with open(archivo_contrasenas_cifrado, "wb") as archivo:
        archivo.write(contrasenas_cifradas)

def cambiar_contraseña_maestra(nueva_contraseña_maestra):
    global contrasena_descifrado
    contrasena_actual = input("Introduce la contraseña maestra actual: ")
    if contrasena_actual == contrasena_descifrado:
        contrasena_descifrado = nueva_contraseña_maestra
        print("Contraseña maestra cambiada con éxito.")
    else:
        print("Contraseña maestra incorrecta. No se puede cambiar la contraseña maestra.")

def descifrar_contraseña():
    contrasena_ingresada = input("Ingrese la contraseña maestra para descifrar el archivo: ")
    if contrasena_ingresada == contrasena_descifrado:
        contrasenas = leer_contrasenas()
        if not contrasenas:
            print("No se encontraron contraseñas almacenadas.")
        else:
            for usuario, contrasena in contrasenas:
                print(f"Usuario/Correo: {usuario}")
                contrasena_descifrada = fernet.decrypt(contrasena).decode()
                print(f"Contraseña descifrada: {contrasena_descifrada}")
                print()
    else:
        print("Contraseña maestra incorrecta. No se pueden descifrar las contraseñas.")

class PasswordManagerUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Administrador de Contraseñas')
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.label = QLabel('Contraseña Maestra:')
        self.password_input = QLineEdit()
        self.login_button = QPushButton('Iniciar Sesión')

        self.login_button.clicked.connect(self.login)

        layout.addWidget(self.label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.central_widget.setLayout(layout)

    def login(self):
        global contrasena_descifrado
        contrasena_ingresada = self.password_input.text()
        if contrasena_ingresada == contrasena_descifrado:
            self.show_menu()
            self.password_input.clear()
        else:
            QMessageBox.warning(self, 'Error', 'Contraseña maestra incorrecta.')
            self.password_input.clear()

    def show_menu(self):
        self.menu_widget = QWidget(self)
        layout = QVBoxLayout()

        generate_button = QPushButton('Generar Contraseña')
        decrypt_button = QPushButton('Descifrar Contraseñas')
        change_password_button = QPushButton('Cambiar Contraseña Maestra')
        exit_button = QPushButton('Salir')

        generate_button.clicked.connect(self.generate_password)
        decrypt_button.clicked.connect(self.decrypt_passwords)
        change_password_button.clicked.connect(self.change_master_password)
        exit_button.clicked.connect(self.close)

        layout.addWidget(generate_button)
        layout.addWidget(decrypt_button)
        layout.addWidget(change_password_button)
        layout.addWidget(exit_button)

        self.menu_widget.setLayout(layout)
        self.setCentralWidget(self.menu_widget)

    def generate_password(self):
        usuario = input("Ingrese su usuario/correo: ")
        longitud = int(input("Longitud de la contraseña: "))
        incluir_numeros = input("¿Incluir números? (S/N): ").strip().lower() == "s"
        incluir_mayusculas = input("¿Incluir letras mayúsculas? (S/N): ").strip().lower() == "s"
        incluir_minusculas = input("¿Incluir letras minúsculas? (S/N): ").strip().lower() == "s"
        incluir_especiales = input("¿Incluir caracteres especiales? (S/N): ").strip().lower() == "s"

        contrasena = generar_contrasena(longitud, incluir_numeros, incluir_mayusculas, incluir_minusculas, incluir_especiales)
        guardar_contrasena(usuario, contrasena)

    def decrypt_passwords(self):
        contrasena_ingresada = input("Ingrese la contraseña maestra para descifrar el archivo: ")
        if contrasena_ingresada == contrasena_descifrado:
            contrasenas = leer_contrasenas()
            if not contrasenas:
                print("No se encontraron contraseñas almacenadas.")
            else:
                for usuario, contrasena in contrasenas:
                    print(f"Usuario/Correo: {usuario}")
                    contrasena_descifrada = fernet.decrypt(contrasena).decode()
                    print(f"Contraseña descifrada: {contrasena_descifrada}")
                    print()
        else:
            print("Contraseña maestra incorrecta. No se pueden descifrar las contraseñas.")

    def change_master_password(self):
        nueva_contraseña_maestra = input("Introduce la nueva contraseña maestra: ")
        cambiar_contraseña_maestra(nueva_contraseña_maestra)

def main():
    app = QApplication([])
    window = PasswordManagerUI()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
