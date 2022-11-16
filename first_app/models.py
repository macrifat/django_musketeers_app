from django.db import models

# Create your models here.

class Members(models.Model):
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50)
    phone_number = models.IntegerField()
    email = models.EmailField()
    
    
    def __str__(self) -> str:
        return str(self.pk) + " "+ self.first_name+ " "+ self.last_name