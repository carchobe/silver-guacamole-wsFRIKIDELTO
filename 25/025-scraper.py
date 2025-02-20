from selenium import webdriver
# para modificar las opciones de webdriver en Chrome
from selenium.webdriver.chrome.options import Options
# para definir que tipo de busqueda del elemento
from selenium.webdriver.common.by import By


def iniciar_chrome():
    """Inicia Chrome con todos los parametros indicados y devuelve el driver"""

    #OPCIONES DE CHROME
    options = Options()
    user_agent= 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
    options.add_argument(f"user-agent={user_agent}") # define un user agent
    # options.add_argument("--window-size=1000.1000") # cambia las dimensiones de la ventana
    options.add_argument("--start-maximized") # para maximizar la ventana, es excluyente de la opcion anterior
    options.add_argument("--disable-web-security") # para inhabilitar la politica de Same Origin
    options.add_argument("--disable-extentions") # Inhabilita extensiones
    options.add_argument("--disable-notifiations") # inhabilitar notificaciones
    options.add_argument("--ignore-certificate-errors") # inhabilita el aviso de error de certificado
    options.add_argument("--no-sandbox")
    #options.add_argument("--log-level=3") # no mostrar nada en la terminal
    options.add_argument("--allow-running-insecure-content") # desactiva el aviso de contenido no seguro
    options.add_argument("--no-default-browser-check") # Desactiva el aviso del navegador predeterminado
    options.add_argument("--no-first-run") # Evita que chrome actue como si fuera la priera vez
    options.add_argument("--no-proxy-server") # Para no usar proxy 
    options.add_argument('--disable-blink-features=AutomationControlled') # IMPORTANTE evita que selenium sea detectado como un bot
    options.add_argument("--headless") # IMPORTANTE, no abre la ventana de chrome
    
    #PARAMETROS a omitir en el inicio de Chrome
    exp_opt = [
    'enable-automaion', # Para que no muestre la notificacion de software automatizado
	'ignore-certificate-errors', # para ignorar errores de certificados
	'enable-logging' # para no mostrar en la terminal el mensaje de devtools   
    ]

    options.add_experimental_option("excludeSwitches",exp_opt)
    
    # PARAMETROS QUE DEFINEN LAS PREFERENCIAS DE CHROME
    prefs = {
	    'profile.default_content_settings_values.notifications': 2, # notificaciones 0: preguntar, 1: permitir, 2: no permitir
	    'intl.accept_languages':["es-ES","es"], # Para definir el idioma del navegador
	    'credentials_enable_service:': False # Para no preguntar lo de guardar credenciales
	    }
    options.add_experimental_option('prefs',prefs)
    
    #Instanciar webdriver de selenium con Chrome
    driver = webdriver.Chrome(options=options)
    #Devolvemos el objeto driver
    return driver

if __name__ == '__main__':
    driver = iniciar_chrome()
    
    # Asignamos las Variables
    URL_BASE = 'https://www.impactgame.es'
    url = "https://www.impactgame.es/epages/63945077.sf/es_ES/?ObjectPath=/Shops/63945077/Products/jm000092"
    
    #Obtenemos la url
    driver.get(url)
    
    #Usar selenium en vez de bf4 para encontrar los elementos
    #nombre
    nombre_producto = driver.find_element(By.CSS_SELECTOR, "h1").text
    #precio
    precio_producto = driver.find_element(By.CSS_SELECTOR, "div.Price").text
    #convertir a valor float para incluir el decimal
    precio_producto_num = float(precio_producto.replace(',','.')[:-2])
    #IMAGEN
    url_imagen = driver.find_element(By.CSS_SELECTOR, "a img").get_attribute("src")

    #Print
    print(f"NOMBRE DEL PRODUCTO: {nombre_producto}")

    print(f"PRECIO DEL PRODUCTO: {precio_producto_num}")
    print(f"IMAGEN: {url_imagen}")

    #Cerramos el script scraper
    driver.quit()