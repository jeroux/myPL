# Generated by Django 4.2.9 on 2024-01-17 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geronte', '0003_alter_patient_drugs_allergies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='drugs_allergies',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geronte.sideeffectsrisks'),
        ),
    ]
