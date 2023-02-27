# Django Portfolio V3

#### Hola!!!
Bienvenido a el código de mi portafolio. Este se encuentra desarrollado en los siguientes elementos: 
- python V 3.8.10
- Django V 3.2.9.
- bootstrap V 4.5
- inflect V 6.0.2

Esta página tiene las siguientes capacidades:

- Mostrar mi portafolio, con detalles básicos en una página de inicio
- Uso de bases de datos relacionales (Sqlite) para almacenar la información y detalles de esta
- Uso de Admin Site para la administración de la información de la base de datos, manejo sencillo para mostrar la información a traves de los modelos
- Uso del patrón Modelo Vista Controlador para el desarrollo de la aplicación
  - Consultas a las bases de datos para las diferentes vistas
  - Uso de templates y funciones de este para la mostrar la información
  - Uso de bootstrap para dar estética a la página y la información

## Limitaciones

Soy consciente de que debería tener la capacidad de crear usuarios nuevos y gestionar su propia página web. Sería lo ideal, pero mi objetivo principal es resaltar mi portafolio. Si cuento con el tiempo me gustaría añadir este elemento.
Quizás falten elementos en la base de datos que quizás también son esenciales|, invito a notificar para realizar el cambio que corresponda.
Uso de bases de datos como Mysql o Postgresql. No cuento con experiencia para lanzar una base de datos en una plataforma, tengo conocimientos en AWS de Amazon, pero no voy a poner mi tarjeta en un servicio que cuenta con poco uso

## Instalación

Se requiere python V 3.8. Utilizando siempre la consola, se descarga el proyecto a través del servicio de Github:

```sh
git clone git@github.com:SergioParraC/Mi-pagina-web-v3.git
```

Se dirije a la carpeta que contiene el proyecto

```sh
cd Mi-pagina-web-v3
```

Instala los elementos requeridos usando el archivo _requirements.txt_

```sh
pip install -r /path/to/requirements.txt
```

Iniciamos el servidor local

```sh
python3 manage.py runserver
```

Ya podemos acceder al servidor local ubicado por defecto en [http://127.0.0.1:8000/]

Si quiere observar el contenido de la base de datos, usted tiene el acceso para visualizar ingresando a [http://127.0.0.1:8000/admin/] a través de las siguientes credenciales:

**Nombre de usuario:** invitado
**Contraseña:** v12345678


> Nota: Este proyecto se desarrolló como parctica y hobbie :D
