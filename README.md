# URL Shortener

Este proyecto es una implementación de un servicio de acortador de URL utilizando Flask y SQLite. La API cuenta con dos endpoints principales: uno para generar un shortcode a partir de una URL dada y otro para redirigir al usuario a la URL original utilizando el shortcode.

## Requisitos

- Python 3.10
- Miniconda
- Flask 2.1.1
- Flask-SQLAlchemy 2.5.1
- pytest 6.2.5
- pytest-flask 1.2.0
- requests 2.30.0

## Instalación y configuración del entorno

### 1. Clone el repositorio:
```
git clone https://github.com/yourusername/url-shortener.git
cd url-shortener
```

### 2. Instale Miniconda siguiendo las instrucciones en:
https://docs.conda.io/en/latest/miniconda.html.

### 3. Cree un entorno virtual con Miniconda:
```
conda create -n url-shortener python=3.10
conda activate url-shortener
```

### 4. Instale las dependencias del proyecto:

```
pip install -r requirements.txt
```

## Inicializar la base de datos

Ejecute el siguiente comando para crear e inicializar la base de datos SQLite:
```
python init_db.py
```

## Ejecutar la aplicación localmente

Inicie la aplicación ejecutando el siguiente comando:
```
python main.py
```

La aplicación estará disponible en `http://localhost:5000`.

## Probar la API

Puede utilizar herramientas como Postman, cURL o su navegador web para probar la API.

Ejemplo de una solicitud POST para acortar una URL con Python utilizando el archivo 'simple_test.py':

Puede modificar la variable "data" para utilizar diferentes urls
```
python simple_test.py
```

## Estructura del proyecto
```
url_shortener/
  ├── app/
  │   ├── __init__.py
  │   ├── models.py
  │   ├── services.py
  │   ├── test_views.py
  │   ├── utils.py
  │   └── views.py
  ├── .gitignore
  ├── config.py
  ├── init_db.py
  ├── LICENCE
  ├── main.py
  ├── README.md
  ├── requirements.txt
  ├── simple_test.py
  └── url_shortener.db
```

## Ejecutar pruebas

Ejecute las pruebas con el siguiente comando:
```
pytest
```

## Decisiones de diseño y tecnología

- Se eligió Python 3.10 debido a sus características mejoradas y compatibilidad con las últimas bibliotecas y tendencias en Python.
- Flask se utiliza como framework debido a su simplicidad y facilidad de uso para desarrollar aplicaciones web rápidamente.
- SQLite se utiliza como base de datos por su simplicidad y facilidad de configuración en un entorno local.
- Pytest se utiliza como herramienta de testing gracias a su facilidad de uso para pruebas en aplicaciones Flask.

## Contribuciones y mejoras

Siéntase libre de contribuir o sugerir mejoras a este proyecto mediante la creación de un Issue o un Pull Request en GitHub.

## Funcionalidad adicional añadida

**Evitar duplicados**: Se verifica si una URL ya existe en la base de datos y ofrecer el shortcode existente en lugar de generar uno nuevo. Esto ayuda a evitar duplicados innecesarios en la base de datos y conserva los recursos.

## Funcionalidad adicionales que podrián implementarse

**Personalización del shortcode**: Permitir a los usuarios personalizar su propio shortcode. Esto da la oportunidad de elegir algo más memorable o relacionado con su negocio o marca.

**Estadísticas de clics**: Llevar un registro de la cantidad de veces que se ha visitado un shortcode y proporcionar estadísticas básicas de clics al propietario de la URL acortada o a la misma URL.

**Fecha de vencimiento de los shortcodes**: Permitir a los usuarios establecer una fecha de vencimiento para sus shortcodes (O uno por default). Después de la fecha de vencimiento, el shortcode ya no redirigirá a la URL original.

**Autenticación de usuario**: Requerir que los usuarios se registren e inicien sesión para utilizar el servicio de acortamiento de URLs. Esto te permitirá asociar los shortcodes con los usuarios, y posiblemente ofrecer funciones adicionales, como la edición o eliminación de shortcodes.

## SIN PUNTOS EXTRA

Decidí utilizar Flask envés de Serverless Framework y AWS Lambda por varios motivos:

**Facilidad de desarrollo**: Flask es un micro-framework muy conocido y ampliamente utilizado que facilita la creación de aplicaciones web en Python. Su simplicidad y flexibilidad permiten un desarrollo rápido y eficiente de la funcionalidad requerida en este desafío.

**Portabilidad**: Al utilizar Flask, la aplicación es portable y se puede desplegar fácilmente en cualquier entorno que soporte Python. Esto significa que, aunque no se haya utilizado Serverless framework y AWS Lambda en este caso, la adaptación a esos entornos (o cualquier otro) es bastante sencilla si se requiere en el futuro.

**Costo**: Utilizar Flask y SQLite permite mantener los costos de infraestructura y despliegue al mínimo. Además, durante el desarrollo y las pruebas, no es necesario incurrir en costos asociados con AWS Lambda y otros servicios en la nube.

**Escalabilidad**: Para este challenge en particular, la implementación de una aplicación Flask es más que suficiente para satisfacer los requisitos de escalabilidad. Si bien AWS Lambda puede proporcionar beneficios de escalabilidad adicionales, estos podrían no ser necesarios en este caso y podrían complicar innecesariamente la solución.

## CON PUNTOS EXTRA

Se realizo la implementación adecuada con Serverless Framework y AWS Lambda con DynamoDB para cumplir los "puntos extra" del challenge.

# Deploy para AWS (Plantilla-Pasos)

## Requisitos

- AWS CLI
- Serverless Framework
- npm
- boto3

## Configurar AWS CLI:

