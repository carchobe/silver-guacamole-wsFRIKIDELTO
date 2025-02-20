# Configurar CHROME y SCRAPING con SELENIUM

Aprenderemos a configurar al detalle nuestro webdriver de Selenium para que nuestras peticiones sean mucho más efectivas, evitando así posibles problemas al realizarlas.
Además, veremos cómo se pueden obtener los datos al hacer web scraping directamente con Selenium, sin necesidad de usar Beautifulsoup.

Sandbox de Chrome

“No-sandbox” es una opción que se puede usar en el navegador Google Chrome para deshabilitar el sandbox. El sandbox es un mecanismo de seguridad que se utiliza para aislar los procesos del navegador y evitar que los sitios web maliciosos ejecuten código en el equipo del usuario. Al deshabilitar el sandbox, se expone al usuario a posibles exploits de JavaScript maliciosos que pueden ejecutar código arbitrario en su equipo . fuente de la repuesta es BING

ARTÍCULO con todas las OPCIONES de inicio de CHROME:

https://peter.sh/experiments/chromium-command-line-switches/

ARTÍCULO sobre SAME ORIGIN POLICY:

https://professor-falken.com/general/como-deshabilitar-la-politica-del-mismo-origen-o-same-origin-policy-en-chrome

CONTENIDO de la clase BY:

https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.by.html#module-selenium.webdriver.common.by

DOCUMENTACIÓN OFICIAL de SELENIUM:

https://www.selenium.dev/documentation

[Encontrando elementos web en selenium](https://www.selenium.dev/documentation/webdriver/elements/finders/)

Reemplazanndo strings en python

https://www.geeksforgeeks.org/python-string-replace/

dividiendo strings en python con split

https://www.geeksforgeeks.org/python-string-split/

ÍNDICE:

[00:00](https://www.youtube.com/watch?v=348iLgXfgvk&list=PLheIVUbpfWZ1AVQHaPq5iwRMf6JcI6xP0&index=4&t=0s) Introducción

[00:42](https://www.youtube.com/watch?v=348iLgXfgvk&list=PLheIVUbpfWZ1AVQHaPq5iwRMf6JcI6xP0&index=4&t=42s) Importación de la clase Options de Chrome en Selenium

[02:32](https://www.youtube.com/watch?v=348iLgXfgvk&list=PLheIVUbpfWZ1AVQHaPq5iwRMf6JcI6xP0&index=4&t=152s) User agent personalizado en Selenium

[03:02](https://www.youtube.com/watch?v=348iLgXfgvk&list=PLheIVUbpfWZ1AVQHaPq5iwRMf6JcI6xP0&index=4&t=182s) Personalizar las dimensiones de la ventana de Chrome

[03:26](https://www.youtube.com/watch?v=348iLgXfgvk&list=PLheIVUbpfWZ1AVQHaPq5iwRMf6JcI6xP0&index=4&t=206s) Maximizar la ventana de Chrome

[04:01](https://www.youtube.com/watch?v=348iLgXfgvk&list=PLheIVUbpfWZ1AVQHaPq5iwRMf6JcI6xP0&index=4&t=241s) Deshabilitar Same Origin Policy

[04:18](https://www.youtube.com/watch?v=348iLgXfgvk&list=PLheIVUbpfWZ1AVQHaPq5iwRMf6JcI6xP0&index=4&t=258s) Deshabilitar las extensiones

[04:25](https://www.youtube.com/watch?v=348iLgXfgvk&list=PLheIVUbpfWZ1AVQHaPq5iwRMf6JcI6xP0&index=4&t=265s) Deshabilitar las notificaciones

[04:44](https://www.youtube.com/watch?v=348iLgXfgvk&list=PLheIVUbpfWZ1AVQHaPq5iwRMf6JcI6xP0&index=4&t=284s) Ignorar el aviso "Su conexión no es privada"

[04:58](https://www.youtube.com/watch?v=348iLgXfgvk&list=PLheIVUbpfWZ1AVQHaPq5iwRMf6JcI6xP0&index=4&t=298s) Deshabilitar el modo sandbox

[05:15](https://www.youtube.com/watch?v=348iLgXfgvk&list=PLheIVUbpfWZ1AVQHaPq5iwRMf6JcI6xP0&index=4&t=315s) No mostrar información de chromedriver en pantalla

[05:26](https://www.youtube.com/watch?v=348iLgXfgvk&list=PLheIVUbpfWZ1AVQHaPq5iwRMf6JcI6xP0&index=4&t=326s) Desactivar el aviso de "Contenido no seguro"

[05:40](https://www.youtube.com/watch?v=348iLgXfgvk&list=PLheIVUbpfWZ1AVQHaPq5iwRMf6JcI6xP0&index=4&t=340s) Desactivar la comprobación de navegador por defecto

[06:06](https://www.youtube.com/watch?v=348iLgXfgvk&list=PLheIVUbpfWZ1AVQHaPq5iwRMf6JcI6xP0&index=4&t=366s) Evitar ejecución de ciertas tareas al iniciar Chrome

[06:24](https://www.youtube.com/watch?v=348iLgXfgvk&list=PLheIVUbpfWZ1AVQHaPq5iwRMf6JcI6xP0&index=4&t=384s) No usar proxies

[06:35](https://www.youtube.com/watch?v=348iLgXfgvk&list=PLheIVUbpfWZ1AVQHaPq5iwRMf6JcI6xP0&index=4&t=395s) Evitar que el servidor detecte que somos un bot

[09:37](https://www.youtube.com/watch?v=348iLgXfgvk&list=PLheIVUbpfWZ1AVQHaPq5iwRMf6JcI6xP0&index=4&t=577s) Parámetros a omitir en el inicio de Chrome

[11:28](https://www.youtube.com/watch?v=348iLgXfgvk&list=PLheIVUbpfWZ1AVQHaPq5iwRMf6JcI6xP0&index=4&t=688s) Parámetros que definen las preferencias de Chrome

[13:26](https://www.youtube.com/watch?v=348iLgXfgvk&list=PLheIVUbpfWZ1AVQHaPq5iwRMf6JcI6xP0&index=4&t=806s) ¿Cómo hacer web scraping con Selenium?

[14:10](https://www.youtube.com/watch?v=348iLgXfgvk&list=PLheIVUbpfWZ1AVQHaPq5iwRMf6JcI6xP0&index=4&t=850s) Método find_element()

[20:17](https://www.youtube.com/watch?v=348iLgXfgvk&list=PLheIVUbpfWZ1AVQHaPq5iwRMf6JcI6xP0&index=4&t=1217s) Método find_elements()

[26:27](https://www.youtube.com/watch?v=348iLgXfgvk&list=PLheIVUbpfWZ1AVQHaPq5iwRMf6JcI6xP0&index=4&t=1587s) Método get_attribute()

[28:10](https://www.youtube.com/watch?v=348iLgXfgvk&list=PLheIVUbpfWZ1AVQHaPq5iwRMf6JcI6xP0&index=4&t=1690s) ¿Cómo evitar que se abra la ventana de Chrome?

[28:39](https://www.youtube.com/watch?v=348iLgXfgvk&list=PLheIVUbpfWZ1AVQHaPq5iwRMf6JcI6xP0&index=4&t=1719s) Conclusiones y despedida