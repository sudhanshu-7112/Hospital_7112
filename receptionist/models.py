from django.db import models

# Create your models here.


class reclogin(models.Model):
    user=models.CharField(max_length=50,null=False, primary_key=True)
    pass1=models.CharField(max_length=15,null=False)