Instala AWS CLI (Command Line Interface) en tu máquina local. Después de instalar AWS CLI, tendrás que configurar tus credenciales de AWS utilizando *aws configure* para poder interactuar con tu cuenta de AWS desde tu línea de comandos.

## Instalar npm:

Instala npm globalmente en tu máquina local siguiendo los pasos de instalacion en: https://nodejs.org/en/download

## Instalar Serverless Framework

Instala Serverless Framework globalmente en tu máquina local usando npm con npm install -g serverless.

## Crear un nuevo servicio Serverless
```
serverless create --template aws-python3 --path url_shortener.
```

## Estructura de directorios

Navega a tu nuevo servicio. Encontrarás un archivo serverless.yml y un archivo handler.py. El archivo **serverless.yml** es donde defines tu infraestructura y el **handler.py** es donde escribes tu código de Python.

## Definir la infraestructura

En el archivo serverless.yml, debes definir tus funciones de Lambda y cualquier recurso adicional, como la tabla de **DynamoDB**, que necesitarás para tu servicio. Las funciones que definirías serían la función que crea la URL corta y la función que redirige a la URL original a partir de la URL corta. Estas funciones se referirían a los métodos en tu handler.py.

## Implementar la lógica de la aplicación:

En el archivo **handler.py**, implementas la lógica para acortar la URL y redirigir a la URL original. Utilizarías el SDK de AWS para Python (boto3) para interactuar con DynamoDB.

## Desplegar el servicio
Una vez que hayas definido tu infraestructura y escrito tu lógica de aplicación, puedes desplegar tu servicio con
```
serverless deploy
```

# Deploy en AWS url_shortener

Crear-tener cuenta en AWS, instalar el cli de aws y utilizar aws configure, este tendra varios prompts los cuales te pedira:

### AWS Access Key ID

Este lo puedes encontrar al buscar en los servicios de AWS como **IAM console**, dentro de la misma en la seccion de **Access keys** crear una nueva, ahi mismo encontraras el *Access key ID* que pide en este prompt

### AWS Secret Access Key
Lo encontraras alado de la *Access key ID*

### Default region name
Esta es la región donde se encontrarán los servicios, te recomiendo basarte en la posición geográfica más cercana al objetivo del proyecto, en este caso puedes encontrar las regiones en la parte superior derecha al lado de tu nombre de usuario y desplegar la lista de regiones, el texto que debes poner es la cadena a la derecha de la región, ejemplo:

US East (Ohio) --> **us-east-2**

### Default output format
Este simplemente poner **json**

## Serverless framework
Crear el nuevo servicio con Serverless framework
```
serverless create --template aws-python3 --path url_shortener.
```

### Configurar Serverless Framework (serverless.yml)
Modificar las varibles:
- service (nombre del servicio)
- region
- functions (estas dependen del handler.py)
- resources (conforme al recurso utilizado, este caso DynamoDB)

### Implementar la lógica de la aplicación (handler.py):
Se implementa la lógica para acortar la URL y redirigir a la URL original. Utilizando el SDK de AWS para Python (boto3) para interactuar con DynamoDB.

## Desplegar el servicio:

Para desplegar el servicio, ejecutar **serverless deploy** en la raíz de tu directorio. Este comando crea la infraestructura necesaria en AWS, incluyendo las funciones de AWS Lambda y la tabla de DynamoDB (las cuales puedes visualizar en el portal de AWS).

## Probar el servicio
Utilizando el archivo *aws/url_shortener/simple_test.py* se puede probar el servicio en "vivo", requiriendo actualizar las urls de los metodos POST y GET, puedes obtener esto a partir del resultado del comando *sls deploy*, o visitando la consola de AWS API Gateway y buscando el API correspondiente.

## Desarrollo a futuro
- Implementar pytest en el servicio de Serverless Framework.
- Implementar el uso de herramientas CI/CD para utilizar esta guia en proyectos mas robustos.

## Beneficios de implementar el servicio con Serverless Framework en AWS

**Escalabilidad automática**: Una de las principales ventajas de AWS Lambda (y el cómputo sin servidor en general) es que escala automáticamente para manejar la carga de trabajo. No necesitas preocuparte por la administración de servidores o por decidir cuántos recursos reservar para tu aplicación.

**Costos basados en el uso**: Con AWS Lambda, solo pagas por el tiempo de cómputo que utilizas. Esto puede ser mucho más eficiente en términos de costos que pagar por un servidor dedicado que puede no estar en uso todo el tiempo.

**Desarrollo centrado en el producto**: Al usar Serverless Framework y AWS Lambda, puedes centrarte más en el desarrollo de tu aplicación y menos en la infraestructura subyacente. Esto puede acelerar el tiempo de desarrollo y permitirte lanzar nuevas características y actualizaciones más rápidamente.

**Mantenimiento reducido**: No tienes que preocuparte por parchar los servidores o mantener la infraestructura actualizada. AWS se encarga de todo esto por ti.

**Integraciones y servicios complementarios de AWS**: Al usar AWS, tienes acceso a una amplia gama de servicios y características adicionales que puedes integrar fácilmente en tu aplicación, como AWS DynamoDB para bases de datos, AWS S3 para almacenamiento, AWS CloudWatch para supervisión y registro, etc.

**Seguridad**: AWS ofrece una gran cantidad de características de seguridad, como la gestión de identidades y acceso, cifrado en reposo y en tránsito, y muchas otras que ayudan a proteger tu aplicación.

**Implementación y desarrollo sencillos con Serverless Framework**: Esta herramienta facilita la configuración y despliegue de tu aplicación, permitiendo un desarrollo más rápido y una mayor productividad. También apoya las mejores prácticas de DevOps, como la infraestructura como código.

## Licencia

Este proyecto está licenciado bajo la licencia MIT.