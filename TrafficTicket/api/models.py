from django.db import models
from django.contrib.auth.models import User

#done
class Admin(models.Model):
    police_station = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

#done
class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=7, primary_key=True)
    chassis_number = models.CharField(max_length=20)
    engine_number = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    license_expiry_date = models.DateField()

#done
class VehicleOwner(models.Model):
    vehicle_number = models.OneToOneField('Vehicle', primary_key=True, on_delete=models.CASCADE)
    nic = models.ForeignKey('Driver', on_delete=models.CASCADE)

#done
class Fine(models.Model):
    fine_id = models.AutoField(primary_key=True)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
    time = models.TimeField()
    date = models.DateField()
    violation = models.ForeignKey('ViolationType', on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    due_date = models.DateField()
    payment_status = models.BooleanField()

#driver
class Driver(models.Model):
    nic = models.OneToOneField('Person', primary_key=True, on_delete=models.CASCADE)
    license_id = models.CharField(max_length=8)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

#done
class Person(models.Model):
    nic = models.CharField(max_length=12, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    telephone = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=200, null=True)

#done
class Accident(models.Model):
    index = models.AutoField(primary_key=True)
    time = models.TimeField()
    date = models.DateField()
    location = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    reporter = models.ForeignKey('Driver', on_delete=models.CASCADE)



class Message(models.Model):
    index = models.AutoField(primary_key=True)
    sender_nic = models.CharField(max_length=12)
    timestamp = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=1000)



#done
class PoliceOfficer(models.Model):
    nic = models.OneToOneField('Person', primary_key=True, on_delete=models.CASCADE)
    police_station = models.CharField(max_length=20)
    officer_id = models.CharField(max_length=10, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


#done
class ViolationType(models.Model):
    violation_id = models.AutoField(primary_key=True)
    violation_type = models.CharField(max_length=50)
    fine_amount = models.DecimalField(max_digits=10, decimal_places=2)



# done
class Violation(models.Model):
    index = models.AutoField(primary_key=True)
    violation = models.ForeignKey('ViolationType', on_delete=models.CASCADE)
    time = models.TimeField()
    date = models.DateField()
    location = models.CharField(max_length=50)
    original_image = models.BinaryField()
    vehicle_image = models.BinaryField()
    license_plate_image = models.BinaryField()
    detected_license_plate = models.CharField(max_length=7)


class Suggestion(models.Model):
    id = models.AutoField(primary_key=True)
    suggestion = models.CharField(max_length=5000)


class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    officer = models.ForeignKey('PoliceOfficer', on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    shift = models.CharField(max_length=5)
    date = models.DateField()
    police_station = models.CharField(max_length=20, null=True)

class VehicleAccident(models.Model):
    accident = models.ForeignKey('Accident', on_delete=models.CASCADE)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)


class OTPVerification(models.Model):
    id = models.AutoField(primary_key=True)
    nic = models.CharField(max_length=12)
    otp = models.CharField(max_length=6)
    timestamp = models.DateTimeField(auto_now_add=True)

class OfficerLocation(models.Model):
    police_station = models.CharField(max_length=20)
    location = models.CharField(max_length=50)

class CameraLocation(models.Model):
    police_station = models.CharField(max_length=20)
    location = models.CharField(max_length=50)