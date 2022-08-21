from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=100,null=True)
    student = models.IntegerField()

    def __str__(self):
        return self.name