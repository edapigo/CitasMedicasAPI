# Citas médicas api - Configuración y Ejecución

Este archivo proporciona los pasos necesarios para configurar y ejecutar el proyecto Django. Asegúrate de seguir los pasos en el orden indicado para evitar problemas.

## Pasos

1. **Crear y activar el entorno virtual|**

   ```bash
   python -m venv venv
   ```
   Para Windows:
   ```bash
   .\venv\Scripts\activate
   ```
   Para macOS/Linux:
   ```bash
   source venv/bin/activate
   ```
2. **Instalar las dependencias**
   ```bash
   pip install -r requirements.txt
   ```
4. **Aplicar las migraciones**
   ```bash
   python manage.py migrate
   ```
5. **Crear el superusuario**
   ```bash
   python manage.py createsuperuser
   ```
   Se te solicitará ingresar un nombre de usuario, un correo electrónico y una contraseña para el superusuario.

   Por ejemplo:
   ```txt
   Username: JordanVillao
   Email: admin@gmail.com
   Password: 123
   ```
6. **Ejecutar el servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```
   El servidor se ejecutará en [http://localhost:8000](http://localhost:8000) por defecto.
   
   Para revisar el **swagger** consultar en  en [http://localhost:8000/swagger/](http://localhost:8000/swagger)

**Nota:** Asegúrate de tener Python instalado en tu sistema antes de comenzar con estos pasos.
