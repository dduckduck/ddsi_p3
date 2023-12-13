import os

CS = "oracle0.ugr.es:1521/practbd.oracle0.ugr.es"
class DB:
    def __init__():
        self.usr = os.environ['DB_USERNAME']
        self.pwd = os.environ['DB_PASSWORD']
        self.conn = None 
        try:
            self.conn = oracledb.connect(user=usr,password=pwd,dsn=cs)
        except Exception as e:
            print(f"Error al establecer conexión:{e}")
            exit(-1)

    def exec_querry(querry: str, msg="Error generico")->list:
        output = []
        try:
            cur.execute(querry)
            output = cur.fetchall()
        except Exception as e:
            print(f"Error al consultar libros: {e}")
        return output


#Generar bases de datos
def crear_tablas(self):
    #Clientes
    with open("sql/create_tables.txt") as ifs:
        lines = ifs.readlines()
    for line in lines:
        if line:
            try:
                conn.cursor.execute(line)
            except Exception as e:
                print(f"Error al crear tabla clientes: {e}")
                fail = True
    
    #Propiedades
    with open("sql/create_tables.txt") as ifs:
        lines = ifs.readlines()
    for line in lines:
        if line:
            try:
                conn.cursor.execute(line)
            except Exception as e:
                print(f"Error al crear tabla clientes: {e}")
                fail = True

    #CompraVenta
    with open("sql/create_tables.txt") as ifs:
        lines = ifs.readlines()
    for line in lines:
        if line:
            try:
                conn.cursor.execute(line)
            except Exception as e:
                print(f"Error al crear tabla clientes: {e}")
                fail = True
    
    #Servicio
    with open("sql/create_tables.txt") as ifs:
        lines = ifs.readlines()
    for line in lines:
        if line:
            try:
                conn.cursor.execute(line)
            except Exception as e:
                print(f"Error al crear tabla clientes: {e}")
                fail = True
  
def borra_tablas():
    with open("sql/drop_tables.txt",'r') as input:
        lines = input.readlines()
    for line in lines:
        try:
            conn.cursor.execute(line)
        except Exception as e:
            print(f"Ha habido un error {e}")
            break
           
            
def imprimir_tablas():
    with open("sql/print_tables.txt",'r') as input:
        lines = input.readlines()
    for line in lines:
       try:
           conn.cursor.execute(line)
           tabla = from_db_cursor(cursor)
           nombre_tabla = line.split(' ')[-1].strip()
           print(f"Tabla: {nombre_tabla}")
           print(f"{tabla}\n")
       except Exception as e:
            print(f"Error al consultar las tablas: {e}")

    

