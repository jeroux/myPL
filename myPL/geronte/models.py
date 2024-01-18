from django.db import models

CATEGORY_SIDE_EFFECTS = (
    ('Allergy', 'Allergy'),
    ('Medication on admission', 'Medication on admission'),
    ('Substance use', 'Substance use'),
)

class Patient(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(null=True, blank=True)

class SideEffectsRisks(models.Model):
    category = models.CharField(
        max_length=200,
        choices=CATEGORY_SIDE_EFFECTS
    )
    description = models.TextField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
    
