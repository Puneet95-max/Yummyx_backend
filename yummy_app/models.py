from django.db import models

class  chef_table(models.Model):
    id = models.IntegerField(primary_key=True)
    src = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    description = models.TextField()
    
    def __str__(self):
      return f"{self.name}"
    
class  testimonial_table(models.Model):
     id = models.IntegerField(primary_key=True)
     description = models.TextField()
     name= models.CharField(max_length=250)
     position = models.CharField(max_length=250)
     src = models.CharField(max_length=250)
     
     def __str__(self):
       return self.name
  
    
