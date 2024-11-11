# Proyecto WattWise

## Descripción del Proyecto

Este proyecto, inspirado en el futuro de los vehículos eléctricos, incluye un módulo llamado Evsimulator. Este módulo permite a los usuarios registrar vehículos que funcionan con gasolina, diésel o gas natural, calcular los costos de mantenimiento y obtener un informe detallado del costo anual de mantenimiento. Además, ofrece una comparación con los costos de mantenimiento de un vehículo eléctrico.

El objetivo principal de WattWise es proporcionar una herramienta integral que facilite la transición hacia vehículos eléctricos, ofreciendo información precisa y útil sobre los costos de mantenimiento y las ventajas económicas a largo plazo. El proyecto está diseñado para ser fácil de usar y accesible para cualquier persona interesada en la movilidad sostenible.

Actualmente, el proyecto está en desarrollo y puede contener errores, vulnerabilidades o carecer de algunas funcionalidades.

Dado que el proyecto está en desarrollo, aún no se ha integrado con bases de datos como MySQL, PostgreSQL, etc. Estas funcionalidades se implementarán en la fase de despliegue en un servidor web.

El proyecto se puede configurar de dos maneras: mediante `git clone` o utilizando Docker. La primera opción es ideal si deseas modificar el código base, mientras que la segunda es más conveniente si solo quieres visualizar la aplicación web en un navegador en cualquier sistema operativo que tenga Docker instalado.

## Configuración del Entorno

1. Clona el repositorio:
    ```sh
    git clone https://github.com/santihern16/wattwise.git
    cd tu-repositorio
    ```

2. Crea y activa un entorno virtual:
    ```sh
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

4. Aplica las migraciones para crear la base de datos:
    ```sh
    python manage.py migrate
    ```

5. Inicia el servidor de desarrollo:
    ```sh
    python manage.py runserver
    ```

## Uso

- Accede a la aplicación en `http://127.0.0.1:8000/`

# Segunda Opción

## Utilizando Docker

1. Descarga la imagen desde el repositorio de Docker Hub:
    ```sh
    docker pull santihern/wattwise:latest
    docker images # Verifica que la imagen se haya descargado correctamente
    ```

2. Inicia un contenedor usando la imagen descargada:
    ```sh
    docker run -d -p 8000:8000 santihern/wattwise
    ```

Esto iniciará un contenedor en segundo plano (-d) y mapeará el puerto 8000 del contenedor al puerto 8000 de la máquina host (-p 8000:8000).

Accede a la aplicación en `http://127.0.0.1:8000/`
