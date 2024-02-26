# models.py
from django.db import models
from django.contrib.auth.models import User

shift_choices = [
    ('Morning', 'Morning'),
    ('Night', 'Night'),
]

country = [
    ('Kenya','Kenya'),
    ('India','India')
]

class Shift(models.Model):
    team_member = models.ForeignKey(User, on_delete=models.CASCADE)
    shift_type = models.CharField(max_length=10, choices=shift_choices)
    team = models.CharField(max_length=50,choices=country,default='Kenya')
    nightShiftComment = models.CharField(default="N/A",help_text="eg CRQ NO.",max_length=40,verbose_name="Night Comment")
    date = models.DateField()
    

    def __str__(self):
        return f"{self.date} - {self.shift_type} - {self.team_member}"



