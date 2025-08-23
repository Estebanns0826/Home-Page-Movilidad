from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from flask_cors import CORS
import sqlite3
from datetime import datetime
import os
import psycopg2
from psycopg2 import Error

app = Flask(__name__)
app.secret_key = 'supersecretkey'
CORS(app)  # Habilita CORS para toda la aplicación

# Ruta de la base de datos
DATABASE = 'database.db'
DATA_BASE_EQUIPOS = 'registro_equipos.db'

# Credenciales de login
USUARIO = 'admin'
CLAVE = '1234'

# Función para conectar a la base de datos de equipos
def get_db_connection_equipos():
    conn = sqlite3.connect(DATA_BASE_EQUIPOS)
    conn.row_factory = sqlite3.Row
    return conn

# Crear la base de datos de equipos si no existe
def crear_base_datos_equipos():
    conn = get_db_connection_equipos()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS equipos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            direccion TEXT,
            tipo_equipo TEXT,
            tarjetas_entrada_equipo TEXT,
            tipo_movimiento TEXT,
            nombre_entrega TEXT,
            nombre_recibe TEXT,
            descripcion_de_fallo TEXT,
            fecha_notificacion TEXT DEFAULT CURRENT_TIMESTAMP,
            fotografia_evidencia TEXT,
            estado_actual TEXT,
            fecha_revision DATE,
            nombre_revisor TEXT,
            motivo_reparacion TEXT,
            descripcion_revision TEXT,
            nombre_reparador TEXT,
            diagnostico_reparacion TEXT,
            insumos_usados TEXT,
            fecha_reparacion DATE,
            nombre_entrega_salida TEXT,
            nombre_recibe_salida TEXT,
            descripcion_salida TEXT,
            imagen_salida TEXT,
            fecha_entrega DATE
        )
    ''')




# Ruta para obtener datos de equipos pendientes (estado_actual != 'entregado')
@app.route('/api/datos_equipos_pendientes', methods=['GET'])
def datos_equipos_pendientes():
    filtro = request.args.get('filtro')
    anio = request.args.get('anio')
    mes = request.args.get('mes')
    semana = request.args.get('semana')
    dia = request.args.get('dia')
    fechaInicio = request.args.get('fechaInicio')
    fechaFin = request.args.get('fechaFin')

    query = """
        SELECT direccion, estado_actual, motivo_reparacion, descripcion_revision, fecha_notificacion
        FROM equipos
        WHERE estado_actual != 'Entregado'
    """
    conditions = []
    parameters = []

    if filtro == 'anio' and anio:
        conditions.append("strftime('%Y', fecha_revision) = ?")
        parameters.append(str(anio))
    elif filtro == 'mes' and anio and mes:
        conditions.append("strftime('%Y', fecha_revision) = ?")
        conditions.append("strftime('%m', fecha_revision) = ?")
        parameters.extend([str(anio), f"{int(mes):02d}"])
    elif filtro == 'semana' and anio and mes and semana:
        conditions.append("strftime('%Y', fecha_revision) = ?")
        conditions.append("strftime('%m', fecha_revision) = ?")
        conditions.append("strftime('%W', fecha_revision) = ?")
        parameters.extend([str(anio), f"{int(mes):02d}", f"{int(semana):02d}"])
    elif filtro == 'dia' and dia:
        conditions.append("fecha_revision = ?")
        parameters.append(dia)
    elif filtro == 'fecha' and fechaInicio and fechaFin:
        conditions.append("fecha_revision BETWEEN ? AND ?")
        parameters.extend([fechaInicio, fechaFin])

    if conditions:
        query += " AND " + " AND ".join(conditions)

    conn = get_db_connection_equipos()
    cursor = conn.cursor()
    cursor.execute(query, parameters)
    equipos_pendientes = cursor.fetchall()
    conn.close()

    datos = {
        'direcciones': [],
        'counts': [],
        'equipos': []
    }

    direcciones_contadas = {}
    for equipo in equipos_pendientes:
        datos['equipos'].append({
            'direccion': equipo['direccion'],
            'estado_actual': equipo['estado_actual'],
            'motivo_reparacion': equipo['motivo_reparacion'],
            'descripcion_revision': equipo['descripcion_revision'],
            'fecha_notificacion': equipo['fecha_notificacion']
        })
        if equipo['direccion']:
            direcciones_contadas[equipo['direccion']] = direcciones_contadas.get(equipo['direccion'], 0) + 1

    datos['direcciones'] = list(direcciones_contadas.keys())
    datos['counts'] = list(direcciones_contadas.values())

    return jsonify(datos)

# Ruta principal para el dashboard
@app.route('/')
def home():
    if 'usuario' in session:
        return render_template('menu.html', usuario=session['usuario'])
    return redirect(url_for('login'))

# Ruta para login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        clave = request.form['clave']
        if usuario == USUARIO and clave == CLAVE:
            session['usuario'] = usuario
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Usuario o contraseña incorrectos')
    return render_template('login.html')

# Ruta para logout
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

# Ruta para obtener coordenadas desde la base de datos
@app.route('/get_location', methods=['POST'])
def get_location():
    data = request.get_json()
    direccion = data.get('direccion')
    if not direccion:
        return jsonify({'success': False, 'error': 'Dirección no proporcionada'})

    try:
        conn = sqlite3.connect('intersecciones.db')
        cursor = conn.cursor()
        cursor.execute("SELECT Latitud, Longitud FROM intersecciones_semaforizadas WHERE direccion = ?", (direccion,))
        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            return jsonify({'success': True, 'coordenadas': {'lat': resultado[0], 'lng': resultado[1]}})
        else:
            return jsonify({'success': False, 'error': 'Ubicación no encontrada'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# Ruta para obtener datos de equipos para el dashboard
@app.route('/api/datos_equipos', methods=['GET'])
def datos_equipos():
    filtro = request.args.get('filtro')
    anio = request.args.get('anio')
    mes = request.args.get('mes')
    semana = request.args.get('semana')
    dia = request.args.get('dia')
    fechaInicio = request.args.get('fechaInicio')
    fechaFin = request.args.get('fechaFin')

    query = """
        SELECT direccion, tipo_equipo, tipo_movimiento, estado_actual, nombre_revisor,
               fecha_revision, motivo_reparacion, fecha_notificacion, fecha_entrega
        FROM equipos
    """
    conditions = []
    parameters = []

    if filtro == 'anio' and anio:
        conditions.append("strftime('%Y', fecha_revision) = ?")
        parameters.append(str(anio))
    elif filtro == 'mes' and anio and mes:
        conditions.append("strftime('%Y', fecha_revision) = ?")
        conditions.append("strftime('%m', fecha_revision) = ?")
        parameters.extend([str(anio), f"{int(mes):02d}"])
    elif filtro == 'semana' and anio and mes and semana:
        conditions.append("strftime('%Y', fecha_revision) = ?")
        conditions.append("strftime('%m', fecha_revision) = ?")
        conditions.append("strftime('%W', fecha_revision) = ?")
        parameters.extend([str(anio), f"{int(mes):02d}", f"{int(semana):02d}"])
    elif filtro == 'dia' and dia:
        conditions.append("fecha_revision = ?")
        parameters.append(dia)
    elif filtro == 'fecha' and fechaInicio and fechaFin:
        conditions.append("fecha_revision BETWEEN ? AND ?")
        parameters.extend([fechaInicio, fechaFin])

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    conn = get_db_connection_equipos()
    cursor = conn.cursor()
    cursor.execute(query, parameters)
    equipos = cursor.fetchall()
    conn.close()

    datos = {
        'tiposEquipo': [],
        'motivoReparacion': [],
        'direcciones': [],
        'fechasRevision': [],
        'tiemposRespuesta': []
    }

    for equipo in equipos:
        if equipo['tipo_equipo']:
            datos['tiposEquipo'].append(equipo['tipo_equipo'])
        if equipo['motivo_reparacion']:
            datos['motivoReparacion'].append(equipo['motivo_reparacion'])
        if equipo['direccion']:
            datos['direcciones'].append(equipo['direccion'])
        if equipo['fecha_revision']:
            datos['fechasRevision'].append(equipo['fecha_revision'])
        if equipo['fecha_notificacion'] and equipo['fecha_entrega']:
            try:

                fecha_notificacion = datetime.strptime(equipo['fecha_notificacion'], '%Y-%m-%d')
                fecha_entrega = datetime.strptime(equipo['fecha_entrega'], '%Y-%m-%d')
                datos['tiemposRespuesta'].append((fecha_entrega - fecha_notificacion).days)
            except ValueError:
                pass

    return jsonify(datos)

# Ruta para renderizar la página del dashboard
@app.route('/report_lab', methods=['GET'])
def estadisticas_equipos():
    return render_template('report_lab.html')

# Ruta para renderizar la página del dashboard
@app.route('/report_tickets', methods=['GET'])
def estadisticas_tickets():
    return render_template('report_tickets.html')

# Inicializar la base de datos de equipos
crear_base_datos_equipos()





def get_db_connection():
    conn = psycopg2.connect(
        host="38.50.50.166",
        port="5432",
        database="tickets",
        user="postgres",
        password="1ts2025"  # Reemplaza con la contraseña real
    )
    return conn




@app.route('/report')
def report():
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        
        # Consulta SQL para calcular los datos por categoría
        query = """
        SELECT 
            categoria, 
            SUM(CASE WHEN estado = 'Operando' THEN 1 ELSE 0 END) AS funcionando, 
            SUM(CASE WHEN estado = 'Apagada' AND causa_id = 38 THEN 1 ELSE 0 END) AS vandalizadas, 
            SUM(CASE WHEN estado = 'Apagada' AND (causa_id IS NULL OR causa_id != 38) THEN 1 ELSE 0 END) AS apagadas, 
            COUNT(id) AS totales, 
            (COUNT(id) * 100.0 / (SELECT COUNT(id) FROM intersecciones)) AS porcentaje 
        FROM intersecciones 
        GROUP BY categoria 
        ORDER BY totales DESC;
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        
        # Calcular totales generales
        total_query = """
        SELECT 
            SUM(CASE WHEN estado = 'Operando' THEN 1 ELSE 0 END) AS funcionando, 
            SUM(CASE WHEN estado = 'Apagada' AND causa_id = 38 THEN 1 ELSE 0 END) AS vandalizadas, 
            SUM(CASE WHEN estado = 'Apagada' AND (causa_id IS NULL OR causa_id != 38) THEN 1 ELSE 0 END) AS apagadas, 
            COUNT(id) AS totales 
        FROM intersecciones;
        """
        cursor.execute(total_query)
        total_row = cursor.fetchone()
        totales = total_row[3]  # Total general para el porcentaje
        
        data = [
            {
                "categoria": row[0],
                "funcionando": row[1],
                "vandalizadas": row[2],
                "apagadas": row[3],
                "totales": row[4],
                "porcentaje": round(row[5], 2) if totales > 0 else 0.0
            }
            for row in rows
        ]
        
        # Agregar fila de totales
        data.append({
            "categoria": "<strong>Total</strong>",
            "funcionando": total_row[0],
            "vandalizadas": total_row[1],
            "apagadas": total_row[2],
            "totales": total_row[3],
            "porcentaje": 100.00
        })
        
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        data = []
        
    finally:
        cursor.close()
        connection.close()
        
    return render_template('report.html', data=data)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)