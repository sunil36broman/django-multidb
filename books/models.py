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


			

  	