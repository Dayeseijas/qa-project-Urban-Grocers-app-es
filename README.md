# Proyecto de pruebas automatizadas para la API de Urban Grocers 

El presente proyecto consiste en la realización de un conjunto de pruebas automatizadas para Urban Grocers.
Las pruebas se centran en la verificación y correcto funcionamiento de la API, ejecutandose pruebas positivas y negativas
referentes a la creación del kit.

# Descripción del proyecto
Como objetivo principal del proyecto, se tiene el garantizar la calidad y fiabilidad de la aplicación Urban Grocers mediante la automatización
de pruebas, consiguiendose mediante la creación de las mismas a través del código en lenguaje Python que permite verificar el comportamiento
de la API en variadas situaciones que incluen: casos de uso común, situaciones límites y errores.

# Documentación

La fuente de documentación empleada ha sido, y se encuentra generada, mediante APIDocs. Herramienta que permite generar documentación
a partir de de comentarios en código fuente.

# Tecnologías y Técnicas Utilizadas

Para desarrollar el proyecto se ha recurrido a lo siguiente:
- Uso de Pycharm, empleando a Python como lenguaje principal para escribir las pruebas autoatizadas.
- Librería pytest, la cual permitió escribir y ejecutar pruebas de forma eficiente y organizada.
- Librería requests, utilizada para la realización de solicitudes HTTP a la API para verificar las respuestas de la misma.
- Librería JSON, la cual permite y facilita el intercambio de datos entre diferentes sistemas y almacenamiento
de datos, logrando trabajar así con objetos en notación JavaScript, permitiendo representar los datos enviados y recibidos por la API
- Se ha empleado una función que realiza una lógica separada, tanto para pruebas positivas como para pruebas negativas

Cabe mencionar que la estructura del presente proyecto emplea los siguientes archivos y carpetas:
- data.py: Contiene los datos de prueba utilizadas en las pruebas automatizadas.
- sender_stand_request.py: Contiene funciones para enviar solicitudes y procesar respuestas de la API.
- configuration.py: Contiene la configuración del entorno de prueba, donde se incluye la URL base, creación de usuario y creación de kit.

# Conclusiones
Cuatro de nueve pruebas arrojaron error según resultado esperado. 