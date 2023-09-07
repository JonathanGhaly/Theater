# seats/models.py
from django.db import models

class Seat(models.Model):
        # Define choices for the 'status' field
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('selected', 'Selected'),
        ('reserved', 'Reserved'),
    )
    COL_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    )
    row = models.CharField(max_length=10)
    number = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    COL = models.CharField(max_length=10, choices=COL_CHOICES, default='1')
