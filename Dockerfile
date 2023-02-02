FROM python:3.7-alpine
WORKDIR /code 
# Variables de entorno con nombre FLASK_APP y valor app.py. Flask utilizará esta variable para saber que arhcivo contiene la app
ENV FLASK_APP=app.py
# Variable de entorno que indica que la app Flask se ejecutará en todas las interfaces de red disponibles
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_DEBUG=TRUE
# Instalar paquetes necesarios 
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]