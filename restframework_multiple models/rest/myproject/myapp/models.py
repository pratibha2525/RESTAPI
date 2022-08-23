from django.db import models

# Create your models here.
class empmodel(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=30)
    emp_course = models.CharField(max_length=30)
    class Meta:
        db_table = "employee"

    

class cricketmodel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    class Meta:
        db_table = "cricket_team"