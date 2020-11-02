from django.db import models

class Customer(models.Model):
    Name = models.CharField(max_length=100)
    Address = models.TextField()
    Email = models.EmailField()
    Contact = models.IntegerField()
    Status = models.BooleanField(default=False)
    Password = models.CharField(max_length=15)
    Date=models.DateField()
    Reg_Id = models.AutoField(primary_key=True,default=1)
       
