# Proyecto de Consumo de API y Almacenamiento en SQL Server

## Descripción del Proyecto

**Objetivo**: El objetivo principal de este proyecto es aprender a consumir datos de una API, procesarlos y almacenarlos en una base de datos SQL Server de manera segura y organizada.

## Utilidades del Proyecto

1. **Consumo de APIs**:
   - Realizar solicitudes HTTP a una API externa usando la librería `requests`.
   - Manejar y procesar respuestas en formato JSON.

2. **Manejo de Datos**:
   - Extraer datos específicos de la respuesta JSON y prepararlos para su almacenamiento.

3. **Conexión a Bases de Datos**:
   - Configurar una conexión segura a una base de datos SQL Server usando `pyodbc`.
   - Insertar datos en una tabla de SQL Server.

4. **Seguridad y Buenas Prácticas**:
   - Utilizar archivos `.env` para mantener las credenciales de la base de datos seguras y fuera del código fuente.
   - Organizar el código en módulos (`database.py` y `main.py`) para mejorar la mantenibilidad y la claridad del proyecto.

5. **Automatización y Escalabilidad**:
   - Este proyecto puede ser la base para automatizar la recolección y almacenamiento de datos desde múltiples APIs.
   - Puede expandirse para incluir más campos, manejar errores y excepciones, y realizar análisis de datos.

## Estructura del Proyecto
proyecto-api-sql │ README.md │ .env │ main.py │ database.py └───requirements.txt

## Archivos y Directorios

- **README.md**: Este archivo, que contiene la descripción del proyecto y las instrucciones.
- **.env**: Archivo que contiene las variables de entorno para la conexión a la base de datos.
- **main.py**: Archivo principal que realiza la solicitud a la API y almacena los datos en la base de datos.
- **database.py**: Archivo que maneja la conexión a la base de datos.
- **requirements.txt**: Archivo que lista las dependencias del proyecto.

## Instalación y Configuración

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/lvildoza/python_get_api_insert_into_sql_database.git
   cd python_get_api_insert_into_sql_database

2. Instala los paquetes necesarios:
   ```bash
   pip install requests python-dotenv pyodbc
   ```
3. Configura tu archivo `.env` en la raíz del proyecto con las credenciales de tu base de datos:
   ```plaintext
   DB_DRIVER={el driver de tu base de datos}
   DB_SERVER={tu servidor o IP}
   DB_NAME={nombre de la base de datos}
   DB_USER={tu nombre de usuario}
   DB_PASSWORD={tu contraseña}
   ```
## Ejecución

Para ejecutar el proyecto, simplemente ejecuta `main.py`:

```bash
python main.py
```
Deberías ver un mensaje con luego de la consulta a la API e inserción en la base de "LDatos insertados correctamente en la base de datos." si todo está configurado correctamente.

## Notas

- Asegúrate de que el archivo `.env` esté en tu archivo `.gitignore` para evitar subir información sensible al repositorio.
- Verifica que los drivers y credenciales de tu base de datos sean correctos para evitar errores de conexión.