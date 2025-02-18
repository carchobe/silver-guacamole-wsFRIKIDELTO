from selenium import webdriver
from bs4 import BeautifulSoup

# Asignamos las Variables
URL_BASE = 'https://www.impactgame.es'
url = "https://www.impactgame.es/epages/63945077.sf/es_ES/?ObjectPath=/Shops/63945077/Products/jm000092"

# descargamos el driver y abrira la ventana de pruebas de Chrome
# Ya no es necesario definir un path. Selenium Manager lo hace por nosotros
driver = webdriver.Chrome()

# Abrimos la url
driver.get(url)

# Descargamos y agarramos el codigo HTML cuando se complete la solicitud GET anterior
driver.page_source

# Listo, hagamos la sopa de BeautifulSoup (el HTML y el parser)
soup = BeautifulSoup(driver.page_source,'html.parser')

# Pidamos el nombre
nombre_producto = soup.find('h1',itemprop="name").text

# El precio
precio = soup.find('span',itemprop="price").text

# La imagen
imagen_producto = URL_BASE + soup.find('img',itemprop="image").attrs.get('src')

# La ultima sub categoria
sub_categoria = soup.find_all('span',itemprop="name")[2].text

# Codigo de referencia del producto
codigo_ref = url[33:41]

# Ahora mostremos los datos obtenidos
print('NOMBRE DEL PRODUCTO:',nombre_producto)
print('PRECIO.............:',precio)
print('IMAGEN.............:',imagen_producto)
print('SUB CATEGORIA......:',sub_categoria)
print('CODIGO.............:',codigo_ref)


#Cerramos el script scraper
driver.quit()