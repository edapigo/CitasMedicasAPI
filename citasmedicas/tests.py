# from django.test import TestCase

# tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Medico, Paciente
import requests_mock

class MedicoViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        Medico.objects.create(nombre="Jordan", apellido="Villao", edad=21, especialidad="Doctor")

    def test_obtener_todos_los_medicos(self):
        # Simulamos la respuesta de la API externa para obtener datos de médicos
        datos_medicos_simulados = [
            {'id': 1, 'nombre': 'Juan', 'edad': 30},
            {'id': 2, 'nombre': 'María', 'edad': 35},
        ]
        
        # Utilizamos requests_mock para simular la solicitud HTTP a la API externa
        with requests_mock.Mocker() as mock_request:
            mock_request.get('http://api.externa.com/medicos/', json=datos_medicos_simulados)
            
            # Realizamos la solicitud a nuestra API
            response = self.client.get('http://localhost:8000/api/Medical/Medico/')
            
            # Aseguramos que la solicitud se haya realizado correctamente (HTTP 200)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            
            # Verificamos que los datos de médicos simulados se devuelvan en la respuesta
            self.assertEqual(response.data, datos_medicos_simulados)

class PacienteViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        Paciente.objects.create(nombre="Anthony", apellido="Ramirez", edad=22, correo="anthony@gmail.com", alergia="Dolor de la vista")

    def test_obtener_todos_los_pacientes(self):
        # Simulamos la respuesta de la API externa para obtener datos de pacientes
        datos_pacientes_simulados = [
            {'id': 1, 'nombre': 'Laura', 'edad': 28},
            {'id': 2, 'nombre': 'Carlos', 'edad': 32},
        ]
        
        # Utilizamos requests_mock para simular la solicitud HTTP a la API externa
        with requests_mock.Mocker() as mock_request:
            mock_request.get('http://api.externa.com/pacientes/', json=datos_pacientes_simulados)
            
            # Realizamos la solicitud a nuestra API
            response = self.client.get('http://localhost:8000/api/Medical/Paciente/')
            
            # Aseguramos que la solicitud se haya realizado correctamente (HTTP 200)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            
            # Verificamos que los datos de pacientes simulados se devuelvan en la respuesta
            self.assertEqual(response.data, datos_pacientes_simulados)
