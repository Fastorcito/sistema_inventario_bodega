# Sistema de inventarios para Testing
**Modulo que simula sistema de inventarios para varias bodegas,** está aplicación web está contruida con el framework Django y con MySQL para ejecutarlo de forma local

## Instalación
Se requiere tener instalado un servicio de MySQL y Python 3.11.9, puedes usar el gestor de entornos virtuales de su preferencia.

Una vez preparado el entorno virtual, posicionate en la carpeta donde se encuentra el proyecto en su entorno local.

### Conda
Si está usando el gestor de entornos virtuales anaconda use el siguiente comando:
```sh
conda install --file requirements.txt
```

### Pip
Si está usando usando otro gestor de entornos virtuales puede usar el siguiente comando:
```sh
pip install -r requirements.txt
```

## Ejecución
Ingrese a **sistema_inventario_bodega/settings.py** y actualiza las credenciales para ingresar a su base de datos.

Use el siguiente comando para migrar los modelos a la base de datos:
```sh
python manage.py migrate
```

Para ejecutar la aplicación de Django use el siguiente comando:
```sh
python manage.py runserver
```

## Panel de Administrador
Para crear un superusuario y poder entrar en el panel de administrador debe uasr el siguiente comando:
```sh
python manage.py createsuperuser
```

Luego dirigete a la url localhost:8000/admin


### Gracias :D