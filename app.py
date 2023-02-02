import os
import psycopg2

from flask import Flask

app = Flask(__name__)

def increase(conn):
    cur= conn.cursor()
    cur.execute("UPDATE contador SET valor_contador=valor_contador + 1")
    conn.commit()

@app.get("/")
def hello():
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
