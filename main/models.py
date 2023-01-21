from django.db import models
from location_field.models.plain import PlainLocationField

# Create your models here.
class Cycle(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    current_location = PlainLocationField(based_fields=['city'], zoom=7)
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True)
    rate = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    image = models.ImageField( upload_to='static/images',null=True, blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class UserCycle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE)
    distance = models.FloatField()

    def __str__(self):
        return str(self.user.name)

ORDER_STATUS_CHOICES = (
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
    )

class Order(models.Model):
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    starting_point = PlainLocationField(based_fields=['city'], zoom=7, null = True, blank = True)
    end_point = PlainLocationField(based_fields=['city'], zoom=7, null = True, blank = True)

    def __str__(self):
        return str(self.cycle.id)



class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')
    end_point = PlainLocationField(based_fields=['city'], zoom=7, null = True, blank = True)
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE, null=True, blank=True)
    estimated_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    estimated_time = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.cycle.id)