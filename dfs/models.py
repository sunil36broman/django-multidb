from django.db import models

# Create your models here.
class Customer(models.Model):
	dept = models.CharField(max_length=100)
	emp_id = models.IntegerField()  	
	
	class Meta:
            db_table='customer'
            managed = False
            
# Create your models here.
class Pasenger(models.Model):
	dept = models.CharField(max_length=100)
	emp_id = models.IntegerField()  	
	
	class Meta:
            db_table='pasenger'
            managed = False	

class PasengerContentTypePermission(models.Model):
            
    class Meta:
        
        managed = False  # No database table creation or deletion  \
                         # operations will be performed for this model. 
                
        default_permissions = () # disable "add", "change", "delete"
                                 # and "view" default permissions

        permissions = ( 
            ('customer_pasenger', 'Global customer pasenger'),  
            ('vendor_pasenger', 'Global vendor pasenger'), 
            ('any_pasenger', 'Global any pasenger'), 
        )            		