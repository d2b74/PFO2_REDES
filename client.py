import requests
from getpass import getpass

API_URL = 'http://127.0.0.1:5000'

def login():
    username = input('Usuario: ')
    password = getpass('Contraseña: ')
    return (username, password)

def show_menu():
    print("\n1. Listar items")
    print("2. Crear item")
    print("3. Actualizar item")
    print("4. Eliminar item")
    print("5. Salir")

def main():
    print("Cliente de consola para la API REST")
    auth = login()
    while True:
        show_menu()
        choice = input("Opción: ")
        if choice == '1':
            r = requests.get(f"{API_URL}/items", auth=auth)
            print(r.json())
        elif choice == '2':
            name = input("Nombre: ")
            desc = input("Descripción: ")
            r = requests.post(f"{API_URL}/items", json={'name': name, 'description': desc}, auth=auth)
            print(r.json())
        elif choice == '3':
            item_id = input("ID del item a actualizar: ")
            name = input("Nuevo nombre: ")
            desc = input("Nueva descripción: ")
            r = requests.put(f"{API_URL}/items/{item_id}", json={'name': name, 'description': desc}, auth=auth)
            print(r.json())
        elif choice == '4':
            item_id = input("ID del item a eliminar: ")
            r = requests.delete(f"{API_URL}/items/{item_id}", auth=auth)
            print(r.json())
        elif choice == '5':
            break
        else:
            print("Opción inválida.")

if __name__ == '__main__':
    main()