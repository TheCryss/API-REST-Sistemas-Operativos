# API-REST-Sistemas-Operativos
## Proyecto final de Sistemas Operativos usando Docker-Compose.

***
En el archivo **requirements.txt** listamos todas las dependencias que usará el proyecto de Python,ya que cambiamos redis por postgres, entonces usaremos la dependencia **psycopg2** para conectarnos a una DB Postgres.

***
Se realizó un REST API *(es una interfaz que dos sistemas de computación utilizan para intercambiar información de manera segura a través de Internet)*, que mantiene un contador que se guarda en una base de datos, la cual en nuestro caso es Postgres. Esta aplicación está distribuida en contenedores.

***
## CÓMO LANZAR LA APLICACIÓN
<p> Lo primero es clonar el repositorio usando el comando: <code>git clone https://github.com/TheCryss/API-REST-Sistemas-Operativos.git</code>.
<p> Luego, colocar el comando <code>cd API-REST-Sistemas-Operativos/</code> para ingresar a la carpeta.
<p> y por último colocar el comando <code>docker compose up</code> para lanzar la aplicación.

***
Integrantes:
- Carlos Andrés Hernandez Agudelo (202125653)
- Juleipssy Daianne Cely Archila (202122035)
- Jose Luis Hincapié Bucheli (202125340)
