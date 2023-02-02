import os
import psycopg2

from flask import Flask

app = Flask(__name__)

def increase(conn):
    cur= conn.cursor()
    cur.execute("UPDATE contador SET valor_contador=valor_contador + 1")
    conn.commit()

def reset(conn):
    cur=conn.cursor()
    cur.execute("UPDATE contador SET valor_contador=0")
    conn.commit()

@app.route("/")
def hello():
    return "Bienvenido a esta API REST con flask y postgresql"


@app.route("/counter",methods=['GET'])
def get_counter():
    database_url = os.getenv("DATABASE_URL")
    try:
        conn = psycopg2.connect(database_url) # Conectar a la base de datos
        cur = conn.cursor() # Crear un cursor
        # Ejecutar una consulta
        cur.execute("SELECT * FROM contador")
        # Obtener el resultado de la consulta
        database_name = cur.fetchone()[0]
        increase(conn)
        return "Has visitado la pagina "+str(database_name)
    except Exception as e:
        # Manejar la excepción
        return str(e)
    finally:
        # Cerrar la conexión
        if conn:
            conn.close()

@app.route("/counter",methods=['DELETE'])
def reset_counter():
    database_url = os.getenv("DATABASE_URL")
    try:
        conn =psycopg2.connect(database_url)
        cur= conn.cursor
        cur.execute("SELECT * FROM contador")
        # Obtener el resultado de la consulta
        database_name = cur.fetchone()[0]
        increase(conn)
        return "El contador fue resetado a "+str(database_name)
    except Exception as e:
        return str(e)
    finally:
        if conn:
            conn.close()