from flask import Flask, render_template, request, redirect, url_for, flash
from flask.globals import request
from flask_mysqldb import MySQL

app = Flask(__name__)

# --------------------------------------------------------------------------------------------------
# ---------------------------------------- BASE DE DATOS -------------------------------------------
# --------------------------------------------------------------------------------------------------

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'calendario_flask'
mysql = MySQL(app)

# --------------------------------------------------------------------------------------------------
# ---------------------------------------- CONFIGURACIONES -----------------------------------------
# --------------------------------------------------------------------------------------------------

app.secret_key = 'mysecretkey'


@app.route('/')
def Index():
    return render_template('index.html')


# --------------------------------------------------------------------------------------------------
# ---------------------------------------- CRUD ESPACIOS ACADEMICO ---------------------------------
# --------------------------------------------------------------------------------------------------

@app.route('/espacios')
def espacios():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM espacios')
    espacios = cur.fetchall()
    return render_template('espacios/espacios.html', espacios=espacios)


@app.route('/agregar_espacio', methods=['POST'])
def agregar_espacio():
    if request.method == 'POST':
        nombre_espacio = request.form['nombre_espacio']
        semestre_espacio = request.form['semestre_espacio']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO espacios (nombre_espacio, semestre_espacio) VALUES (%s, %s)',
                    (nombre_espacio, semestre_espacio))
        mysql.connection.commit()
        flash('espacio agregado satisfactoriamente')
    return redirect(url_for('espacios'))


@app.route('/editar_espacio/<id>')
def editar_espacio(id):
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM espacios WHERE id_espacio = {id}")
    espacio = cur.fetchall()
    return render_template('espacios/editar_espacio.html', espacio=espacio[0])


