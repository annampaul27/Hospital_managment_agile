from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Lab)
admin.site.register(Appointment)
admin.site.register(DiagnosticTest)
admin.site.register(Prescription)
admin.site.register(MedicalHistory)
admin.site.register(Payment)
