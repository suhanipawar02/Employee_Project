from django.db import models

class Employee(models.Model):
    ename = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobno = models.CharField(max_length=15, unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

 

    class Meta:
        db_table = 'employeedata'
