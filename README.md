# API-REST-Sistemas-Operativos
## Proyecto final de Sistemas Operativos usando Docker-Compose.

***
En el archivo **requirements.txt** listamos todas las dependencias que usará el proyecto de Python,ya que cambiamos redis por postgres, entonces usaremos la dependencia **psycopg2** para conectarnos a una DB Postgres.

***
Se realizó un REST API *(es una interfaz que dos sistemas de computación utilizan para intercambiar información de manera segura a través de Internet)*, que mantiene un contador que se guarda en una base de datos, la cual en nuestro caso es Postgres. Esta aplicación está distribuida en contenedores.

***
## CÓMO LANZAR LA APLICACIÓN
- Lo primero es clonar el repositorio usando el comando: <code>git clone https://github.com/TheCryss/API-REST-Sistemas-Operativos.git</code>.
- Luego, colocar el comando <code>cd API-REST-Sistemas-Operativos/</code> para ingresar a la carpeta.
- Por último, debes colocar el comando <code>docker compose up</code> para lanzar la aplicación.

***

## Como usar la aplicacion

A continuación se le describira cada uno de los endpoints y el comando que debe ingresar en consola una vez hayas hecho el <code>docker compose up</code>

- Endpoint "/":

Este endpoint te devuelve un mensaje de bienvenida a la API REST..

<code>curl -s http://localhost:8000/</code>


- Endpoint "/counter" con método GET:

Este endpoint te devuelve el número de veces que has visitado la página.

<code>curl http://localhost:8000/counter</code>

- Endpoint "/counter" con método DELETE:

Este endpoint resetea el contador a 0.

<code>curl -X DELETE http://localhost:8000/counter</code>

- Endpoint "/counter" con método POST:

Este endpoint actualiza el valor del contador a un valor específico enviado en el cuerpo de la petición.

<code>curl -X POST -H "Content-Type: application/json" -d '{"value": 123}' http://localhost:8000/counter</code>

- Endpoint "/counter/int:value" con método PUT:

Este endpoint actualiza el valor del contador a un valor específico enviado en la URL.

<code>curl -X PUT -H "Content-Type: application/json" http://localhost:8000/counter/25</code>

- Endpoint "/counter" con método PUT:

Este endpoint incrementa el valor del contador en 1.

<code>curl -X PUT http://localhost:8000/counter</code>

***
Integrantes:
- Carlos Andrés Hernandez Agudelo (202125653)
- Juleipssy Daianne Cely Archila (202122035)
- Jose Luis Hincapié Bucheli (202125340)
