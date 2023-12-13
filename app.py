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
def index():
    cur = conn.cursor()
    books = "Sin datos"
    try:
        cur.execute('SELECT * FROM books')
        books = cur.fetchall()
    except Exception as e:
        print(f"Error al consultar libros: {e}")
    return render_template('index.html', books=books)




@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        pages_num = int(request.form['pages_num'])
        review = request.form['review']
        
        cur = conn.cursor()
        #Rollback seria conveniente
        try: 
            cur.execute('INSERT INTO books (title, author, pages_num, review)'
                        'VALUES (:1, :2, :3, :4)',
                    (title, author, pages_num, review))
            conn.commit()
        except Exception as e:
            print(f"Error al insertar libros {e}")
        return redirect(url_for('index'))

    return render_template('create.html')
