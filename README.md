# Taller Semana 10


## Acciones previas al taller

* Ingresar a la carpeta **ejemplo04/proyectouno**
* Levantar el entorno
* Instalar la librerías django-import-export en el entorno; a través de **pip install django-import-export**
  * La librería permite: "django-import-export is a Django application and library for importing and exporting data with included admin integration - https://django-import-export.readthedocs.io/en/latest/index.html"
* Usar el atajo **python manage.py migrate**
* Crear un super-usuario
* Revisar los archivos de la aplicación **models.py admin.py**
* Levantar el proyecto a través de **runserver**
* En la interfaz de administración generar dos registros de tipo **Modulo**
* Importar los registros de estudiantes.csv; desde la interfaz de administración, opción **import**
* Importar los registros de matriculas.csv; desde la interfaz de administración, opción **import**


## Desarrollo taller - Semana 10 - revisar el proyecto de la carpeta ejemplo04 del repositorio usado en clases

### Crear un proyecto en Django
* El proyecto se lo debe crear en la carpeta taller
* Nombre del Proyecto: **deporteecuador**
  * Nombre de la Aplicación: **futbolec**

### Problemática

### Crear las siguientes entidades:


* Equipo de Futbol: nombre, siglas, username twitter

* Jugador: nombre, posición campo, número camiseta, sueldo, equipo de fútbol

* Campeonato: nombre de campeonato, nombre de auspiciante

* Campeonato Equipos: año, equipo de fútbol, campeonato

### Habilitar la parte administrativa

### Agregar información

#### ejemplos
Equipos:
 * Barcelona / BSC / @barcerlonat
 * Liga de Quito / LDUQ / @lduq

Jugadores:
 * Damian Diaz, centro, 10, 20000, Barcelona
 * Javier Burrai, arquero, 1, 18000, Barcelona
 * Alexander Alvarado, delantero, 7, 19000, Liga de Quito
 * Nilson Souza, defensa, 3, 15000, Liga de Quito

 Campeonato:
 * Liga Pro / Bet593

 Campeonatos Equipos
 * 2023 / Barcelona / Liga Pro
 * 2023 / Liga de Quito / Liga Pro

![alt text](image.png)

![alt text](image-1.png)
