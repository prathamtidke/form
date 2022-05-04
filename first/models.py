from django.db import models

class Details(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Age = models.IntegerField()
    Location = models.CharField(max_length=50)

    def __str__(self):
        return self.Firstname

    
