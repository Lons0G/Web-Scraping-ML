import requests
from bs4 import BeautifulSoup

url = 'https://listado.mercadolibre.com.mx/computacion/laptops-accesorios/nuevo/lenovo-ideapad-slim-3-intel-i5_NoIndex_True#applied_filter_id%3DITEM_CONDITION%26applied_filter_name%3DCondici%C3%B3n%26applied_filter_order%3D4%26applied_value_id%3D2230284%26applied_value_name%3DNuevo%26applied_value_order%3D1%26applied_value_results%3D38%26is_custom%3Dfalse'

response = requests.get(url, timeout = 5)

print('Status: ', response.status_code)


soup = BeautifulSoup(response.text, 'html.parser')
main = soup.find('main', id='root-app')

productos = main.find('ol', class_='ui-search-layout ui-search-layout--stack')

with open('pagina.html', 'w', encoding='utf-8') as archivo:
    archivo.write(str(productos))
print("HTML guardado correctamente en 'pagina.html'")
