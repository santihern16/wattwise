# Proyecto WattWise

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