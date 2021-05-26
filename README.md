# ferme-website
_Proyecto e-commerce para portafolio Duoc UC. Construido con [Django](https://www.djangoproject.com/) y [Bootstrap 5](https://getbootstrap.com/)._
 
## Pre-requisitos:
```
Python 3+, Oracle database xe y dependencias listadas en /requirements.txt
```

## Organización de archivos:
```
Scripts y modelos de la base de datos se encuentran en la carpeta /scripts_oracle
El proyecto utiliza el patrón de Django MVT
```

## Setup ambiente de desarrollo:
* Actualizar tus credenciales de Oracle en **ferme/settings.py**
* Ejecutar scripts de oracle 1, 2 y 3
* Migrar tablas de Django **“python ./manage.py migrate”** _(path proyecto)_
* Crear superusuario **“python ./manage.py createsuperuser”** _(path proyecto)_
* Iniciar servidor **“python ./manage.py runserver”** _(path proyecto)_

## Datos de muestra:
```
Se pueden insertar datos de muestra para testing utilizando el script sql 4
```
