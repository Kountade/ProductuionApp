from django.db import models

# Create your models here.
class Blog(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(max_length=5000)
    image = models.ImageField()
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.titre
class Service(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(max_length=5000)
    image = models.ImageField()
  
    def __str__(self):
        return self.titre