from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Planer(models.Model):
    autor=models.ForeignKey(User,on_delete=models.CASCADE)
    tekst=models.CharField(max_length=40)
    zavrsen=models.BooleanField(default=False)

    def __str__(self):
        return self.tekst

    def get_absolute_url(self):
        return reverse("planer_detaljno", args=[str(self.id)])
    
    