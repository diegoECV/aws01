

from flask import Flask, render_template, redirect, url_for, request, session, flash
import os
import pymysql

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Cambia esto en producción

# Configuración de la base de datos
DB_HOST = os.getenv('DB_HOST', 'aws-ges.c506266wsgbx.us-east-1.rds.amazonaws.com')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'diego1416')
DB_NAME = os.getenv('DB_NAME', 'sistema_ventas')

def get_db_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )

# Login
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM usuarios WHERE username=%s AND password=%s', (username, password))
            user = cursor.fetchone()
        conn.close()
        if user:
            session['user_id'] = user['id']
            return redirect(url_for('formulario'))
        else:
            flash('Usuario o contraseña incorrectos')
    return render_template('index.html')

# Formulario para captar datos
@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if 'user_id' not in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        dni_ruc = request.form['dni_ruc']
        nombres = request.form['nombres']
        telefono = request.form['telefono']
        correo = request.form['correo']
        direccion = request.form['direccion']
        estado = request.form.get('estado', 1)
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute('''INSERT INTO clientes (dni_ruc, nombres, telefono, correo, direccion, estado)
                              VALUES (%s, %s, %s, %s, %s, %s)''',
                           (dni_ruc, nombres, telefono, correo, direccion, estado))
            conn.commit()
        conn.close()
        flash('Cliente registrado exitosamente')
        return redirect(url_for('tabla'))
    return render_template('formulario.html')


# Visualización de datos en tabla
@app.route('/tabla')
def tabla():
    if 'user_id' not in session:
        return redirect(url_for('index'))
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes')
        clientes = cursor.fetchall()
    conn.close()
    return render_template('tabla.html', clientes=clientes)

# Editar cliente (mostrar formulario con datos actuales)
@app.route('/editar/<int:id>', methods=['GET'])
def editar(id):
    if 'user_id' not in session:
        return redirect(url_for('index'))
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes WHERE id=%s', (id,))
        cliente = cursor.fetchone()
    conn.close()
    if not cliente:
        flash('Cliente no encontrado')
        return redirect(url_for('tabla'))
    return render_template('formulario.html', cliente=cliente, editar=True)

# Actualizar cliente (procesar edición)
@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    if 'user_id' not in session:
        return redirect(url_for('index'))
    dni_ruc = request.form['dni_ruc']
    nombres = request.form['nombres']
    telefono = request.form['telefono']
    correo = request.form['correo']
    direccion = request.form['direccion']
    estado = request.form.get('estado', 1)
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute('''UPDATE clientes SET dni_ruc=%s, nombres=%s, telefono=%s, correo=%s, direccion=%s, estado=%s WHERE id=%s''',
                       (dni_ruc, nombres, telefono, correo, direccion, estado, id))
        conn.commit()
    conn.close()
    flash('Cliente actualizado exitosamente')
    return redirect(url_for('tabla'))

# Eliminar cliente
@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    if 'user_id' not in session:
        return redirect(url_for('index'))
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute('DELETE FROM clientes WHERE id=%s', (id,))
        conn.commit()
    conn.close()
    flash('Cliente eliminado exitosamente')
    return redirect(url_for('tabla'))

# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
