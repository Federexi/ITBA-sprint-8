
from random import choices
from django.db import models


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.CharField(max_length=20, 
    choices = [('PERSONAL', 'PERSONAL'), ('HIPOTECARIO', 'HIPOTECARIO'), ('PRENDARIO', 'PRENDARIO')])
    loan_date = models.DateField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        db_table = 'prestamo'


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()
    employee_amnt_per_client = models.FloatField()
    given_credit_cards = models.IntegerField()
    given_dedit_cards = models.IntegerField()
    average_given_loans = models.TextField()

    class Meta:
        db_table = 'sucursal'        