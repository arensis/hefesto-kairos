# Hefesto-Kairos

El proyecto funciona como un API REST para el registro de datos de estaciones meteorológicas arduino y como servicio de consulta de datos sobre estas estaciones.

## Estación meteorológica

Para reportar datos se utilizó una placa NodeMCU que tiene conectado un sensor de temperatura y humedad DHT11. La placa envía las mediciones a través de una petición REST al servidor y en caso de error envía una notificación a un bot de Telegram.
Para funcionar correctamente se han de completar ciertas variables en el fichero config.h, tales como la conexión de la wifi, la url del servidor, los datos de conexión con el bot de telegram, etc.

[Repositorio de código de estación con DHT11 y placa NodeMCU](https://github.com/arensis/arduino/tree/kairos/NodeMCU/KAIROS_STATION_DHT11_SENSOR/API_CLIENT_JSON_DS18B20_TEMP_SENSOR)

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
  Si el contenedor de docker va a ser ejecutado dentro de una raspberry pi, si la raspberry pi es inferior a la raspberrypi 5 deberá usarse la versión de mongo 4.4.6, debido a que versiones posteriores requieren que el procesador suporte instrucciones AVX y los procesadores que montan raspberrypi inferiores a la 5 no lo soportan.
  - Fuente: https://github.com/linuxserver/docker-unifi-network-application/issues/4
  - Qué son las instruccions AVX: https://hardzone.es/reportajes/que-es/instrucciones-avx-procesador/
  - Comando:
    ```bash
    docker run -p 0.0.0.0:27017:27017 --name mongo-kairos -d mongo:4.4.6
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
