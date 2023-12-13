import os

CS = "oracle0.ugr.es:1521/practbd.oracle0.ugr.es"
class DB:
    def __init__():
        self.usr = os.environ['DB_USERNAME']
        self.pwd = os.environ['DB_PASSWORD']
        self.conn = None 
        try:
            self.conn = oracledb.connect(user=usr,password=pwd,dsn=CS)
        except Exception as e:
            print(f"Error al establecer conexión:{e}")
            exit(-1)

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
        
    def llenar_tablas(self):

        #Propiedades
        num_entradas = 10
        random.seed(69)
        fail = False
        clientes = propiedades = []
        query = "INSERT INTO Cliente VALUES (:1, :2)"
        #Clientes - Genero lista de tupla 
        for i in range(0,num_entradas,1):
            clientes.append((i,random.randint(0,999)))
            propiedades.append((i,random.randint(0,999)))
        
        savepoint = f"SP_{random.randint(0,99)}"
        cursor.execute(f"SAVEPOINT {savepoint}")
        try:
            conn.cursor.executemany(query,clientes)
            conn.cursor.executemany(query,propiedades)
        except Exception as e:
            fail = True
            print(f"Ha habido un error al desplegar base de datos {e}")
            cursor.execute(f"ROLLBACK TO SAVEPOINT {savepoint}")
        finally:
            if not fail:
                conn.commit() #Puede lanzar excepcion
        

    def borra_tablas(self):
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

        