@app.route('/actualizar_espacio/<id>', methods=['POST'])
def actualizar_espacio(id):
    if request.method == 'POST':
        nombre_espacio = request.form['nombre_espacio']
        semestre_espacio = request.form['semestre_espacio']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE espacios
            SET nombre_espacio = %s,
                semestre_espacio = %s
            WHERE id_espacio = %s
        """, (nombre_espacio, semestre_espacio, id))
        mysql.connection.commit()
        flash('espacio actualizado satisfactoriamente')
    return redirect(url_for('espacios'))


@app.route('/eliminar_espacio/<id>')
def eliminar_espacio(id):
    cur = mysql.connection.cursor()
    cur.execute(f"DELETE FROM espacios WHERE id_espacio = {id}")
    mysql.connection.commit()
    flash('espacio eliminado satisfactoriamente')
    return redirect(url_for('espacios'))


# --------------------------------------------------------------------------------------------------
# ---------------------------------------- CRUD ESTUDIANTES ----------------------------------------
# --------------------------------------------------------------------------------------------------

@app.route('/estudiantes')
def estudiantes():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM estudiantes')
    estudiantes = cur.fetchall()
    return render_template('estudiantes/estudiantes.html', estudiantes=estudiantes)


@app.route('/agregar_estudiante', methods=['POST'])
def agregar_estudiantes():
    if request.method == 'POST':
        identificacion_estudiante = request.form['identificacion_estudiante']
        nombres_estudiante = request.form['nombres_estudiante']
        apellidos_estudiante = request.form['apellidos_estudiante']
        telefono_estudiante = request.form['telefono_estudiante']
        email_estudiante = request.form['email_estudiante']
        semestre_estudiante = request.form['semestre_estudiante']
        
        cur = mysql.connection.cursor()
        try:
            cur.execute(
                'INSERT INTO estudiantes (identificacion_estudiante, nombres_estudiante, apellidos_estudiante, telefono_estudiante, email_estudiante, semestre_estudiante) VALUES (%s, %s, %s, %s, %s, %s)',
                (identificacion_estudiante, nombres_estudiante, apellidos_estudiante, telefono_estudiante, email_estudiante, semestre_estudiante))
            mysql.connection.commit()
            flash('estudiante agregado satisfactoriamente')
        except IOError as e:
            flash('La identificacion o el correo del estudiante ya existen')
            print(e)
    return redirect(url_for('estudiantes'))


@app.route('/editar_estudiante/<id>')
def editar_estudiante(id):
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM estudiantes WHERE id_estudiante = {id}")
    estudiante = cur.fetchall()
    return render_template('estudiantes/editar_estudiante.html', estudiante=estudiante[0])


@app.route('/actualizar_estudiante/<id>', methods=['POST'])
def actualizar_estudiante(id):
    if request.method == 'POST':
        identificacion_estudiante = request.form['identificacion_estudiante']
        nombres_estudiante = request.form['nombres_estudiante']
        apellidos_estudiante = request.form['apellidos_estudiante']
        telefono_estudiante = request.form['telefono_estudiante']
        email_estudiante = request.form['email_estudiante']
        semestre_estudiante = request.form['semestre_estudiante']
        cur = mysql.connection.cursor()
        try:
            cur.execute("""
                UPDATE estudiantes
                SET identificacion_estudiante = %s,
                    nombres_estudiante = %s,
                    apellidos_estudiante = %s,
                    telefono_estudiante = %s,
                    email_estudiante = %s,
                    semestre_estudiante = %s
                WHERE id_estudiante = %s
            """, (identificacion_estudiante, nombres_estudiante, apellidos_estudiante, telefono_estudiante, email_estudiante, semestre_estudiante, id))
            mysql.connection.commit()
            flash('estudiante actualizado satisfactoriamente')
        except:
            flash('La identificacion o el correo del estudiante ya existen')
    return redirect(url_for('estudiantes'))


@app.route('/eliminar_estudiante/<id>')
def eliminar_estudiante(id):
    cur = mysql.connection.cursor()
    cur.execute(f"DELETE FROM estudiantes WHERE id_estudiante = {id}")
    mysql.connection.commit()
    flash('estudiante eliminado satisfactoriamente')
    return redirect(url_for('estudiantes'))

# --------------------------------------------------------------------------------------------------
# ---------------------------------------- CRUD SESIONES ----------------------------------------
# --------------------------------------------------------------------------------------------------


@app.route('/asistencias')
def asistencias():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM asistencias')
    asistencias = cur.fetchall()
    cur.execute('SELECT * FROM espacios')
    espacios = cur.fetchall()
    return render_template('asistencias/asistencias.html', asistencias=asistencias, espacios=espacios)


@app.route('/agregar_asistencia', methods=['POST'])
def agregar_asistencia():
    if request.method == 'POST':
        fecha_asistencia = request.form['fecha_asistencia']
        hora_inicio_asistencia = request.form['hora_inicio_asistencia']
        hora_fin_asistencia = request.form['hora_fin_asistencia']
        espacio_id = request.form['espacio_id']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO asistencias (fecha_asistencia, hora_inicio_asistencia, hora_fin_asistencia, espacio_id) VALUES (%s, %s, %s, %s)',
                    (fecha_asistencia, hora_inicio_asistencia, hora_fin_asistencia, espacio_id))
        mysql.connection.commit()
        flash('asistencia agregada satisfactoriamente')
    return redirect(url_for('asistencias'))


@app.route('/editar_asistencia/<id>')
def editar_asistencia(id):
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM asistencias WHERE id_asistencia = {id}")
    asistencia = cur.fetchall()
    cur.execute('SELECT * FROM espacios')
    espacios = cur.fetchall()
    return render_template('asistencias/editar_asistencia.html', asistencia=asistencia[0], espacios=espacios)


@app.route('/actualizar_asistencia/<id>', methods=['POST'])
def actualizar_asistencia(id):
    if request.method == 'POST':
        fecha_asistencia = request.form['fecha_asistencia']
        hora_inicio_asistencia = request.form['hora_inicio_asistencia']
        hora_fin_asistencia = request.form['hora_fin_asistencia']
        espacio_id = request.form['espacio_id']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE asistencias
            SET fecha_asistencia = %s,
                hora_inicio_asistencia = %s,
                hora_fin_asistencia = %s,
                espacio_id = %s
            WHERE id_asistencia = %s
        """, (fecha_asistencia, hora_inicio_asistencia, hora_fin_asistencia, espacio_id, id))
        mysql.connection.commit()
        flash('asistencia actualizada satisfactoriamente')
    return redirect(url_for('asistencias'))


@app.route('/eliminar_asistencia/<id>')
def eliminar_asistencia(id):
    cur = mysql.connection.cursor()
    cur.execute(f"DELETE FROM asistencias WHERE id_asistencia = {id}")
    mysql.connection.commit()
    flash('asistencia eliminada satisfactoriamente')
    return redirect(url_for('asistencias'))

# --------------------------------------------------------------------------------------------------
# ---------------------------------------- TOMAR ASISTENCIAS ---------------------------------------
# --------------------------------------------------------------------------------------------------

@app.route('/tomar_asistencias')
def tomar_asistencias():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM asistencias')
    asistencias = cur.fetchall()
    cur.execute('SELECT * FROM espacios')
    espacios = cur.fetchall()
    return render_template('asistencias/tomar_asistencias.html', asistencias=asistencias, espacios=espacios)


