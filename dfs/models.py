from django.db import models

# Create your models here.
class Customer(models.Model):
	dept = models.CharField(max_length=100)
	emp_id = models.IntegerField()  	
	
	class Meta:
			db_table='customer'