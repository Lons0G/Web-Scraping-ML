from extractor import scrape_html
from database import Database

def main():
    # 1. Extraer datos
    productos = scrape_html('pagina.html')
    
    # 2. Conexión a DB y creación de tabla
    db = Database()
    db.create_table()
    
    # 3. Almacenar cada producto
    for producto in productos:
        db.insert_product(producto)
        print(f"Insertado: {producto.nombre[:50]}...")  # Muestra primeros 50 caracteres
    
    # 4. Cerrar conexión
    db.close()
    print("✅ Proceso completado")

if __name__ == "__main__":
    main()
