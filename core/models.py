from django.db import models
from django.contrib.auth.models import User
# Create your models here.


#Patient Profile
class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    status = models.CharField(max_length=20, default="Active")

    def __str__(self):
        return self.full_name



#Doctor Profile
class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=20, default="Active")

    def __str__(self):
        return self.user.username


#Lab Technician Profile
class LabTechnicianProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=20, default="Active")

    def __str__(self):
        return self.user.username


#Front Desk (Reception)
class FrontDeskProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=20, default="Active")

    def __str__(self):
        return self.user.username


#Admin Profile
class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


#Appointments
class Appointment(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason = models.CharField(max_length=255)
    status = models.CharField(max_length=20, default="Scheduled")
    created_at = models.DateTimeField(auto_now_add=True)


#Prescriptions
class Prescription(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=150)
    dosage = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


#Labs
class Lab(models.Model):
    name = models.CharField(max_length=150)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=20, default="Active")
    created_at = models.DateTimeField(auto_now_add=True)


#Diagnostic Tests
class DiagnosticTest(models.Model):
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


#Test Booking
class TestBooking(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    test = models.ForeignKey(DiagnosticTest, on_delete=models.CASCADE)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    booking_date = models.DateField()
    status = models.CharField(max_length=20, default="Booked")
    created_at = models.DateTimeField(auto_now_add=True)


#Lab Results
class LabResult(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    lab_technician = models.ForeignKey(LabTechnicianProfile, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=150)
    test_value = models.CharField(max_length=100)
    normal_range = models.CharField(max_length=100)
    result_status = models.CharField(max_length=20)
    remarks = models.TextField()
    test_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)


#Payments
class Payment(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=20)
    payment_date = models.DateTimeField(auto_now_add=True)


#Login History
class LoginHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=50)
    device_info = models.CharField(max_length=255)


#Patient Medical 
class PatientHistory(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    treatment = models.TextField()
    notes = models.TextField()
    recorded_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)


