import os
import psycopg2

from flask import Flask,jsonify, request

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
        return "Has visitado la pagina "+str(database_name)+" veces"
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
        cur= conn.cursor()
        # Obtener el resultado de la consulta
        reset(conn)
        database_name = cur.fetchone()[0]
        return "El contador fue resetado a "+str(database_name)
    except Exception as e:
        return str(e)
    finally:
        if conn:
            conn.close()

def update(conn):
    cur = conn.cursor()
    data = request.get_json()
    counter_value = data['value']
    cur.execute(f"UPDATE contador SET valor_contador = {counter_value}")
    conn.commit()
    

#curl -X POST -H "Content-Type: application/json" -d '{"value": 123}' http://localhost:8000/counter
#Peticion para actualizar el valor
    
@app.route('/counter', methods=['POST'])
def add_counter():
    database_url = os.getenv("DATABASE_URL")
    try:
        conn = psycopg2.connect(database_url)
        cur = conn.cursor()
        update(conn)
        counter_value= cur.execute("SELECT * FROM contador")
        return f"El contador ha sido actualizado a {counter_value}"
    except Exception as e:
        return str(e)
    finally:
        if conn:
            conn.close()

#curl -X PUT -H "Content-Type: application/json" http://localhost:8000/counter/25
#Peticion para actualizar el valor

@app.route('/counter/<int:value>', methods=['PUT'])
def update_counter(value):
    database_url = os.getenv("DATABASE_URL")
    try:
        conn = psycopg2.connect(database_url)
        cur = conn.cursor()
        cur.execute(f"UPDATE contador SET valor_contador = {value}")
        conn.commit()
        cur.execute("SELECT * FROM contador")
        counter_value = cur.fetchone()[0]
        return f"El contador ha sido actualizado a {counter_value}"
    except Exception as e:
        return str(e)
    finally:
        if conn:
            conn.close()