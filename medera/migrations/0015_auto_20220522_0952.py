# Generated by Django 2.0.7 on 2022-05-22 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medera', '0014_auto_20220522_0741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='doctor',
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(default='Male', max_length=6),
        ),
    ]
