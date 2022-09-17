# Hefesto-Kairos

El proyecto funciona como un API REST para el registro de datos de estaciones meteorológicas arduino y como servicio de consulta de datos sobre estas estaciones.

## Instalar python

  ```console
  sudo apt install python3
  ```

## Instalar administrador de paquetes pip

  ```bash
  sudo apt install python3-venv python3-pip
  ```


## Crear por primera vez la configuración de entorno para el proyecto

- ### Crear el entorno virtual

  ```bash
  python3 -m venv venv
  ```

- ### Activar el entorno virtual

  - ### Sistemas Unix

    ```bash
    source venv/bin/activate
    ```

  - ## Windows

    ```powershell
    venv\Scripts\activate
    ```

- ### Instalar las dependencias del proyecto

    ```bash
    pip3 install -r requirements.txt
    ```

## Arrancar el proyecto

- ### Activar el entorno virtual si no está ya activo

- ### Exportar la variable de entorno de la aplicación

  - #### Sistemas Unix

    ```bash
    export FLASK_APP=kairos.py
    ```

  - #### Windows

    ```powershell
    $env:FLASK_APP = "kairos.py"
    ```

  - #### Configurar la aplicación en modo debug

    ```bash
    export FLASK_DEBUG=1
    ```

- ### Levantar una instancia de MongoDB con docker

  ```bash
  docker run -p 0.0.0.0:27017:27017 --name mongo-kairos -d mongo:4
  ```

- ### Arrancar el servidor

  ```bash
  flask run
  ```
  > **Nota:** Si diera algún error al arrancar borrar la carpeta de entorno y volverlo a crear y activar

## Formatear el fuente

  ```bash
  black kairos.py
  ```

## Analizar el fuente

  ```bash
  pylint kairos.py
  ```
