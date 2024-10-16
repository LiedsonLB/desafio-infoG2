from django.db import models

class Survivor(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    last_location_latitude = models.FloatField()
    last_location_longitude = models.FloatField()
    infected = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Resource(models.Model):
    WATER = 'water'
    FOOD = 'food'
    MEDICATION = 'medication'
    AMMUNITION = 'ammunition'
    RESOURCE_CHOICES = [
        (WATER, 'Water'),
        (FOOD, 'Food'),
        (MEDICATION, 'Medication'),
        (AMMUNITION, 'Ammunition'),
    ]

    survivor = models.ForeignKey(Survivor, on_delete=models.CASCADE, related_name='resources')
    resource_type = models.CharField(max_length=20, choices=RESOURCE_CHOICES)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.resource_type} - {self.quantity}"