from django.db import models


# Create your models here.
class webuser(models.Model):
    login_name = models.CharField(max_length=10, primary_key=True)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = "webUser"
