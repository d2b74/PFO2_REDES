# 📝 Gestor de Tareas RESTful

Este proyecto es una **API RESTful simple** para la gestión de tareas, desarrollada con **Flask** y **SQLite**. Incluye un sistema de **autenticación básica** y un **cliente de consola interactivo** para operar con la API sin necesidad de una interfaz gráfica.

---

## 📁 Estructura del Proyecto

```

gestor-tareas/
│
├── api.py              # Servidor Flask con endpoints RESTful
├── client.py           # Cliente de consola para consumir la API
├── db.py               # Inicializa la base de datos SQLite
├── data.db             # Archivo de base de datos SQLite (generado automáticamente)
├── run.py              # Script principal que lanza toda la aplicación
├── requirements.txt    # Lista de dependencias necesarias
└── README.md           # Documentación del proyecto

````

---

## ⚙️ Instalación

1. Clona este repositorio o descarga los archivos:

   ```sh

   git clone https://github.com/Jonyls62/PFO2_REDES.git
   cd PFO2_REDES
````

2. Crea un entorno virtual (opcional pero recomendado):

   ```sh
   python -m venv venv
   source venv/bin/activate   # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:

   ```sh
   pip install -r requirements.txt
   ```

---

## 🚀 Uso

Ejecuta todo el sistema con:

```sh
python run.py
```

Este comando realiza lo siguiente:

* Inicializa la base de datos (`data.db`).
* Levanta el servidor Flask (`api.py`).
* Permite registrar y autenticar usuarios.
* Lanza el cliente de consola (`client.py`) para interactuar con la API.

---

## 🔐 Autenticación

* El sistema utiliza **autenticación básica (Basic Auth)** para proteger los endpoints sensibles.
* Los tokens o credenciales no se almacenan en el cliente.

---

## 🔧 Endpoints Principales

| Método | Endpoint      | Descripción                    | 
| ------ | ------------- | ------------------------------ | 
| POST   | `/register`   | Registrar un nuevo usuario     | 
| POST   | `/login`      | Iniciar sesión                 | 
| GET    | `/items`      | Listar todas las tareas        | 
| POST   | `/items`      | Crear una nueva tarea          | 
| PUT    | `/items/<id>` | Actualizar una tarea existente | 
| DELETE | `/items/<id>` | Eliminar una tarea             | 
| GET    | `/usuario`    | Listar usuarios registrados    | 

---

## 💻 Cliente de Consola

El cliente permite las siguientes acciones:

* Listar tareas
* Crear nuevas tareas
* Editar tareas existentes
* Eliminar tareas
* Registrar o iniciar sesión como usuario

El cliente se comunica con la API y se apaga automáticamente cuando el usuario sale del sistema.

---

## 🧪 Tecnologías Utilizadas

* Python 3
* Flask
* SQLite
* Requests
* getpass (para ocultar contraseñas en consola)

---

## 📌 Notas

* La base de datos se genera automáticamente al iniciar el sistema.
* Puedes modificar la URL base de la API dentro de `client.py` si decides desplegarla remotamente.
* Ideal para principiantes que quieren practicar APIs REST con Flask y manejo de clientes básicos.

---
---

## 🧠 Respuestas Conceptuales

### 🔒 ¿Por qué hashear contraseñas?

Hashear contraseñas es una práctica esencial para la seguridad de cualquier aplicación que maneje autenticación de usuarios. Las razones son:

- **Protección contra brechas de seguridad**: Si la base de datos se ve comprometida, los atacantes no obtendrán contraseñas en texto plano.
- **Irreversibilidad**: Un buen algoritmo de hash (como bcrypt) hace prácticamente imposible revertir el hash a la contraseña original.
- **Verificación segura**: Se puede comprobar si una contraseña ingresada es válida sin necesidad de guardar el dato original.
- **Cumplimiento de estándares**: Cumple con buenas prácticas de seguridad y normativas de protección de datos.

---

### 🗃️ Ventajas de usar SQLite en este proyecto

SQLite fue elegido por varias razones que lo hacen ideal para proyectos pequeños y medianos como este:

- ✅ **Sin configuración**: No requiere instalar ni configurar un servidor de base de datos.
- 📦 **Portabilidad**: La base entera está contenida en un único archivo (`data.db`), lo que facilita su traslado o respaldo.
- ⚡ **Ligereza**: Tiene un bajo consumo de recursos, perfecto para entornos locales o de prueba.
- 🐍 **Compatibilidad nativa**: Python incluye soporte para SQLite sin instalar librerías externas.
- 🔧 **Bajo mantenimiento**: Ideal para proyectos académicos o con una carga moderada de usuarios.
- 🚀 **Desarrollo ágil**: Permite ciclos rápidos de desarrollo y pruebas.

