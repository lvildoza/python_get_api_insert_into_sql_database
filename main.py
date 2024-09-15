import requests
import json
from database import get_db_connection

# Realiza la solicitud a la API
response = requests.get('https://jsonplaceholder.typicode.com/users/1')

# Convierte la respuesta a un diccionario de Python
response_json = response.json()

# Obtiene los datos del usuario y la calle
user = response_json['name']
street = response_json['address']['street']

# Conexión a la base de datos SQL Server
conn = get_db_connection()
cursor = conn.cursor()

# Inserta los datos en la tabla Users
cursor.execute('''
    INSERT INTO Users (Name, Street)
    VALUES (?, ?)
''', (user, street))

# Confirma la transacción
conn.commit()

# Cierra la conexión
cursor.close()
conn.close()

print("Datos insertados correctamente en la base de datos.")
