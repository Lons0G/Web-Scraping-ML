from types import NoneType
from bs4 import BeautifulSoup
from producto import Producto
from datetime import date

fecha = date.today() 

with open('pagina.html', 'r', encoding='utf-8') as archivo:
    html = archivo.read()

soup = BeautifulSoup(html, 'html.parser')

lista = soup.find_all('li', class_='ui-search-layout__item')

productos = []
for producto in lista:
    nombre = producto.find('a', class_='poly-component__title')
    precio = producto.find('span', class_='andes-money-amount andes-money-amount--cents-superscript')
    vendedor = producto.find('span', class_='poly-component__seller')
    calificacion = producto.find('span', class_='poly-reviews__rating')

    if type(vendedor) == NoneType and type(calificacion) == NoneType:
        prod = Producto(nombre.text, precio.text, '', '', fecha)
    elif type(vendedor) == NoneType and type(calificacion) != NoneType:
        prod = Producto(nombre.text, precio.text, '', calificacion.text, fecha)
    elif type(vendedor) != NoneType and type(calificacion) == NoneType:
        prod = Producto(nombre.text, precio.text, vendedor.text, '', fecha)
    else: 
        prod = Producto(nombre.text, precio.text, vendedor.text, calificacion.text, fecha)
    
    productos.append(prod)

print(len(productos))
i = 0
while i < len(productos):
    print(productos[i])
    i += 1
