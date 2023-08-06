from django.db import models

# Create your models here.
class all_tasks(models.Model):
    id = models.AutoField
    name = models.CharField(max_length= 500)
    description = models.CharField(max_length= 500)
    start_date = models.DateField()
    end_date = models.DateField()
    priority = models.IntegerField()
    category = models.CharField(max_length=500)
