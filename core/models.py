from django.db import models
class User(models.Model):
    ROLE_CHOICES = [
        ('Patient', 'Patient'),
        ('Doctor', 'Doctor'),
        ('Lab Technician', 'Lab Technician'),
        ('Admin', 'Admin'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email
    
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    details = models.TextField()

    def __str__(self):
        return self.user.email

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.user.email
class Lab(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.patient} - {self.doctor}"
class DiagnosticTest(models.Model):
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
class Prescription(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    details = models.TextField()

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

