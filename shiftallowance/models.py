# models.py
from django.db import models
from django.contrib.auth.models import User

shift_choices = [
    ('Morning', 'Morning'),
    ('Night', 'Night'),
]


class Shift(models.Model):
    team_member = models.ForeignKey(User, on_delete=models.CASCADE)
    shift_type = models.CharField(max_length=10, choices=shift_choices)
    nightShiftComment = models.CharField(default="N/A",help_text="eg CRQ NO.",max_length=40,verbose_name="Night Comment")
    date = models.DateField()

    class Meta:
        # Define unique_together attribute to specify the combination of fields
        unique_together = ['team_member', 'shift_type', 'date']
    

    def __str__(self):
        return f"{self.date} - {self.shift_type} - {self.team_member}"
    

country = [
    ('Kenya','Kenya'),
    ('India','India')
]

class UserInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    employeeID = models.IntegerField()
    team = models.CharField(max_length=50,choices=country,default='Kenya')


class onShift(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField()

