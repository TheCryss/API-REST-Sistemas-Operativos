import time

import os
import psycopg2

from flask import Flask

app = Flask(__name__)



@app.get("/")
def hello():
    database_url = os.getenv("DATABASE_URL")
    
    # Conectar a la base de datos
    conn = psycopg2.connect(database_url)
    
    # Crear un cursor
    cur = conn.cursor()
    
    # Ejecutar una consulta
    cur.execute("SELECT current_database()")

    # Obtener el resultado de la consulta
    database_name = cur.fetchone()[0]
    return database_name
    
    # Obtener los resultados
    #result = cur.fetchone()[0]
    
    # Cerrar el cursor y la conexión a la base de datos

    
    # Devolver los resultados como respuesta HTTP
    #return result
