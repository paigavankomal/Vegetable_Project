from django.db import models
from datetime import *
Item_CHOICES = (
        ("0",'---select item----'),
        ("10",'Potates'),
        ("20",'Tomotoes'),
        ("30",'Onion'),
        ("40",'Cabbage'),
        ("50",'Apple'),
    )
# Create your models here.
class Billing(models.Model): #this is class for creating  table in database
    #Attributes:
    
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    address=models.CharField(max_length=50,default='dd')
    email=models.EmailField(max_length=50)
    mobile=models.CharField(max_length=50)
    Payable_amt=models.IntegerField(max_length=50)
    item=models.CharField(max_length=50,choices=Item_CHOICES, default='0')
    qty=models.IntegerField(max_length=50)
   
   

