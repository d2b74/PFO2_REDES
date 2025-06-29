import subprocess
import requests
import time
import os
import sys
from getpass import getpass

# Configuración por defecto
USERNAME = 'nombre'
PASSWORD = '1234'
SERVER_URL = 'http://127.0.0.1:5000'

# Permitir modificar usuario y contraseña
def prompt_user_input():
    global USERNAME, PASSWORD
    print("\n--- CREAR USUARIO ---")
    if input("¿Usar usuario personalizado? (s/N): ").lower() == 's':
        USERNAME = input("Usuario: ") or USERNAME
        PASSWORD = getpass("Contraseña: ") or PASSWORD

# Paso 1: Inicializar la base de datos
print("Inicializando base de datos...")
subprocess.run([sys.executable, 'db.py'])

# Paso 2: Levantar el servidor en segundo plano
print("Levantando servidor...")
server_process = subprocess.Popen([sys.executable, 'api.py'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Paso 3: Esperar a que el servidor esté listo
print("Esperando que el servidor esté disponible...")
for i in range(10):
    try:
        requests.get(f"{SERVER_URL}/items", auth=(USERNAME, PASSWORD), timeout=1)
        break
    except Exception:
        time.sleep(1)
else:
    print("Error: el servidor no respondió a tiempo.")
    server_process.terminate()
    sys.exit(1)

# Paso 4: Registrar usuario automáticamente
prompt_user_input()
print(f"Registrando usuario: {USERNAME}")
try:
    r = requests.post(f"{SERVER_URL}/register", json={
        'username': USERNAME,
        'password': PASSWORD
    })
    print("Respuesta del servidor:", r.json())
except Exception as e:
    print("Error al registrar usuario:", e)
    server_process.terminate()
    sys.exit(1)

# Paso 5: Lanzar cliente
print("Lanzando cliente...")
try:
    subprocess.run([sys.executable, 'client.py'])
except KeyboardInterrupt:
    print("\nCliente detenido.")

# Paso 6: Detener servidor al salir del cliente
print("Apagando servidor...")
server_process.terminate()
