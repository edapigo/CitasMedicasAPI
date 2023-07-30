from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import *

# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "profile"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]

# class PatientAdmin(admin.ModelAdmin):
#     list_filter = ('name',)
#     search_fields = ('name',)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(HealthInsurance)
admin.site.register(Specialty)
admin.site.register(Experience)
admin.site.register(Doctor)
admin.site.register(ExperienceDoctor)
admin.site.register(Patient)
admin.site.register(Hospital)
admin.site.register(OfficeHours)
admin.site.register(Appointment)
admin.site.register(Diagnosis)
admin.site.register(Billing)

# admin.site.register(Admin1)
# admin.site.register(Cita)
# admin.site.register(Medicamento)
# admin.site.register(Paciente)
# admin.site.register(Medico)

# admin.site.register(Patient, PatientAdmin)