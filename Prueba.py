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

#Generar bases de datos
#Crear las tablas de la pase de datos
with open("sql/create_tables.txt") as ifs:
    lines = ifs.readlines()
    for line in lines:
        if line:
            try:
                cur.execute(line)
            except Exception as e:
                print(f"Error al crear las tablas : {e}")
                fail = True
        
with open("sql/llenar_tables.txt") as ifs:
    lines = ifs.readlines()
    fail = False
    for line in lines:
        if line:
            try:
                cur.execute(line)
            except Exception as e:
                fail = True
                print(f"Ha habido un error al desplegar base de datos {e}")
                #cursor.execute(f"ROLLBACK TO SAVEPOINT {savepoint}")
            finally:
                if not fail:
                    conn.commit() #Puede lanzar excepcion

cur.close()
conn.close()
