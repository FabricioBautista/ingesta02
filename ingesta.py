import pymysql
import csv
import boto3

# Conectar a la base de datos MySQL
connection = pymysql.connect(
    host='your-mysql-host', 
    user='your-username', 
    password='your-password', 
    database='your-database-name'
)

# Ejecutar una consulta para obtener los datos de una tabla
cursor = connection.cursor()
cursor.execute("SELECT * FROM your_table")

# Guardar los resultados en un archivo CSV
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([i[0] for i in cursor.description])  # Column headers
    writer.writerows(cursor.fetchall())  # Data rows

# Cerrar la conexión a MySQL
cursor.close()
connection.close()

# Subir el archivo CSV a S3
s3 = boto3.client('s3')
bucket_name = 'fb-output02'
s3.upload_file('output.csv', bucket_name, 'output.csv')

print("Archivo CSV subido a S3 correctamente.")
