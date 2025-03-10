from django.db import models
from django.contrib.auth.models import User

class Package(models.Model):
    STATUS = [
        ('pending', 'Pending'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
    ]

    t_number = models.CharField(max_length=20, unique=True)
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    address = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    driver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_deleted = models.BooleanField(default=False) 

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def __str__(self):
        return self.t_number
