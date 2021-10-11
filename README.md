# Introduction 
Microservicio para geolocalizar una direccion dada en texto

# Getting Started
1. Se debe tener instalado pip y ejecutar pajo un virtualenv -Solo si no tiene instalado de lo contrario pasar al punto 2
> pip install virtualenv

2. para crear el ambiente 
> virtualenv venv

3. para cambiar por consola al entorno recien creado
> source venv/bin/activate 

4. Instalar dependencias
> pip3 --no-cache-dir install -r requirements.txt

5. Ejecutar la aplicación
> python src/app.py

# Build
Para subir, si se han realizado nuevas instalaciones se debe ejecutar el siguiente comando, para que al crear la imagen docker tome las dependencias
> pip freeze > requirements.txt

