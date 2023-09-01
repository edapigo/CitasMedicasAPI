from django.db import models
from django.contrib.auth.models import User

# Seguro mmedico
class HealthInsurance(models.Model):
    code = models.CharField(max_length=25)
    name = models.CharField(max_length=100)

# Especialidad
class Specialty(models.Model):
    code = models.CharField(max_length=25)
    name = models.CharField(max_length=100)

class Experience(models.Model):
    description = models.CharField(max_length=250)
    name = models.CharField(max_length=100)

# Profile
class Profile(models.Model):
    PATIENT = "PT"
    DOCTOR = "DR"
    EMPLOYEE = "EM"
    ADMIN = "AD"

    TYPE_USER = [
        (PATIENT, "Paciente"),
        (DOCTOR, "Doctor"),
        (EMPLOYEE, "Empleado"),
        (ADMIN, "Administrador"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type_user = models.CharField(
        max_length=2,
        choices=TYPE_USER,
        default=PATIENT,
    )
    cedula = models.CharField(max_length=13)
    age = models.IntegerField(default=0)
    is_collaborator = models.BooleanField()

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.OneToOneField(Specialty, on_delete=models.CASCADE)

class ExperienceDoctor(models.Model):
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    experience = models.OneToOneField(Experience, on_delete=models.CASCADE)

class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='paciente', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.name


class Hospital(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.address


class OfficeHours(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    DIA_DOMINGO = 'DO'
    DIA_LUNES = 'LU'
    DIA_MARTES = 'MA'
    DIA_MIERCOLES = 'MI'
    DIA_JUEVES = 'JU'
    DIA_VIERNES = 'VI'
    DIA_SABADO = 'SA'
    DIA_SEMANA_CHOICES = (
        (DIA_DOMINGO, 'Domingo'),
        (DIA_LUNES, 'Lunes'),
        (DIA_MARTES, 'Martes'),
        (DIA_MIERCOLES, 'Miercoles'),
        (DIA_JUEVES, 'Jueves'),
        (DIA_VIERNES, 'Viernes'),
        (DIA_SABADO, 'Sabado'),
    )
    day_of_week = models.CharField(
        max_length=2,
        choices=DIA_SEMANA_CHOICES,
        default=DIA_LUNES,
    )
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.day_of_week


class Appointment(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_app = models.DateField()
    hour_app = models.TimeField()


class Diagnosis(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_dg = models.DateField()
    hour_dg = models.TimeField()
    description = models.TextField()
    treatment = models.TextField()


class Billing(models.Model):
    DEBIT = 'DB'
    CREDIT = 'CR'
    CASH = "CA"
    TYPE_CARD = (
        (DEBIT, 'Tarjjeta de debito'),
        (CREDIT, 'Tarjeta de credito'),
        (CASH, 'EFECTIVO'),
    )

    number = models.CharField(max_length=50, default = '0001')
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    paymennt_methods = models.CharField(
        max_length=2,
        choices=TYPE_CARD,
        default=CASH,
    )
# Create your models here.

class Admin1(models.Model):
    usuario= models.CharField(max_length=100)
    correo = models.EmailField((""), max_length=254)
    contraseña = models.CharField(max_length=100)
    def __str__(self):
      return self.usuario

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveSmallIntegerField()
    correo = models.CharField(max_length=100, default=" ")
    alergia = models.CharField(max_length=100, default=" ")
    
    


class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveSmallIntegerField()
    especialidad= models.CharField(max_length=100)
   


class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    


class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    costo = models.PositiveSmallIntegerField()