@app.route('/cargar_estudiantes_asistencia/<id_asistencia>')
def cargar_estudiantes_asistencia(id_asistencia):
    cur = mysql.connection.cursor()
    #cur.execute(f"SELECT * FROM asistencias WHERE id_asistencia = {id_asistencia}")
    #asistencia = cur.fetchall()
    cur.execute('SELECT * FROM asistencias')
    asistencias = cur.fetchall()
    cur.execute('SELECT * FROM espacios')
    espacios = cur.fetchall()
    cur.execute(f"SELECT asistencia_id FROM asistencias_estudiantes AS ae INNER JOIN asistencias AS a ON ae.asistencia_id = a.id_asistencia WHERE a.id_asistencia = {id_asistencia}")
    asistencia_realizada = cur.fetchall()

    if asistencia_realizada:
        flash('La asistencia que desea cargar ya existe')
        return render_template('asistencias/tomar_asistencias.html', asistencias=asistencias, espacios=espacios)
    else:
        cur.execute(
            f"SELECT nombre_espacio FROM espacios AS e INNER JOIN asistencias AS a ON e.id_espacio = a.espacio_id WHERE a.id_asistencia = {id_asistencia}")
        nombre_espacio = cur.fetchall()
        cur.execute(
            f"SELECT semestre_espacio FROM espacios AS e INNER JOIN asistencias AS a ON e.id_espacio = a.espacio_id WHERE a.id_asistencia = {id_asistencia}")
        semestre_espacio = cur.fetchall()[0]
        cur.execute(f"SELECT * FROM estudiantes WHERE semestre_estudiante = {semestre_espacio[0]}")
        estudiantes = cur.fetchall()
        if estudiantes == ():
            flash('No hay estudiantes en el semestre del espacio academico')
        return render_template('asistencias/tomar_asistencias.html', asistencias=asistencias, espacios=espacios, estudiantes=estudiantes, id_asistencia=id_asistencia, nombre_espacio=nombre_espacio)


@app.route('/tomar_asistencia', methods=['POST'])
def tomar_asistencia():
    if request.method == 'POST':
        try:
            result = request.form.to_dict(flat=False)
            asistencia_id = result['asistencia_id'][0]
            if result.get("estudiante_asistencia"):
                for estudiante_id in result['estudiante_id']:
                    if estudiante_id in result['estudiante_asistencia']:
                        estudiante_asistencia = 1
                        cur = mysql.connection.cursor()
                        cur.execute('INSERT INTO asistencias_estudiantes (estudiante_id, asistencia_id, estudiante_asistencia) VALUES (%s, %s, %s)',
                                    (estudiante_id, asistencia_id, estudiante_asistencia))
                        mysql.connection.commit()
                    else:
                        continue
            flash('asistencia de los estudiantes agregada satisfactoriamente')
        except:
            flash('No se puede guardar sin cargar estudiantes')
    return redirect(url_for('tomar_asistencias'))

# --------------------------------------------------------------------------------------------------
# ---------------------------------------- LISTAR ASISTENCIAS ---------------------------------------
# --------------------------------------------------------------------------------------------------


@app.route('/listar_asistencias')
def listar_asistentas():
    #lista_asistencias2 = lista_asistencias()
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM asistencias')
    asistencias = cur.fetchall()
    cur.execute('SELECT * FROM espacios')
    espacios = cur.fetchall()
    return render_template('asistencias/listar_asistencias.html', asistencias=asistencias, espacios=espacios)


@app.route('/listar_estudiantes/<asistencia_id>')
def listar_estudiantes(asistencia_id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM asistencias')
    asistencias = cur.fetchall()
    cur.execute('SELECT * FROM espacios')
    espacios = cur.fetchall()
    cur.execute(f"SELECT estudiante_id FROM asistencias_estudiantes WHERE asistencia_id = {asistencia_id}")
    estudiantes_ids = cur.fetchall()
    lista_estudiantes = []
    for estudiante_id in estudiantes_ids:
        cur.execute(f"SELECT * FROM estudiantes WHERE id_estudiante = {estudiante_id[0]}")
        estudiante = cur.fetchall()
        lista_estudiantes.append(estudiante[0])
    if lista_estudiantes == []:
            flash('La lista no tiene estudiantes')
    return render_template('asistencias/listar_asistencias.html', asistencias=asistencias, espacios=espacios, lista_estudiantes=lista_estudiantes, asistencia_id=asistencia_id)


@app.route('/eliminar_lista_asistencia/<asistencia_id>')
def eliminar_lista_asistencia(asistencia_id):
    cur = mysql.connection.cursor()
    
    cur.execute(
        f"DELETE FROM asistencias_estudiantes WHERE asistencia_id = {asistencia_id}")
    mysql.connection.commit()
    flash('asistencia eliminada satisfactoriamente')
    return redirect(url_for('listar_asistentas'))


# --------------------------------------------------------------------------------------------------
# ---------------------------------------- MAIN ----------------------------------------------------
# --------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    app.run(port=3000, debug=True)