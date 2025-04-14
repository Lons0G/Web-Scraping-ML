import psycopg2

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
    
    def close(self):
        """Cierra la conexión"""
        self.cursor.close()
        self.conn.close()
