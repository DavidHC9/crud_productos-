from flask import Flask, request, jsonify, render_template
import sqlite3
import os

app = Flask(__name__)

DATABASE = os.path.join(os.path.dirname(__file__), 'productos.db')

def init_db():
    with app.app_context():
        db = sqlite3.connect(DATABASE)
        db.execute('''CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            Nota REAL NOT NULL,
            Materia TEXT)''')
        db.commit()

def get_db():
    return sqlite3.connect(DATABASE)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/productos', methods=['GET', 'POST'])
def productos():
    db = get_db()
    if request.method == 'POST':
        data = request.get_json()
        db.execute('INSERT INTO productos (nombre, Nota, Materia) VALUES (?, ?, ?)',
                   [data['nombre'], data['Nota'], data['Materia']])
        db.commit()
        return jsonify({"mensaje": "Nota guardado correctamente"})
    cursor = db.execute('SELECT * FROM productos')
    productos = [dict(id=row[0], nombre=row[1], Nota=row[2], Materia=row[3]) for row in cursor.fetchall()]
    return jsonify(productos)

@app.route('/productos/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def producto_id(id):
    db = get_db()
    if request.method == 'GET':
        cursor = db.execute('SELECT * FROM productos WHERE id = ?', [id])
        row = cursor.fetchone()
        if row:
            return jsonify(dict(id=row[0], nombre=row[1], Nota=row[2], Materia=row[3]))
        else:
            return jsonify({"error": "Nota no encontrado"}), 404

    elif request.method == 'PUT':
        data = request.get_json()
        db.execute('UPDATE productos SET nombre = ?, Nota = ?, Materia = ? WHERE id = ?',
                   [data['nombre'], data['Nota'], data['Materia'], id])
        db.commit()
        return jsonify({"mensaje": "Nota actualizado"})

    elif request.method == 'DELETE':
        db.execute('DELETE FROM productos WHERE id = ?', [id])
        db.commit()
        return jsonify({"mensaje": "Nota eliminado"})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)