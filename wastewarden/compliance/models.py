from django.db import models
from accounts.models import Organization

class ComplianceViolation(models.Model):
    hospital = models.ForeignKey(Organization, on_delete=models.CASCADE)
    violation_type = models.CharField(max_length=200)
    description = models.TextField()
    severity = models.CharField(max_length=20)
    detected_on = models.DateField()
    status = models.CharField(max_length=20, default="OPEN")
