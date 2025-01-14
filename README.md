# ferme-website

_Proyecto e-commerce para portafolio Duoc UC. Construido con [Django](https://www.djangoproject.com/), [Bootstrap 5](https://getbootstrap.com/) y Oracle SQL._

## Pre-requisitos:

Python 3+, dependencias listadas en requirements.txt, Docker/Podman

## Organización de archivos:

Scripts y modelos de la base de datos se encuentran en la carpeta /scripts_oracle.
El proyecto utiliza el patrón de Django MVT

## Setup ambiente de desarrollo:

1. Clonar repositorio

```sh
git clone https://github.com/Jaycedam/ferme-website.git
cd ferme-website
```

2. Crear entorno virtual de Python e instala dependencias

```sh
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

3. Usar container para Oracle SQL Free (Docker/Podman)

Ejemplo con Podman, instala [aquí](https://podman.io/getting-started/installation.html).
Utilizaremos Oracle Database 23ai Free Lite, ve detalles del container [aquí](https://container-registry.oracle.com/ords/ocr/ba/database/free).

```sh
podman run -d --name oracle-db -p 1521:1521 container-registry.oracle.com/database/free:23.6.0.0-lite
```

4. Revisa que el container se encuentre en estado "healthy" antes de proceder:

```sh
podman ps
```

5. Cambia la contraseña de la bd:

```sh
podman exec <oracle-db> ./setPassword.sh <your_password>
```

6. Copia los scripts de la carpeta /scripts_oracle a la carpeta /scripts_oracle del container:

```sh
podman cp scripts_oracle/ oracle-db:/tmp/scripts_oracle

```

7. Luego conecta con sqlplus

```sh
podman exec -it oracle-db sqlplus sys/admin@freepdb1 as sysdba
```

8. Aquí debes crear un usuario y asignarle los permisos necesarios. Para desarrollo local podemos asignar todos los permisos para poder comenzar rápido. Ejemplo:

```sql
CREATE USER ferme IDENTIFIED BY password;
GRANT ALL PRIVILEGES TO ferme;
```

9. Ingresando con el nuevo usuario en sqlplus, comienza a ejecutar los scripts de la carpeta /scripts_oracle en orden (1, 2, 3 y opcionalmente 4).

```sql
@/tmp/scripts_oracle/1.SCRIPT_CREACION_TABLAS.ddl
@/tmp/scripts_oracle/2.SCRIPT_INSERTS.sql
@/tmp/scripts_oracle/3.TRIGGERS_AND_SP.sql
@/tmp/scripts_oracle/4.INSERT_PRODUCTOS_MUESTRA.sql
```

10. Actualizar USER/PASSWORD de Oracle en **ferme/settings.py** con el nuevo usuario creado.

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.oracle",
        "NAME": "localhost:1521/freepdb1", # freepdb1 is the default pluggable db name in the oracle container
        "USER": "ferme",
        "PASSWORD": "password",
    }
}
```

11. Realiza las migraciones de la base de datos y crea un superusuario

```sh
python manage.py migrate
python manage.py createsuperuser
```

12. Corre el servidor para comprobar que todo está funcionando correctamente:

```sh
python manage.py runserver
```
