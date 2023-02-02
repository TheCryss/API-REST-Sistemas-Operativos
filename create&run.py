import psycopg2
database_url = os.getenv("DATABASE_URL")
conn = psycopg2.connect(database_url)
cur = conn.cursor()
cur.execute("""CREATE TABLE contador (id SERIAL PRIMARY KEY,value INTEGER);""")
cur.execute("""INSERT INTO contador (value) VALUES (0);""")
conn.commit()
cur.close
conn.close