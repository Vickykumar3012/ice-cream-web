from django.db import models

# Create your models here.
class Contact(models.Model):
      name = models.CharField(max_length=50)
      email = models.CharField(max_length=50)
      password = models.CharField(max_length=60)
      checkbox = models.BooleanField(blank=True,null=True)
      date = models.DateField(auto_now_add=True) 


      def __str__(self):
            return self.name+" "+self.email