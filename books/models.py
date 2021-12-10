from django.db import models

class Books(models.Model):
	title = models.CharField(max_length=150)
	author = models.CharField(max_length=100)
	read = models.CharField(max_length=3)

class Category(models.Model):
	title = models.CharField(max_length=150)
	author = models.CharField(max_length=100)
	read = models.CharField(max_length=3)    

class Tag(models.Model):
	title = models.CharField(max_length=150)
	author = models.CharField(max_length=100)
	read = models.CharField(max_length=3) 

class BookAuthor(models.Model):
	title = models.CharField(max_length=150)
	author = models.CharField(max_length=100)
	read = models.CharField(max_length=3)     

class RightsSupport(models.Model):
            
    class Meta:
        
        managed = False  # No database table creation or deletion  \
                         # operations will be performed for this model. 
                
        default_permissions = () # disable "add", "change", "delete"
                                 # and "view" default permissions

        permissions = ( 
            ('customer_rights', 'Global customer rights'),  
            ('vendor_rights', 'Global vendor rights'), 
            ('any_rights', 'Global any rights'), 
        )
			

  	