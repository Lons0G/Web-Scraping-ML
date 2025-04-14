from types import NoneType
from bs4 import BeautifulSoup
from producto import Producto
from datetime import date, timedelta

def scrape_html(file_path):
    fecha = date.today() - timedelta(days=1)  
    productos = []

    with open(file_path, 'r', encoding='utf-8') as archivo:
        soup = BeautifulSoup(archivo.read(), 'html.parser')

    for item in soup.find_all('li', class_='ui-search-layout__item'):
        nombre = item.find('a', class_='poly-component__title')
        precio = item.find('span', class_='andes-money-amount')
        vendedor = item.find('span', class_='poly-component__seller')
        calificacion = item.find('span', class_='poly-reviews__rating')

        # Limpieza de datos
        precio_limpio = float(precio.text.replace('$', '').replace(',', '')) if precio else 0.0
        vendedor_text = vendedor.text.strip() if vendedor else ''
        calificacion_num = float(calificacion.text) if calificacion else None

        productos.append(Producto(
            nombre=nombre.text if nombre else '',
            precio=precio_limpio,
            vendedor=vendedor_text,
            calificacion=calificacion_num,
            fecha=fecha
        ))

    return productos
