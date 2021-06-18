# ferme-website
_Proyecto e-commerce para portafolio Duoc UC. Construido con [Django](https://www.djangoproject.com/) y [Bootstrap 5](https://getbootstrap.com/)._
 
## Pre-requisitos:
Python 3+, Oracle database xe y dependencias listadas en /requirements.txt


## Organización de archivos:
Scripts y modelos de la base de datos se encuentran en la carpeta /scripts_oracle.
El proyecto utiliza el patrón de Django MVT

## Setup ambiente de desarrollo:
* Actualizar USER/PASSWORD de Oracle en **ferme/settings.py**
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'xe',
        'USER': 'portafolio',
        'PASSWORD': 'portafolio',
        'HOST': '',
        'PORT': '',
    }
}
```
* Actualizar EMAIL_HOST_USER/EMAIL_HOST_PASSWORD en **ferme/settings.py** (La cuenta debe tener acceso de apps menos seguras)
```
EMAIL_HOST = 'smtp.googlemail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'email@example.com'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_USE_TLS = True
```
* Ejecutar scripts de oracle 1, 2 y 3 en la BD y migrar tablas de Django
```
python ./manage.py migrate
```
* Crear superusuario
```
python ./manage.py createsuperuser
```
* Iniciar servidor
```
python ./manage.py runserver
```
