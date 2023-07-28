# Proyecto-SIPAU
Sistema web m&eacute;dico donde podras:

1. Reservar citas medicas.
2. Registrar usuarios (clientes, empleados)
3. Ingreso de doctores
4. Especialidades
5. Facturaci&oacute;n 

y mucho m&aacute;s, proyecto realizado con el framework **Django** y **python**.


### Configuraci&oacute;n entorno virtual

##### Pasos Opcionales
Se recomienda crear un entorno virtualizado para no compremeter el real, pero es opcional dependera de cada persona.

1. instalar venv (Opcional)
`pip install virtualenv`

2. crear entorno virtualizado (Opcional)
`python -m virtualenv ven`

3. Activar entorno
`./venv/Scripts/Activate`

##### Pasos obligatorios del proyecto

1. Instalar Django
`pip install django`

2. Una ves descarago, crear su usuario
`python-admin createsuperuser`

Puede ser cualquiera por ejemplo:

> usuer: JordanVillao (ejemplo)
>> email: admin@gmail.com
>>> contraseña: 123

3. Mover las carpetas al sistema

4. Ejecutar migraciones
> `python magane.py migrate`
>> `python manage.py makemigrations`
>>> `python magane.py migrate`

4. Levantar el servidor
`python manage.py runserver`

=============================================
##### SI LES SALE ERROR
Puede ser por varias razones entre ellas puede faltar el restframework
1. Instalar
`pip install djangorestframework`
2. Instalar descargar coreapi 
`pip install coreapi`
3. Tambien instalar drf_yasg para swagger
`pip install -U drf-yasg`

4. Ejecutar migraciones
> `python magane.py migrate`
>> `python manage.py makemigrations`
>>> `python magane.py migrate`

Listo **happing coding ;)**