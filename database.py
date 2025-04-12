import psycopg2

conn = psycopg2.connect(host='localhost', dbname='postgres', user='postgres', password='postgres123!', port=5432)

cursor = conn.cursor

def create_table():
    cursor.execute("""
                   CREATE TABLE IF NOT EXIST Productos(
                       ID INT PRIMARY KEY,
                       Nombre VARCHAR(255) NOT NULL,
                       Precio DECIMAL(10, 2) NOT NULL,
                       Vendedor VARCHAR(255),
                       Calificacion DECIMAL(2, 1),
                       Fecha DATE NOT NULL,
                       Recomendado INT DEFAULT 0
                       )
                   """)

def insert():
    cursor.execute("""
            INSERT INTO productos (
                nombre, 
                precio_original, 
                precio_num, 
                vendedor, 
                calificacion, 
                fecha_publicacion
            ) VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            nombre,
            precio,
            precio_limpio,
            vendedor_text,
            calificacion_num,
            fecha
        ))
