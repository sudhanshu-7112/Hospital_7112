# Generated by Django 2.0.7 on 2022-05-22 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medera', '0013_patient_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientrecord',
            name='appointments',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
