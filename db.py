import os
import oracledb

cs = "oracle0.ugr.es:1521/practbd.oracle0.ugr.es"
usr = pwd = os.environ['DB_USERNAME']

try:
    conn = oracledb.connect(user=usr,password=pwd,dsn=cs)
except Exception as e:
    print(f"Error al establecer conexión:{e}")
    #:exit(-1)

cur = conn.cursor()

# Crear tabla de libros 
try:
	cur.execute('CREATE TABLE books (id integer GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1) PRIMARY KEY,'
                                 'title varchar (150) NOT NULL,'
                                 'author varchar (50) NOT NULL,'
                                 'pages_num integer NOT NULL,'
                                 'review varchar2 (150),'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP)'
                                 )
except Exception as e:
	print(f"Error: {e}")

# Insertar datos en la tabla 
try:
	cur.execute('INSERT INTO books (title, author, pages_num, review)'
		    'VALUES (:1, :2, :3, :4)',
		    ('A Tale of Two Cities',
		     'Charles Dickens',
		     489,
		     'A great classic!')
		    )
except Exception as e:
	print(f"Error: {e}")

try:
	cur.execute('INSERT INTO books (title, author, pages_num, review)'
		    'VALUES (:1, :2, :3, :4)',
		    ('Anna Karenina',
		     'Leo Tolstoy',
		     864,
		     'Another great classic!')
		    )
except Exception as e:
	print(f"Error: {e}")

try:
	cur.execute('INSERT INTO books (title, author, pages_num, review)'
		    'VALUES (:1, :2, :3, :4)',
		    ('Cronicas de la Torre',
		     'Laura Gallego',
		     271,
		     'Libro de fantasia de adolescentes')
		    )
except Exception as e:
	print(f"Error: {e}")

conn.commit()

cur.close()
conn.close()
