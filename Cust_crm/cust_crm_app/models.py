from django.db import models

class Record(models.Model):
    #whenever we will create a record it will get a timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 20)
    address = models.CharField(max_length = 100)
    district = models.CharField(max_length = 20)
    city = models.CharField(max_length = 30)
    state = models.CharField(max_length = 20)
    pincode= models.CharField(max_length = 10)
    country = models.CharField(max_length = 50)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")