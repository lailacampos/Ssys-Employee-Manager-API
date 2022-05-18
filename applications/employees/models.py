from datetime import date
from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=250, default='FirstName LastName')
    email = models.EmailField(max_length=250, default='employee@email.com')
    departament = models.CharField(max_length=250, default='Full-Stack')
    salary = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    birth_date = models.DateField(default=date.today)
