import psycopg2
import numpy as np

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            host='localhost',
            dbname='postgres',
            user='postgres',
            password='postgres123!',
            port=5432
        )
        self.cursor = self.conn.cursor()
    
    def create_table(self):
        """Crea la tabla si no existe"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                ID SERIAL PRIMARY KEY,
                Nombre VARCHAR(255) NOT NULL,
                Precio DECIMAL(10, 2) NOT NULL,
                Vendedor VARCHAR(255),
                Calificacion DECIMAL(2, 1),
                Fecha DATE NOT NULL,
                Recomendado INT DEFAULT 0
            )
        """)
        self.conn.commit()
    
    def insert_product(self, producto):
        """Inserta un producto en la tabla"""
        self.cursor.execute("""
            INSERT INTO productos (Nombre, Precio, Vendedor, Calificacion, Fecha)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            producto.nombre,
            producto.precio,
            producto.vendedor,
            producto.calificacion,
            producto.fecha
        ))
        self.conn.commit()
    
    def obtener_datos_numpy(self):
        """Devuelve (datos_numpy, nombres_columnas) para machine learning"""
        with self.conn.cursor() as cursor:
            cursor.execute("""
                SELECT precio, calificacion, recomendado
                FROM productos
                ORDER BY fecha ASC 
            """)
            
            datos = cursor.fetchall()
            
            arr = np.array(datos, dtype=float)
            arr[:, 0] = np.round(arr[:, 0].astype(float), 2)
            arr[:, 1] = np.round(arr[:, 1].astype(float), 2)
            arr[:, 2] = arr[:, 2].astype(int)
            
            return arr

    def close(self):
        """Cierra la conexión"""
        self.cursor.close()
        self.conn.close()
