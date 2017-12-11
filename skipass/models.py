from django.db import models

# Create your models here.
class Skipass(models.Model):
    uid = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=19)
    price = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    time_from = models.CharField(max_length=10)
    time_to = models.CharField(max_length=10)

    def __str__(self):
        return self.name


