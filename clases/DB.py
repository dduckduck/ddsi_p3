import os
import oracledb
from flask import Flask, render_template, request, url_for, redirect

cs = "oracle0.ugr.es:1521/practbd.oracle0.ugr.es"
usr = pwd = os.environ['DB_USERNAME']

app = Flask(__name__)

try:
    conn = oracledb.connect(user=usr,password=pwd,dsn=cs)
except Exception as e:
    print(f"Error al establecer conexión:{e}")
    #:exit(-1)


@app.route('/')
def home():
    #display the home 
    return render_template('home.html')

@app.route('/cliente/')
def index():
    cur = conn.cursor()
    cliente = "Sin datos"
    try:
        cur.execute('SELECT * FROM Cliente')
        cliente = cur.fetchall()
    except Exception as e:
        print(f"Error al consultar clientes: {e}")
    return render_template('cliente.html', cliente=cliente)


@app.route('/cliente/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        #datos de cliente
        cur = conn.cursor()
        #Rollback seria conveniente
        try: 
            #insertar datos para nuevo cliente 
            cur.execute() 
        except Exception as e:
            print(f"Error al insertar cliente {e}")
        return redirect(url_for('cliente'))

    return render_template('cliente_new.html')


@app.route('/propiedad/')
def index():
    cur = conn.cursor()
    propiedad = "Sin datos"
    try:
        cur.execute('SELECT * FROM Propiedad')
        propiedad = cur.fetchall()
    except Exception as e:
        print(f"Error al consultar pro`popriedad: {e}")
    return render_template('propiedad.html', propiedad=propiedad)


@app.route('/propiedad/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        Ref_catrastal = request.form['Ref_catrastal']
        Tamano = int(request.form['Tamanno'])
        N_habitaciones = int(request.form['N_habitaciones'])
        N_banos = int(request.form['N_banos'])
        Garaje = request.form['Garaje']
        Terraza = request.form['Terraza']
        Certificado = request.form['Certificado']
        Localizacion = request.form['Localizacion']
        CP = request.form['CP']
        Estado = request.form['Estado']
        Disponibilidad = request.form['Disponibilidad']
        DNI_propietario = request.form['DNI_propietario']

        cur = conn.cursor()
        try: 
            cur.execute('INSERT INTO Propiedad(Ref_catastral, Tamano, N_habitaciones, N_banos, Garaje, Terraza, Certificado, Localizacion, CP, Estado, Disponibilidad, DNI_propietario)'
                        'VALUES (:1, :2, :3 , :4, :5, :6, :7, :8, :9, :10, :11, :12)', 
                        (Ref_catrastal, Tamano, N_habitaciones, N_banos, Garaje, Terraza, Certificado, Localizacion, CP, Estado, Disponibilidad, DNI_propietario))
            
            conn.comit()
        except Exception as e:
            print(f"Error al insertar propiedad {e}")
        return redirect(url_for('propiedad'))

    return render_template('propiedad_new.html')

#COMPRA / VENTA 
@app.route('/cliente/')
def index():
    cur = conn.cursor()
    cliente = "Sin datos"
    try:
        cur.execute('SELECT * FROM Cliente')
        cliente = cur.fetchall()
    except Exception as e:
        print(f"Error al consultar clientes: {e}")
    return render_template('cliente.html', cliente=cliente)


@app.route('/cliente/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        #datos de cliente
        cur = conn.cursor()
        #Rollback seria conveniente
        try: 
            conn.execute()
            #insertar datos para nuevo cliente 
        except Exception as e:
            print(f"Error al insertar cliente {e}")
        return redirect(url_for('cliente'))

    return render_template('cliente_new.html')

#SERVICIO 
@app.route('/cliente/')
def index():
    cur = conn.cursor()
    cliente = "Sin datos"
    try:
        cur.execute('SELECT * FROM Cliente')
        cliente = cur.fetchall()
    except Exception as e:
        print(f"Error al consultar clientes: {e}")
    return render_template('cliente.html', cliente=cliente)


@app.route('/cliente/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        #datos de cliente
        cur = conn.cursor()
        #Rollback seria conveniente
        try: 
            conn.execute()
            #insertar datos para nuevo cliente 
        except Exception as e:
            print(f"Error al insertar cliente {e}")
        return redirect(url_for('cliente'))

    return render_template('cliente_new.html')
