from django.db import models
from django.contrib.auth.models import AbstractUser

class Organization(models.Model):
    ORG_TYPES = [
        ('HOSPITAL', 'Hospital'),
        ('CLINIC', 'Clinic'),
        ('LAB', 'Laboratory'),
        ('COLLECTOR', 'Collector'),
        ('TREATMENT', 'Treatment Facility'),
        ('REGULATOR', 'Regulator'),
    ]

    name = models.CharField(max_length=200)
    org_type = models.CharField(max_length=20, choices=ORG_TYPES)
    registration_number = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class User(AbstractUser):
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('STAFF', 'Staff'),
        ('COLLECTOR', 'Collector'),
        ('INSPECTOR', 'Inspector'),
        ('REGULATOR', 'Regulator'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True)
