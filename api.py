from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
import sqlite3
import bcrypt

app = Flask(__name__)
auth = HTTPBasicAuth()

def get_db():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    return conn

@auth.verify_password
def verify_password(username, password):
    conn = get_db()
    user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
    conn.close()
    if user and bcrypt.checkpw(password.encode(), user['password'].encode()):
        return username
    return None

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    try:
        conn = get_db()
        conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Usuario registrado'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Usuario ya existe'}), 400

@app.route('/items', methods=['GET'])
@auth.login_required
def get_items():
    conn = get_db()
    items = conn.execute('SELECT * FROM items').fetchall()
    conn.close()
    return jsonify([dict(item) for item in items])

@app.route('/items', methods=['POST'])
@auth.login_required
def create_item():
    data = request.json
    name = data.get('name')
    description = data.get('description', '')
    conn = get_db()
    conn.execute('INSERT INTO items (name, description) VALUES (?, ?)', (name, description))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Item creado'}), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
@auth.login_required
def update_item(item_id):
    data = request.json
    name = data.get('name')
    description = data.get('description', '')
    conn = get_db()
    conn.execute('UPDATE items SET name = ?, description = ? WHERE id = ?', (name, description, item_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Item actualizado'})

@app.route('/items/<int:item_id>', methods=['DELETE'])
@auth.login_required
def delete_item(item_id):
    conn = get_db()
    conn.execute('DELETE FROM items WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Item eliminado'})

if __name__ == '__main__':
    app.run(debug=True)