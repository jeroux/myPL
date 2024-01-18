# Generated by Django 4.2.9 on 2024-01-18 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geronte', '0006_remove_sideeffectsrisks_patient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sideeffectsrisks',
            name='category',
            field=models.CharField(choices=[('Allergy', 'Allergy'), ('Medication on admission', 'Medication on admission'), ('Substance use', 'Substance use')], max_length=200),
        ),
    ]
