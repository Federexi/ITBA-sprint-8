# Conectando con el mundo - Sprint 8

Script que genera un api privada, útil para interactuar con la información del homebanking, creada utilizando Django Rest Framework.

## Dependencias

* python 3  https://www.python.org/downloads/

* Django https://www.djangoproject.com/download/

* Django Rest Framework https://www.django-rest-framework.org/

## Instalacion

Para instalar en Linux

$ sudo apt-get install python3

Para instalar el resto de los requerimientos

$ pip install -r requirements.txt

## Correr el programa

* Crear ambiente virtual y activarlo:
$ python3 -m venv env
$ env/scripts/activate

* Instalar requerimientos

* Posicionarse en el directorio "homebanking":
$ cd homebanking

* Activar el servidor:
$ python3 manage.py runserver

* Acceder a la api:
http://127.0.0.1:8000/api/

* Acceder a los prestamos de una sucursal:
http://127.0.0.1:8000/api/prestamos_por_sucursal/(id de la sucursal deseada)

* Acceder a las tarjetas de un cliente:
http://127.0.0.1:8000/api/tarjetas/(id de cliente deseado)

* Acceder al listado publico de sucursales:
http://127.0.0.1:8000/api/sucursales/

## Grupo 3

* Integrantes: Agustín Nahuel Bloise, Diego Ezequiel Benítez y Federico Bidarra.
