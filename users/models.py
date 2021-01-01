from django.db import models


# Create your models here.

class All_Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=20)

    class Meta:
        db_table = "All_Users"
