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

## Licencia

Este proyecto está licenciado bajo la licencia MIT.