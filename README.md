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

### Crear el entorno virtual

  ```bash
  python3 -m venv venv
  ```

### Activar el entorno virtual

```bash
source venv/bin/activate
```

### Instalar las dependencias del proyecto

  ```bash
  pip3 install -r requirements.txt
  ```

## Arrancar el proyecto

### Activar el entorno virtual si no está ya activo

```bash
source venv/bin/activate
```

### Exportar la variable de entorno de la aplicación

```bash
export FLASK_APP=kairos.py
```

### Configurar la aplicación en modo debug

```bash
export FLASK_DEBUG=1
```

### Levantar el servidor

```bash
flask run
```

## Formatear el fuente

  ```bash
  black kairos.py
  ```

## Analizar el fuente

  ```bash
  pylint kairos.py
  ```
