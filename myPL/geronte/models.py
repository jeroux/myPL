from django.db import models

CATEGORY_SIDE_EFFECTS = (
    ('Allergy', 'Allergy'),
    ('Medication', 'Medication on admission'),
    ('Substance_use', 'Substance use'),
)

class Patient(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(null=True, blank=True)
    drugs_allergies = models.ForeignKey(to='SideEffectsRisks', on_delete=models.CASCADE, null=True, blank=True)

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    specialty = models.CharField(max_length=200)
    patients = models.ManyToManyField(Patient)

class SideEffectsRisks(models.Model):
    category = models.CharField(
        max_length=200,
        choices=CATEGORY_SIDE_EFFECTS
    )
    description = models.TextField()
    
    
